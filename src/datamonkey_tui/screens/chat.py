"""Chat interface screen."""

from textual.app import ComposeResult
from textual.containers import Grid, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Input, TextArea, Button, ListView, ListItem
from textual.markup import escape

from ..api.client import DatamonkeyClient


class ChatScreen(Screen):
    """Chat interface for interacting with the AI assistant."""
    
    BINDINGS = [
        ("escape", "pop_screen", "Back"),
        ("c", "clear_chat", "Clear"),
        ("n", "new_conversation", "New"),
        ("ctrl+c", "copy_message", "Copy"),
    ]
    
    CSS = """
    ChatScreen {
        layout: grid;
        grid-size: 2 3;
        grid-columns: 1fr 2fr;
        grid-rows: auto 1fr auto;
    }
    
    .header {
        column-span: 2;
    }
    
    .conversations {
        border: solid $primary;
        padding: 1;
        margin: 1;
    }
    
    .chat-container {
        layout: grid;
        grid-columns: 1fr;
        grid-rows: auto 1fr auto;
        row-span: 2;
        border: solid $secondary;
        padding: 1;
        margin: 1;
    }

    .input-container {
        column-span: 2;
        border-top: solid $panel;
        padding: 1;
        background: $surface;
    }
    
    .conversation-title {
        text-style: bold;
        color: $primary;
    }
    
    .message-user {
        color: $accent;
        margin: 0 1;
    }
    
    .message-ai {
        color: $text;
        margin: 0 1;
        background: $surface;
        padding: 0 1;
    }
    
    .message-input {
        height: 3;
        border: solid $primary;
        max-height: 3;  # Force single line
        width: 1fr;
    }

    .input-row {
        height: 3;
        align: center middle;
    }

    .input-hint {
        color: $text-muted;
        margin-bottom: 1;
    }

    .send-button {
        margin: 0 1;
        background: $primary;
        min-width: 12;
        height: 3;
        text-align: center;
    }
    """
    
    def __init__(self, api_client: DatamonkeyClient):
        """Initialize the chat screen.
        
        Args:
            api_client: The Datamonkey API client
        """
        super().__init__()
        self.api_client = api_client
        self.current_conversation_id = None
    
    def compose(self) -> ComposeResult:
        """Create the chat screen layout."""
        yield Header(classes="header")
        
        # Conversations list
        with Vertical(classes="conversations"):
            yield Static("Conversations", classes="conversation-title")
            yield ListView(id="conversation-list")
            yield Button("New Conversation", id="new-btn", variant="primary")
        
        # Chat messages and input area container
        with Grid(classes="chat-container"):
            yield Static("Select a conversation or create a new one", id="chat-title")
            yield TextArea(id="messages")
            with Vertical(classes="input-container"):
                yield Static("Type your message and press Enter or click Send", classes="input-hint")
                with Horizontal(classes="input-row"):
                    yield Input(
                        placeholder="Start typing…",
                        id="message-input",
                        classes="message-input"
                    )
                    yield Button("📤 Send", id="send-btn", classes="send-button")

        yield Footer()
    
    def key_esc(self) -> None:
        """Handle ESC key to go back to main screen."""
        print("DEBUG: ESC key pressed in chat screen")  # Debug
        self.app.pop_screen()
    
    async def on_key(self, event) -> None:
        """Handle key events at the screen level."""
        print(f"DEBUG: Screen key event: {event.key}")  # Debug
        if event.key == "enter":
            try:
                input_widget = self.query_one("#message-input", Input)
                if input_widget.has_focus and input_widget.value.strip():
                    print("DEBUG: Sending message from screen key handler")  # Debug
                    await self.send_message()
                    event.stop()
            except Exception as e:
                print(f"DEBUG: Error in screen key handler: {e}")  # Debug
    
    async def key_ctrl_enter(self) -> None:
        """Handle Ctrl+Enter to send message."""
        print("DEBUG: Ctrl+Enter key pressed in chat screen")  # Debug
        await self.send_message()
    
    async def on_mount(self) -> None:
        """Initialize the screen when mounted."""
        # Make messages textarea readonly
        messages_widget = self.query_one("#messages", TextArea)
        messages_widget.read_only = True
        messages_widget.can_focus = False
        
        # Focus the input widget for better UX
        input_widget = self.query_one("#message-input", Input)
        input_widget.focus()
        
        await self.load_conversations()
    
    async def load_conversations(self) -> None:
        """Load the list of conversations."""
        try:
            response = await self.api_client.list_conversations()
            conversation_list = self.query_one("#conversation-list", ListView)
            conversation_list.clear()
            
            if response.conversations:
                for conv in response.conversations:
                    item = ListItem(
                        Static(conv.title or f"Conversation {conv.id[:8]}"),
                        id=conv.id
                    )
                    conversation_list.append(item)
            else:
                conversation_list.append(ListItem(Static("No conversations yet")))
                
        except ValueError as e:
            # Handle authentication requirement
            if "Authentication required" in str(e):
                self.notify("🔐 Please create a new conversation first to get authenticated")
                conversation_list = self.query_one("#conversation-list", ListView)
                conversation_list.clear()
                conversation_list.append(ListItem(Static("Create your first conversation to get started")))
            else:
                self.notify(escape(f"Failed to load conversations: {e}"))
        except Exception as e:
            self.notify(escape(f"Failed to load conversations: {e}"))
    
    async def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Handle conversation selection."""
        if event.item.id == "new-btn":
            await self.action_new_conversation()
        else:
            await self.load_conversation(event.item.id)
    
    async def action_new_conversation(self) -> None:
        """Create a new conversation."""
        try:
            response = await self.api_client.create_conversation()
            self.current_conversation_id = response.id
            
            # Update UI
            title_widget = self.query_one("#chat-title", Static)
            title_widget.update(f"New Conversation: {response.id[:8]}")
            
            # Clear messages
            messages_widget = self.query_one("#messages", TextArea)
            messages_widget.clear()
            
            # Reload conversation list
            await self.load_conversations()
            
            self.notify(escape("New conversation created"))
            
        except Exception as e:
            self.notify(escape(f"Failed to create conversation: {e}"))
    
    async def load_conversation(self, conversation_id: str) -> None:
        """Load a specific conversation."""
        try:
            self.current_conversation_id = conversation_id

            
            # Get conversation details
            conv_response = await self.api_client.get_conversation(conversation_id)
            
            # Get messages
            messages_response = await self.api_client.get_messages(conversation_id)
            
            # Update UI
            title_widget = self.query_one("#chat-title", Static)
            title_widget.update(conv_response.title or f"Conversation {conversation_id[:8]}")
            
            # Display messages
            messages_widget = self.query_one("#messages", TextArea)
            messages_widget.clear()
            
            if messages_response.messages:
                for msg in messages_response.messages:
                    if msg.role == "user":
                        messages_widget.insert(f"You: {msg.content}\n\n")
                    else:
                        self._insert_ai_message(messages_widget, msg.content)

            messages_widget.home()

        except Exception as e:
            self.notify(escape(f"Failed to load conversation: {e}"))
    
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "send-btn":
            await self.send_message()
        elif event.button.id == "new-btn":
            await self.action_new_conversation()
    
    async def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle input submission."""
        print(f"DEBUG: Input submitted from {event.input.id} with value: '{event.input.value}'")  # Debug
        if event.input.id == "message-input":
            print("DEBUG: Sending message via on_input_submitted")  # Debug
            await self.send_message()
    
    async def send_message(self) -> None:
        """Send a message to the current conversation."""
        if not self.current_conversation_id:
            self.notify(escape("Please create or select a conversation first"))
            return

        input_widget = self.query_one("#message-input", Input)
        message = input_widget.value.strip()

        if not message:
            return

        try:
            # Add user message to UI
            messages_widget = self.query_one("#messages", TextArea)
            messages_widget.insert(f"You: {message}\n\n")

            # Clear input
            input_widget.value = ""

            # Send to API
            response = await self.api_client.send_message(
                self.current_conversation_id, 
                message
            )

            # Add AI response to UI
            if hasattr(response, "message") and response.message is not None:
                ai_content = getattr(response.message, "content", "")
            else:
                ai_content = getattr(response, "content", "")

            self._insert_ai_message(messages_widget, ai_content)
            messages_widget.move_cursor((messages_widget.document.line_count - 1, 0))

        except Exception as e:
            self.notify(escape(f"Failed to send message: {e}"))

    def _insert_ai_message(self, messages_widget: TextArea, content: str) -> None:
        """Insert the AI's response into the chat history."""
        if not content:
            messages_widget.insert("AI: (no response)\n\n")
            return

        messages_widget.insert(f"AI: {content}\n\n")
    
    async def action_clear_chat(self) -> None:
        """Clear the current chat messages."""
        messages_widget = self.query_one("#messages", TextArea)
        messages_widget.clear()
        self.notify(escape("Chat cleared"))
    
    async def action_copy_message(self) -> None:
        """Copy the last message to clipboard."""
        # This would require a clipboard library
        self.notify(escape("Copy feature not yet implemented"))

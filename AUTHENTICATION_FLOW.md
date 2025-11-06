# Datamonkey TUI - Authentication Flow

## 🎯 Correct Authentication Flow

The TUI now follows the correct authentication pattern where **create operations generate tokens** and **read operations require existing tokens**.

## 📋 Operations by Type

### 🔑 **Token-Generating Operations** (Create new assets)
These operations can be performed without a token and will return a new token in the response headers:

- **Create Conversation** - `POST /conversations`
- **Upload Dataset** - `POST /datasets`  
- **Create Visualization** - `POST /visualizations`
- **Create Job** - `POST /jobs` (when implemented)

### 🔒 **Token-Required Operations** (Access existing assets)
These operations require an existing token to access user's data:

- **List Conversations** - `GET /conversations`
- **Get Conversation** - `GET /conversations/{id}`
- **Send Message** - `POST /conversations/{id}/messages`
- **Get Messages** - `GET /conversations/{id}/messages`
- **List Datasets** - `GET /datasets`
- **Get Dataset** - `GET /datasets/{id}`
- **List Visualizations** - `GET /visualizations`
- **Get Visualization** - `GET /visualizations/{id}`

## 🚀 User Workflow

### **First-Time User:**
1. **Start TUI** → Shows "💡 Start by uploading a dataset or creating a chat to get authenticated"
2. **Create Conversation** → API returns new token → Auto-saved → UI shows "🔐 Auto-authenticated successfully!"
3. **Main Screen Updates** → Shows "✅ Authenticated - Ready to use all features!"
4. **Access All Features** → Can now list conversations, datasets, visualizations

### **Returning User:**
1. **Start TUI** → Auto-loads saved token → Shows "✅ Authenticated - Ready to use all features!"
2. **Use All Features** → Full access to existing data

## 🔧 Technical Implementation

### **API Client Logic:**

```python
# Token-Generating Operations
async def create_conversation(self):
    headers = self._get_headers()  # May be empty
    result = await self.chat.create_conversation(_headers=headers, **body)
    self._extract_and_save_token(result)  # Extract token from response headers
    return result

# Token-Required Operations  
async def list_conversations(self):
    token = session_manager.get_token()
    if not token:
        raise ValueError("Authentication required. Please create a conversation first.")
    return await self.chat.list_user_conversations(user_token=token)
```

### **Token Extraction:**
- Checks response headers for: `user_token`, `x-user-token`, `authorization`, `x-auth-token`
- Auto-saves new tokens to `~/.config/datamonkey/session.json`
- Triggers UI refresh callback when new token extracted

### **Error Handling:**
- Graceful handling of missing tokens with helpful error messages
- Clear guidance on what action to take to get authenticated
- Visual feedback when authentication is successful

## 📱 UI Experience

### **Main Screen Status:**
- **No Token**: "💡 Start by uploading a dataset or creating a chat to get authenticated"
- **Has Token**: "✅ Authenticated - Ready to use all features!"

### **Screen Behaviors:**
- **Chat Screen**: Shows "Create your first conversation to get started" if no token
- **Dataset Screen**: Shows "Upload your first dataset to get started" if no token  
- **Visualization Screen**: Shows "Create your first job to get started" if no token

### **Notifications:**
- "🔐 Auto-authenticated successfully!" - When token extracted
- "🔐 Please create a new conversation first to get authenticated" - Guidance message

## 🛡️ Security Benefits

1. **Minimal Token Exposure**: Only create operations expose tokens
2. **Clear Access Pattern**: Users understand when they need to authenticate
3. **Automatic Management**: Tokens handled transparently
4. **Persistent Sessions**: Tokens saved across TUI sessions
5. **Secure Storage**: Tokens stored in user config directory

## 📊 Example Flow

```bash
# 1. User starts TUI (no token)
python -m datamonkey_tui
# Shows: "💡 Start by uploading a dataset or creating a chat to get authenticated"

# 2. User creates conversation
# API Call: POST /conversations (no token)
# Response: New token in headers
# Action: Token auto-saved, UI refreshes
# Shows: "🔐 Auto-authenticated successfully!"

# 3. User can now access all features
# API Call: GET /conversations (with token)
# Response: User's conversation list
# Shows: Conversation list populated
```

This creates a natural, intuitive authentication flow that matches how the Datamonkey API actually works! 🎉

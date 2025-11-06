# Authentication Guide for Datamonkey TUI

## Overview

The TUI now provides a seamless authentication experience with automatic session management and clear user guidance.

## ✅ New Authentication Features

### 1. **Visual Session Status**
- **Main screen** shows authentication status at startup
- ✅ **Green**: "Authenticated - Ready to use!" 
- ⚠️ **Yellow**: "Not authenticated - Please set your session token first"
- 👆 **Cyan**: "Press 'S' or click Session button to authenticate"

### 2. **Automatic Authentication Check**
- Protected features (Chat, Datasets, Visualizations) require authentication
- Auto-redirect to Session screen if not authenticated
- Clear notification messages guide users

### 3. **Enhanced Session Screen**
- Step-by-step instructions for getting API token
- Better placeholder text ("Paste your API token here...")
- Visual feedback for save/clear operations
- Automatic return to main screen with status refresh

### 4. **Session Persistence**
- Tokens stored in `~/.config/datamonkey/session.json`
- Automatic loading on startup
- Persistent across TUI sessions

## 🔐 How It Works

### First-Time User Flow:

1. **Start TUI** → Shows "Not authenticated" warning
2. **Click any feature** → Auto-redirects to Session screen
3. **Follow instructions** → Get token from web interface
4. **Paste token** → Save and return to main screen
5. **Status updates** → Shows "Authenticated - Ready to use!"

### Returning User Flow:

1. **Start TUI** → Automatically loads saved token
2. **Shows "Authenticated"** → Ready to use all features
3. **Optional** → Go to Session screen to update/clear token

## 🎯 User Experience Improvements

### **Before:**
- ❌ No indication authentication was needed
- ❌ Users had to manually find Session screen
- ❌ No guidance on getting a token
- ❌ Errors when trying unauthenticated actions

### **After:**
- ✅ Clear visual status indicators
- ✅ Auto-redirect when authentication needed
- ✅ Step-by-step token instructions
- ✅ Seamless session management
- ✅ Persistent authentication

## 📝 Session File Location

```
~/.config/datamonkey/
├── session.json          # Stored authentication token
├── logs/
│   └── datamonkey_tui.log # Application logs
└── config.json           # User configuration
```

## 🔧 Configuration

### Environment Variables (.env):
```bash
# API endpoint
DATAMONKEY_API_URL=http://localhost:9300

# Logging level
LOG_LEVEL=INFO

# Custom config directory (optional)
CONFIG_DIR=~/.config/datamonkey
```

## 🚀 Quick Start

```bash
# 1. Start the TUI
python -m datamonkey_tui

# 2. Follow the authentication prompts
# 3. Paste your API token when redirected
# 4. Start using all features!
```

## 🛡️ Security Features

- **Token masking**: Tokens are hidden in input fields
- **Secure storage**: Tokens stored in user config directory
- **Automatic cleanup**: Clear token option available
- **Session validation**: Token checked before API calls

## 📊 Authentication Status Tracking

The main screen dynamically updates to show:
- Current authentication state
- Visual indicators (colors/icons)
- Actionable guidance for users
- Real-time status refresh after token changes

This creates a professional, user-friendly authentication experience that guides users through the setup process seamlessly! 🔐✨

# 🎙️ FOMO Voice Club

**Private Voice Podcast Platform with Live Streaming & Gamification**

[![React](https://img.shields.io/badge/React-18.x-blue)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0+-green)](https://www.mongodb.com/)
[![LiveKit](https://img.shields.io/badge/LiveKit-WebRTC-orange)](https://livekit.io/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)](https://core.telegram.org/bots)

---

## 📋 Overview

FOMO Voice Club is a private voice podcast platform that combines:
- 🎤 **Live Voice Streaming** via LiveKit WebRTC
- 📱 **Telegram Integration** for notifications and recording
- 🏆 **Gamification System** with XP, Levels, and Badges
- 🔐 **Wallet-based Authentication** for private club access
- 📊 **Analytics Dashboard** for club management
- 💬 **Comments System** with nested replies, reactions, and emoji picker
- 📚 **Personal Library** with saved and liked podcasts

---

## 🏗️ Architecture

```
/app
├── backend/                    # FastAPI Backend
│   ├── routes/                 # API Endpoints (modular)
│   │   ├── podcasts.py         # Podcast CRUD, reactions, saves
│   │   ├── comments.py         # Comments with replies & reactions
│   │   ├── library.py          # User library (saved/liked)
│   │   ├── live_sessions.py    # Live streaming
│   │   ├── xp.py               # XP & Levels
│   │   ├── badges.py           # Badge system
│   │   ├── admin_panel.py      # Admin management
│   │   └── ...
│   ├── models.py               # Pydantic models
│   ├── server.py               # Main FastAPI app
│   ├── requirements.txt        # Python dependencies
│   └── .env.example            # Environment template
│
├── frontend/                   # React Frontend
│   ├── src/
│   │   ├── components/         # Reusable UI components
│   │   │   ├── ui/             # shadcn/ui components
│   │   │   ├── library/        # Library page components
│   │   │   ├── CommentsSection.jsx
│   │   │   ├── Navigation.jsx
│   │   │   ├── GlobalPlayer.jsx
│   │   │   └── ...
│   │   ├── pages/              # Route pages
│   │   │   ├── Home.jsx        # Homepage with filters
│   │   │   ├── PodcastDetail.jsx
│   │   │   ├── Library.jsx     # Personal library
│   │   │   ├── MyProgress.jsx  # User progress & badges
│   │   │   ├── CreatePodcast.jsx
│   │   │   └── ...
│   │   ├── context/            # React contexts
│   │   └── utils/              # Helper functions
│   ├── package.json            # Node.js dependencies
│   └── .env.example            # Environment template
│
└── docs/                       # Documentation
```

---

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.11+
- MongoDB 6.0+
- Yarn (preferred over npm)

### Installation

#### 1. Clone the repository
```bash
git clone https://github.com/your-org/fomo-voice-club.git
cd fomo-voice-club
```

#### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your credentials
```

#### 3. Frontend Setup
```bash
cd frontend

# Install dependencies (use yarn, not npm!)
yarn install

# Configure environment
cp .env.example .env
# Edit .env with your backend URL
```

#### 4. Start Services
```bash
# Terminal 1 - Backend
cd backend
uvicorn server:app --host 0.0.0.0 --port 8001 --reload

# Terminal 2 - Frontend
cd frontend
yarn start
```

#### 5. Open in browser
- Frontend: http://localhost:3000
- API Docs: http://localhost:8001/docs

---

## ⚙️ Configuration

### Backend Environment Variables (.env)

| Variable | Description | Required | Example |
|----------|-------------|----------|----------|
| `MONGO_URL` | MongoDB connection string | ✅ | `mongodb://localhost:27017` |
| `DB_NAME` | Database name | ✅ | `fomo_voice_club` |
| `JWT_SECRET_KEY` | JWT signing key | ✅ | `your-secret-key` |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | ❌ | `123456:ABC...` |
| `LIVEKIT_URL` | LiveKit server URL | ❌ | `wss://your-livekit.com` |
| `LIVEKIT_API_KEY` | LiveKit API key | ❌ | `APIxxxx` |
| `LIVEKIT_API_SECRET` | LiveKit secret | ❌ | `secret...` |

### Frontend Environment Variables (.env)

| Variable | Description | Example |
|----------|-------------|----------|
| `REACT_APP_BACKEND_URL` | Backend API URL | `http://localhost:8001` |

---

## 📚 Features

### 🎤 Podcasts
- Upload and stream audio podcasts
- AI-powered transcription and summaries
- **Category-based organization** with filtering
- Duration and date range filtering
- Like and Save functionality
- Detailed analytics (views, plays, likes, comments)

### 💬 Comments System
- Nested replies with threading
- Emoji reactions (❤️ 🔥 👏 😮 😢)
- Quote replies
- Real-time updates

### 📚 Personal Library
- **Saved** - Bookmarked podcasts
- **Liked** - Favorite podcasts (heart reactions)
- **Playlists** - Custom collections

### 🔴 Live Streaming
- Real-time voice rooms via LiveKit
- Hand raise queue system
- Live chat with reactions
- Recording to Telegram channel

### 🏆 Gamification
- **5 Levels**: Observer → Active → Contributor → Speaker → Core Voice
- **XP System**: Earn XP for listening, attending, speaking
- **14 Badges**: Participation, Contribution, Authority categories
- **Leaderboard**: Top members by XP
- Auto-grant all badges to admins

### 👥 Club Management
- Wallet-based roles (Owner, Admin, Member)
- Private club access control
- Analytics dashboard
- Moderation tools

---

## 🔌 API Endpoints

### Podcasts
```
GET    /api/podcasts                    # List all podcasts
POST   /api/podcasts                    # Create podcast
GET    /api/podcasts/{id}               # Get podcast details
POST   /api/podcasts/{id}/save          # Toggle save
POST   /api/podcasts/{id}/reactions     # Add/remove reaction
GET    /api/podcasts/{id}/reactions     # Get reactions count
```

### Library
```
GET    /api/library/saved/{user_id}     # Get saved podcasts
GET    /api/library/liked/{user_id}     # Get liked podcasts
```

### Comments
```
GET    /api/podcasts/comments/{podcast_id}       # Get comments
POST   /api/podcasts/comments                    # Add comment
PUT    /api/podcasts/comments/{id}/react         # Add reaction
```

### Live Sessions
```
GET    /api/live-sessions/sessions      # List live sessions
POST   /api/live-sessions/sessions      # Create session
GET    /api/live-sessions/{id}          # Join session
```

### Gamification
```
GET    /api/xp/{user_id}/progress       # User progress
GET    /api/users/{user_id}/badges      # User badges
GET    /api/xp/leaderboard              # XP leaderboard
```

### Admin
```
GET    /api/admin/settings              # Club settings
POST   /api/admin/settings              # Update settings
GET    /api/admin/check-role/{wallet}   # Check user role
POST   /api/admin/add-admin             # Add admin (grants all badges)
```

---

## 🖥️ Pages

| Route | Page | Description |
|-------|------|-------------|
| `/` | Home | Podcast catalog with search, sort, filters |
| `/podcast/{id}` | Podcast Detail | Player, comments, analytics |
| `/library` | My Library | Saved, Liked, Playlists tabs |
| `/progress` | My Progress | XP, Level, Badges |
| `/members` | Members | Club members list |
| `/leaderboard` | Leaderboard | Top XP earners |
| `/create` | Create Podcast | Upload or Go Live |
| `/admin` | Admin Panel | Club management |
| `/live/{id}` | Live Room | Live streaming room |

---

## 🧪 Testing

### Test Mode (Frontend)
Use browser console to simulate different user roles:
```javascript
// Test as Owner
localStorage.setItem('testMode', 'owner');
location.reload();

// Test as Admin
localStorage.setItem('testMode', 'admin');
location.reload();

// Test as Regular User
localStorage.setItem('testMode', 'user');
location.reload();
```

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
yarn test
```

---

## 🚀 Deployment

### Production Checklist

1. **Environment Variables**
   - Set production `MONGO_URL`
   - Generate strong `JWT_SECRET_KEY`
   - Configure `REACT_APP_BACKEND_URL` to production API

2. **Build Frontend**
   ```bash
   cd frontend
   yarn build
   ```

3. **Backend**
   - Use production ASGI server (gunicorn + uvicorn workers)
   - Enable CORS for your domain
   - Configure reverse proxy (nginx/caddy)

4. **Database**
   - Create indexes for performance
   - Set up backups
   - Configure authentication

### Docker (Optional)
```bash
docker-compose up -d
```

---

## 📝 Changelog (Latest Session)

### ✅ Completed
- **Like/Save Functionality** - Fixed API to correctly populate Library
- **Library Page** - Removed "My Podcasts" tab, kept Saved/Liked/Playlists
- **Podcast Detail Page** - Added Description/Transcript/AI Summary blocks
- **Homepage** - Redesigned search/sort/filter bar
- **Categories** - Replaced Tags with Categories in filters
- **Create Podcast** - Added Category field
- **Comments** - Full-featured system with replies and reactions
- **Badges** - Auto-grant to admins, monochrome design

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- [LiveKit](https://livekit.io/) - WebRTC infrastructure
- [shadcn/ui](https://ui.shadcn.com/) - UI components
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [Tailwind CSS](https://tailwindcss.com/) - Styling
- [React](https://reactjs.org/) - Frontend framework

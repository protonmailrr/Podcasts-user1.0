# 🎙️ FOMO Voice Club

**Private Voice Podcast Platform with Live Streaming & Gamification**

[![React](https://img.shields.io/badge/React-18.x-blue)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0+-green)](https://www.mongodb.com/)
[![LiveKit](https://img.shields.io/badge/LiveKit-WebRTC-orange)](https://livekit.io/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)](https://core.telegram.org/bots)

## 📋 Overview

FOMO Voice Club is a private voice podcast platform that combines:
- 🎤 **Live Voice Streaming** via LiveKit WebRTC
- 📱 **Telegram Integration** for notifications and recording
- 🏆 **Gamification System** with XP, Levels, and Badges
- 🔐 **Wallet-based Authentication** for private club access
- 📊 **Analytics Dashboard** for club management

## 🏗️ Architecture

```
/app
├── backend/                 # FastAPI Backend
│   ├── routes/             # API Endpoints (modular)
│   │   ├── podcasts.py     # Podcast CRUD
│   │   ├── live_sessions.py # Live streaming
│   │   ├── xp.py           # XP & Levels
│   │   ├── badges.py       # Badge system
│   │   └── ...
│   ├── services/           # Business logic
│   ├── models.py           # Pydantic models
│   └── server.py           # Main FastAPI app
│
├── frontend/               # React Frontend
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   │   ├── ui/         # shadcn/ui components
│   │   │   └── ...
│   │   ├── pages/          # Route pages
│   │   ├── context/        # React contexts
│   │   └── utils/          # Helper functions
│   └── package.json
│
└── tests/                  # Test files
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.11+
- MongoDB 6.0+

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-org/fomo-voice-club.git
cd fomo-voice-club
```

2. **Backend Setup**
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
```

3. **Frontend Setup**
```bash
cd frontend
yarn install
cp .env.example .env
```

4. **Start Services**
```bash
# Backend
uvicorn server:app --host 0.0.0.0 --port 8001

# Frontend
yarn start
```

## ⚙️ Configuration

### Backend Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `MONGO_URL` | MongoDB connection string | ✅ |
| `DB_NAME` | Database name | ✅ |
| `JWT_SECRET_KEY` | JWT signing key | ✅ |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | ❌ |
| `LIVEKIT_URL` | LiveKit server URL | ❌ |
| `LIVEKIT_API_KEY` | LiveKit API key | ❌ |
| `LIVEKIT_API_SECRET` | LiveKit secret | ❌ |

### Frontend Environment Variables

| Variable | Description |
|----------|-------------|
| `REACT_APP_BACKEND_URL` | Backend API URL |

## 📚 Features

### 🎤 Podcasts
- Upload and stream audio podcasts
- AI-powered transcription and summaries
- Tag-based organization
- Duration and date filtering

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

### 👥 Club Management
- Wallet-based roles (Owner, Admin, Member)
- Private club access control
- Analytics dashboard
- Moderation tools

## 🔌 API Endpoints

### Core Endpoints
```
GET  /api/                      # API info
GET  /api/podcasts              # List podcasts
POST /api/podcasts              # Create podcast
GET  /api/podcasts/{id}         # Get podcast

GET  /api/live-sessions/sessions  # List live sessions
POST /api/live-sessions/sessions  # Create session
GET  /api/live-sessions/{id}      # Join session

GET  /api/xp/{user_id}/progress   # User progress
GET  /api/users/{user_id}/badges  # User badges
GET  /api/xp/leaderboard          # XP leaderboard
```

### Admin Endpoints
```
GET  /api/admin/settings        # Club settings
POST /api/admin/settings        # Update settings
GET  /api/admin/check-role/{wallet}  # Check user role
```

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
yarn test
```

## 📝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [LiveKit](https://livekit.io/) - WebRTC infrastructure
- [shadcn/ui](https://ui.shadcn.com/) - UI components
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [Tailwind CSS](https://tailwindcss.com/) - Styling

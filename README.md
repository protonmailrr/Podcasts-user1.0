# FOMO Podcasts Platform

Приватная платформа для голосовых подкастов с Telegram интеграцией, live streaming и gamification системой.

## 🚀 Основные функции

- **Live Streaming** - WebRTC аудио через LiveKit
- **Telegram Voice Chat** - слушатели присоединяются через Telegram
- **Real-time Chat** - WebSocket чат с эмодзи реакциями
- **Hand Raise** - система поднятия руки для выступления
- **XP & Badges** - геймификация с уровнями и наградами
- **Telegram Integration** - уведомления + recording bot
- **Auto Podcast Creation** - автоматическое создание подкастов из live сессий
- **AI Summary** - AI генерация summary для подкастов
- **Admin Panel** - управление участниками и настройками

---

## 📁 Структура проекта

```
/app
├── backend/                    # FastAPI Backend
│   ├── server.py              # Главный сервер
│   ├── .env                   # Переменные окружения (КЛЮЧИ!)
│   ├── requirements.txt       # Python зависимости
│   ├── routes/                # API маршруты
│   │   ├── live_sessions.py   # Live streaming + WebSocket + Auto Podcast
│   │   ├── admin_panel.py     # Админка
│   │   ├── telegram.py        # Telegram интеграция
│   │   ├── xp.py              # XP система
│   │   └── ...
│   ├── services/
│   │   └── telegram_service.py # Telegram уведомления
│   ├── telegram_recording_bot.py # Бот записи из @Podcast_F
│   └── init_demo_users.py     # Инициализация демо данных
│
├── frontend/                   # React Frontend
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Home.jsx            # Главная (поиск, фильтры, теги)
│   │   │   ├── LiveRoom.jsx        # Live комната (host)
│   │   │   ├── LiveRoomView.jsx    # Live комната (listener)
│   │   │   ├── LiveManagement.jsx  # Управление стримами
│   │   │   ├── PodcastDetail.jsx   # Страница подкаста
│   │   │   └── ...
│   │   └── components/
│   │       ├── PodcastCard.jsx     # Карточка подкаста
│   │       └── ...
│   └── .env                   # Frontend переменные
│
├── README.md                  # Этот файл
├── QUICKSTART.md              # Быстрый запуск
└── TASKS.md                   # Текущие задачи
```

---

## 🔑 Ключи и API

### Расположение: `/app/backend/.env`

```env
# MongoDB
MONGO_URL="mongodb://localhost:27017"
DB_NAME="fomo_voice_club"

# JWT
JWT_SECRET_KEY="fomo-podcast-secret-key-2025"

# Telegram Bot
TELEGRAM_BOT_TOKEN="8293451127:AAEVo5vQV_vJqoziVTDKHYJiOYUZQN-2M2E"

# Telegram Channels (разделены на 2)
# @Podcast_F - для записей стримов (Recording Bot мониторит)
TELEGRAM_RECORDING_CHANNEL_ID="-1003133850361"
TELEGRAM_RECORDING_CHANNEL="Podcast_F"

# @P_FOMO - для уведомлений о стримах и Voice Chat
TELEGRAM_NOTIFICATIONS_CHANNEL_ID="-1003534592932"
TELEGRAM_NOTIFICATIONS_CHANNEL="P_FOMO"

# LiveKit (WebRTC Audio)
LIVEKIT_URL="wss://fomo-bxb0f38x.livekit.cloud"
LIVEKIT_API_KEY="APIqNLg599MoAHc"
LIVEKIT_API_SECRET="9wWu3BHo199HEcvcE22KMpcuSDfqy7K7TA5oXEOaXae"
```

---

## 📱 Telegram Integration (2 канала)

### Архитектура:

| Канал | ID | Назначение |
|-------|-----|------------|
| **@Podcast_F** | -1003133850361 | Записи стримов (Recording Bot мониторит) |
| **@P_FOMO** | -1003534592932 | Уведомления + Voice Chat для слушателей |

### Компоненты:

#### 1. Notification Bot (@Podcast_FOMO_bot)
- Отправляет уведомления о начале/завершении стримов в @P_FOMO
- Отправляет личные уведомления пользователям с подключённым Telegram
- Файл: `/app/backend/services/telegram_service.py`

#### 2. Recording Bot
- Мониторит канал @Podcast_F каждые 30 секунд
- Автоматически создаёт подкасты из аудио/видео записей
- Файл: `/app/backend/telegram_recording_bot.py`
- Запускается через Supervisor

### Флоу работы:

```
1. Админ создаёт Live Session на сайте
        ↓
2. Нажимает "Start" → уведомление в @P_FOMO
        ↓
3. Пользователи видят уведомление и переходят в @P_FOMO
        ↓
4. В @P_FOMO запускается Voice Chat
        ↓
5. Все слушают стрим в Telegram Voice Chat
        ↓
6. Админ нажимает "End" → создаётся подкаст + уведомление
        ↓
7. Если запись публикуется в @Podcast_F → Recording Bot обновляет подкаст с аудио
```

---

## 🎙️ Live Streaming

### Создание стрима:
1. Перейти в `/live-management`
2. Нажать "Create Live Session"
3. Ввести Title и Description
4. Нажать "Start" для запуска

### Для слушателей:
- На странице Live Room есть баннер **"Listen in Telegram Voice Chat"**
- Кнопка "Open Telegram" ведёт на `https://t.me/P_FOMO?voicechat`

### Auto Podcast Creation:
- При завершении стрима автоматически создаётся подкаст
- Статус: `awaiting_recording` (ожидает аудио файл)
- Когда Recording Bot найдёт запись → обновит подкаст с аудио

---

## 🏠 Home Page Features

### Поиск и фильтрация:
- Поиск по названию, описанию, тегам
- Фильтр по тегам (боковая панель)
- Сортировка: Newest, Oldest, Duration, Popular

### Группировка по тегам:
- Подкасты группируются по тегам
- Каждая группа = горизонтальный ряд со скроллом
- Например: "All Episodes", "Live", "Recording", "Club"

### Статистика наверху:
- Количество участников
- Общий XP
- Количество выступлений
- Топ 3 участника с аватарами

---

## 🎧 Podcast Detail Page

### Структура:
- **Player** - обложка с кнопкой Play, progress bar
- **Info** - название, автор, статистика, теги
- **Actions** - Like, Save, Share
- **Tabs** - Description, Transcript, AI Summary
- **Comments** - комментарии с возможностью добавления
- **Sidebar** - Analytics (Plays, Views, Likes, Comments)

### AI Summary:
- Генерируется после загрузки аудио и транскрипции
- Отображается в красивом градиентном блоке

---

## 📡 LiveKit Integration

### Что это?
LiveKit - WebRTC платформа для real-time аудио.

### API Endpoint:
```
POST /api/live-sessions/livekit/token
Body: {
  "session_id": "uuid",
  "user_id": "user-id",
  "username": "Name"
}
Response: {
  "token": "jwt-token",
  "url": "wss://fomo-bxb0f38x.livekit.cloud",
  "room": "session-id",
  "mock_mode": false
}
```

---

## 👤 Админ панель

### URL: `/admin`

### Функции:
- Управление кошельками (Owner, Admins)
- Список участников с XP
- Настройки клуба

---

## 🚀 Запуск

### 1. Backend
```bash
cd /app/backend
pip install -r requirements.txt
python init_demo_users.py  # Инициализация БД
```

### 2. Frontend
```bash
cd /app/frontend
yarn install
```

### 3. Сервисы
```bash
sudo supervisorctl restart all
sudo supervisorctl status
```

Все сервисы должны быть RUNNING:
- backend
- frontend
- telegram_recording_bot

---

## 📱 URL Структура

| URL | Описание |
|-----|----------|
| `/` | Главная (подкасты по тегам, поиск, фильтры) |
| `/live-management` | Управление стримами |
| `/live/{session_id}` | Live комната |
| `/podcast/{id}` | Страница подкаста |
| `/admin` | Админ панель |
| `/members` | Участники (Leaderboard) |
| `/progress` | Прогресс XP |
| `/library` | Библиотека подкастов |

---

## 🔧 Supervisor

Конфигурация Recording Bot: `/etc/supervisor/conf.d/telegram_bot.conf`
```ini
[program:telegram_recording_bot]
command=/root/.venv/bin/python /app/backend/telegram_recording_bot.py
directory=/app/backend
autostart=true
autorestart=true
```

---

## 📝 Демо аккаунты

| ID | Role | XP | Level |
|----|------|-----|-------|
| demo-owner-001 | Owner | 10,000 | 5 |
| demo-admin-002 | Admin | 5,000 | 4 |
| demo-user-003 | Member | 500 | 2 |

---

## 🛠️ Технологии

- **Backend**: FastAPI, Python, Motor (MongoDB async)
- **Frontend**: React, Tailwind CSS, shadcn/ui
- **Database**: MongoDB
- **Real-time**: WebSocket, LiveKit (WebRTC)
- **Telegram**: python-telegram-bot, aiogram

---

*Последнее обновление: 2026-01-03*

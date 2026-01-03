# 📝 CHANGELOG

История изменений проекта FOMO Podcasts Platform.

---

## [2026-01-03] - Major Update

### 🆕 New Features

#### Telegram Integration (2 каналов)
- **@P_FOMO** - канал для уведомлений и Voice Chat (слушатели)
- **@Podcast_F** - канал для записей (Recording Bot мониторит)
- Уведомления автоматически отправляются при старте/завершении стримов
- Ссылки на Voice Chat в уведомлениях

#### Auto Podcast Creation
- При завершении Live Session автоматически создаётся подкаст
- Статус `awaiting_recording` для подкастов без аудио
- Связь live_session ↔ podcast через `podcast_id`

#### Home Page Redesign
- Компактная статистика наверху (members, XP, speeches, Top 3)
- Поиск по названию, описанию, тегам
- Фильтр по тегам (боковая панель Sheet)
- Сортировка: Newest, Oldest, By Duration, Most Popular
- Группировка подкастов по тегам
- Горизонтальный скролл для каждой группы
- Названия тегов с большой буквы (без #)

#### Podcast Detail Redesign
- Чистый UX - player сверху с обложкой
- Tabs: Description, Transcript, AI Summary
- Analytics sidebar (Plays, Views, Likes, Comments)
- Comments section с возможностью добавления
- Убраны дублирующиеся элементы

#### Live Room Enhancement
- Баннер "🎧 Listen in Telegram Voice Chat"
- Кнопка "Open Telegram" → t.me/P_FOMO?voicechat
- Добавлено в LiveRoom.jsx и LiveRoomView.jsx

### 🔧 Improvements

#### PodcastCard Component
- Компактный дизайн с обложкой 16:10
- Play button появляется при hover
- Бейджи статуса: LIVE (красный), Awaiting Recording (оранжевый)
- Теги с большой буквы
- Статистика: views, likes, дата

#### Live Management
- Убрано поле "Telegram Channel ID" из формы
- Кнопка "Open Voice Chat" для live сессий
- Toast с ссылкой на Telegram при запуске

#### Interface
- Весь интерфейс на английском языке
- Select компонент для сортировки (красивый дизайн)
- Sheet компонент для фильтров

### 🐛 Bug Fixes
- Исправлена ошибка `likes.includes is not a function`
- Исправлены undefined values в PodcastCard
- Исправлена работа с datetime в live_sessions

### 📁 Files Changed
- `/app/backend/.env` - добавлены 2 Telegram канала
- `/app/backend/routes/live_sessions.py` - auto podcast creation
- `/app/backend/services/telegram_service.py` - уведомления с ссылками
- `/app/frontend/src/pages/Home.jsx` - полный редизайн
- `/app/frontend/src/pages/PodcastDetail.jsx` - полный редизайн
- `/app/frontend/src/pages/LiveRoom.jsx` - Telegram баннер
- `/app/frontend/src/pages/LiveRoomView.jsx` - Telegram баннер
- `/app/frontend/src/pages/LiveManagement.jsx` - убрано поле канала
- `/app/frontend/src/components/PodcastCard.jsx` - новый дизайн

---

## [Previous Versions]

### Phase 6: RSS & Webhooks + Modular Architecture
- RSS feed generation
- Webhooks для интеграций
- Модульная архитектура routes

### Phase 5: Telegram Recording Bot
- Автоматическое создание подкастов из Telegram
- Мониторинг канала @Podcast_F
- Supervisor конфигурация

### Phase 4: LiveKit Integration
- WebRTC аудио через LiveKit
- Real-time voice rooms
- Token generation API

### Phase 3: XP & Gamification
- XP система с уровнями
- Бейджи и награды
- Leaderboard

### Phase 2: Live Streaming
- WebSocket для real-time
- Hand raise система
- Chat с реакциями

### Phase 1: Core Platform
- Базовая структура
- MongoDB интеграция
- React frontend

---

*Последнее обновление: 2026-01-03*

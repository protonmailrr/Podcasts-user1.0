# 🚀 Quick Start Guide

Быстрый запуск FOMO Podcasts Platform.

---

## 1. Проверка сервисов

```bash
sudo supervisorctl status
```

Должны быть RUNNING:
- `backend` (FastAPI на порту 8001)
- `frontend` (React на порту 3000)
- `telegram_recording_bot` (Telegram бот)

---

## 2. Инициализация базы данных

```bash
cd /app/backend
python init_demo_users.py
python create_full_demo_data.py  # опционально
```

---

## 3. Проверка API

```bash
curl http://localhost:8001/api/
# {"message":"FOMO Podcast API","version":"6.0 - Phase 6: RSS & Webhooks + Modular Architecture"}
```

---

## 4. Доступ к приложению

| Страница | URL |
|----------|-----|
| Главная | https://YOUR-DOMAIN/ |
| Управление стримами | https://YOUR-DOMAIN/live-management |
| Админ панель | https://YOUR-DOMAIN/admin |

---

## 5. Создание Live Stream

### На сайте:
1. Перейти в `/live-management`
2. Нажать **"Create Live Session"**
3. Заполнить Title и Description
4. Нажать **"Start"**

### В Telegram:
1. Уведомление автоматически отправится в @P_FOMO
2. Слушатели присоединяются через Voice Chat в Telegram

### Завершение:
1. Нажать **"End"** на странице стрима
2. Автоматически создаётся подкаст
3. Уведомление о завершении в @P_FOMO

---

## 6. Telegram каналы

| Канал | Назначение |
|-------|------------|
| **@P_FOMO** | Уведомления + Voice Chat (слушатели здесь) |
| **@Podcast_F** | Записи стримов (Recording Bot мониторит) |

### Бот: @Podcast_FOMO_bot
- Должен быть администратором в обоих каналах
- Права: публикация сообщений

---

## 7. Запись стримов

### Вариант 1: Через Telegram
1. Запустить Voice Chat в @P_FOMO
2. Включить запись (настройки Voice Chat)
3. После окончания → отправить запись в @Podcast_F
4. Recording Bot автоматически создаст подкаст

### Вариант 2: Через LiveKit
1. Присоединиться к Audio Room на сайте
2. LiveKit записывает аудио
3. При завершении → аудио сохраняется

---

## 8. Перезапуск сервисов

```bash
# Все сервисы
sudo supervisorctl restart all

# Отдельно
sudo supervisorctl restart backend
sudo supervisorctl restart frontend
sudo supervisorctl restart telegram_recording_bot
```

---

## 9. Просмотр логов

```bash
# Backend
tail -f /var/log/supervisor/backend.err.log

# Frontend
tail -f /var/log/supervisor/frontend.err.log

# Telegram Bot
tail -f /var/log/supervisor/telegram_bot.err.log
```

---

## 10. Переменные окружения

### Backend (`/app/backend/.env`):
```env
MONGO_URL="mongodb://localhost:27017"
DB_NAME="fomo_voice_club"
JWT_SECRET_KEY="your-secret"
TELEGRAM_BOT_TOKEN="your-bot-token"
TELEGRAM_RECORDING_CHANNEL_ID="-100..."
TELEGRAM_NOTIFICATIONS_CHANNEL_ID="-100..."
LIVEKIT_URL="wss://your-livekit.cloud"
LIVEKIT_API_KEY="your-key"
LIVEKIT_API_SECRET="your-secret"
```

### Frontend (`/app/frontend/.env`):
```env
REACT_APP_BACKEND_URL=https://your-domain
```

---

## 11. Troubleshooting

### Backend не запускается:
```bash
tail -n 50 /var/log/supervisor/backend.err.log
pip install -r /app/backend/requirements.txt
```

### Telegram бот не работает:
1. Проверить токен в `.env`
2. Проверить что бот - админ в каналах
3. Проверить логи: `tail -f /var/log/supervisor/telegram_bot.err.log`

### Live сессия не создаётся:
```bash
curl -X POST http://localhost:8001/api/live-sessions/sessions \
  -H "Content-Type: application/json" \
  -d '{"title": "Test", "description": "Test"}'
```

---

*Последнее обновление: 2026-01-03*

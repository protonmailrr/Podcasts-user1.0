# 🎙️ FOMO Voice Club - API Documentation

Полное описание API эндпоинтов.

---

## 📌 Base URL

- **Development:** `http://localhost:8001/api`
- **Production:** `https://api.yourdomain.com/api`

---

## 🎤 Podcasts

### Получить список подкастов
```http
GET /api/podcasts
```

**Query Parameters:**
| Параметр | Тип | Описание |
|----------|------|----------|
| `limit` | int | Макс. кол-во (default: 50) |
| `skip` | int | Смещение (default: 0) |
| `author_id` | string | Фильтр по автору |
| `tag` | string | Фильтр по тегу |

**Response:**
```json
[
  {
    "id": "podcast-001",
    "title": "Welcome to FOMO",
    "description": "Introduction...",
    "author_id": "demo-owner-001",
    "category": "Introduction",
    "tags": ["welcome", "intro"],
    "duration": 1800,
    "views_count": 52,
    "likes": 45,
    "created_at": "2025-12-27T20:28:53.311Z"
  }
]
```

### Создать подкаст
```http
POST /api/podcasts
Content-Type: application/json
```

**Body:**
```json
{
  "title": "Название подкаста",
  "description": "Описание",
  "author_id": "user-123",
  "category": "DeFi",
  "tags": ["crypto", "defi"],
  "visibility": "public",
  "is_live": false
}
```

### Получить подкаст по ID
```http
GET /api/podcasts/{podcast_id}
```

### Сохранить/Убрать из сохранённых
```http
POST /api/podcasts/{podcast_id}/save
Content-Type: multipart/form-data

user_id=demo-user-123
```

**Response:**
```json
{"message": "Podcast saved", "saved": true}
```

### Добавить реакцию (Like)
```http
POST /api/podcasts/{podcast_id}/reactions
Content-Type: multipart/form-data

user_id=demo-user-123
reaction_type=heart
```

**Response:**
```json
{"message": "Reaction added", "added": true, "reaction_type": "heart"}
```

### Получить реакции
```http
GET /api/podcasts/{podcast_id}/reactions
```

**Response:**
```json
{
  "podcast_id": "podcast-001",
  "reactions": {
    "like": 45,
    "heart": 12,
    "fire": 8,
    "clap": 5
  }
}
```

---

## 📚 Library

### Получить сохранённые подкасты
```http
GET /api/library/saved/{user_id}
```

**Response:** Массив подкастов

### Получить понравившиеся подкасты
```http
GET /api/library/liked/{user_id}
```

**Response:** Массив подкастов с реакцией "heart"

---

## 💬 Comments

### Получить комментарии
```http
GET /api/podcasts/comments/{podcast_id}
```

**Response:**
```json
[
  {
    "id": "comment-001",
    "podcast_id": "podcast-001",
    "author_id": "user-123",
    "text": "Отличный подкаст!",
    "parent_id": null,
    "reactions": {"heart": 2, "fire": 1},
    "created_at": "2025-01-03T12:00:00Z",
    "replies": [...]
  }
]
```

### Добавить комментарий
```http
POST /api/podcasts/comments
Content-Type: application/json
```

**Body:**
```json
{
  "podcast_id": "podcast-001",
  "author_id": "user-123",
  "text": "Мой комментарий",
  "parent_id": null,
  "quote_text": null
}
```

### Добавить реакцию на комментарий
```http
PUT /api/podcasts/comments/{comment_id}/react
Content-Type: application/json
```

**Body:**
```json
{
  "user_id": "user-123",
  "reaction": "heart"
}
```

---

## 🏆 Gamification

### Прогресс пользователя
```http
GET /api/xp/{user_id}/progress
```

**Response:**
```json
{
  "user_id": "user-123",
  "xp": 1250,
  "level": 3,
  "level_name": "Contributor",
  "xp_to_next": 250,
  "progress_percent": 83,
  "priority_score": 75,
  "engagement_score": 82
}
```

### Бейджи пользователя
```http
GET /api/users/{user_id}/badges
```

**Response:**
```json
{
  "badges": [
    {
      "id": "first_listen",
      "name": "First Listen",
      "description": "Listened to first podcast",
      "icon": "Headphones",
      "category": "participation",
      "earned": true,
      "earned_at": "2025-01-01T12:00:00Z"
    }
  ]
}
```

### Лидерборд
```http
GET /api/xp/leaderboard?limit=10
```

**Response:**
```json
{
  "leaderboard": [
    {
      "user_id": "user-001",
      "name": "Club Owner",
      "xp_total": 15000,
      "level": 5,
      "rank": 1
    }
  ]
}
```

---

## 👥 Admin

### Получить настройки клуба
```http
GET /api/admin/settings
```

### Проверить роль пользователя
```http
GET /api/admin/check-role/{wallet_address}
```

**Response:**
```json
{
  "is_owner": false,
  "is_admin": true,
  "wallet": "0x123..."
}
```

### Добавить админа
```http
POST /api/admin/add-admin
Content-Type: application/json
```

**Body:**
```json
{
  "wallet_address": "0x123..."
}
```

*Примечание: при добавлении админа автоматически выдаются все 14 бейджей*

---

## 🔴 Live Sessions

### Получить активные сессии
```http
GET /api/live-sessions/sessions
```

### Создать сессию
```http
POST /api/live-sessions/sessions
Content-Type: application/json
```

**Body:**
```json
{
  "title": "Live Discussion",
  "podcast_id": "podcast-001",
  "host_id": "user-123"
}
```

---

## 🛠️ Коды ответов

| Код | Описание |
|------|----------|
| 200 | Успешный запрос |
| 201 | Ресурс создан |
| 400 | Неверный запрос |
| 401 | Не авторизован |
| 403 | Доступ запрещён |
| 404 | Ресурс не найден |
| 500 | Внутренняя ошибка сервера |

---

## 📖 Swagger документация

Интерактивная документация доступна по адресу:
- **Swagger UI:** `http://localhost:8001/docs`
- **ReDoc:** `http://localhost:8001/redoc`

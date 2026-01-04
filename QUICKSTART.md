# 🚀 FOMO Voice Club - Quick Start Guide

Полное руководство по быстрому запуску проекта.

---

## 📋 Требования

- **Node.js** 18+ ([download](https://nodejs.org/))
- **Python** 3.11+ ([download](https://python.org/))
- **MongoDB** 6.0+ ([download](https://mongodb.com/) или MongoDB Atlas)
- **Yarn** (не npm!): `npm install -g yarn`

---

## ⚡ Быстрый запуск (5 минут)

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-org/fomo-voice-club.git
cd fomo-voice-club
```

### 2. Настройка Backend

```bash
cd backend

# Установка зависимостей
pip install -r requirements.txt

# Создание .env файла
cp .env.example .env
```

Отредактируйте `.env`:
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=fomo_voice_club
JWT_SECRET_KEY=your-super-secret-key-change-this
```

### 3. Настройка Frontend

```bash
cd ../frontend

# Установка зависимостей (ВАЖНО: используйте yarn, не npm!)
yarn install

# Создание .env файла
cp .env.example .env
```

Отредактируйте `.env`:
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

### 4. Запуск сервисов

**Терминал 1 - Backend:**
```bash
cd backend
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

**Терминал 2 - Frontend:**
```bash
cd frontend
yarn start
```

### 5. Открытие в браузере

- **Приложение:** http://localhost:3000
- **API документация:** http://localhost:8001/docs

---

## 🧪 Тестовый режим

Для тестирования разных ролей откройте консоль браузера (F12) и выполните:

```javascript
// Войти как Owner (полный доступ)
localStorage.setItem('testMode', 'owner');
location.reload();

// Войти как Admin
localStorage.setItem('testMode', 'admin');
location.reload();

// Войти как обычный пользователь
localStorage.setItem('testMode', 'user');
location.reload();

// Выйти из тестового режима
localStorage.removeItem('testMode');
location.reload();
```

---

## 📁 Структура проекта

```
fomo-voice-club/
├── backend/
│   ├── routes/          # API endpoints
│   │   ├── podcasts.py  # Подкасты, реакции, сохранения
│   │   ├── comments.py  # Комментарии
│   │   ├── library.py   # Библиотека пользователя
│   │   ├── xp.py        # XP и уровни
│   │   ├── badges.py    # Бейджи
│   │   └── ...
│   ├── models.py        # Pydantic модели
│   ├── server.py        # Главный файл FastAPI
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/  # UI компоненты
│   │   ├── pages/       # Страницы
│   │   │   ├── Home.jsx
│   │   │   ├── PodcastDetail.jsx
│   │   │   ├── Library.jsx
│   │   │   ├── MyProgress.jsx
│   │   │   └── ...
│   │   └── context/     # React контексты
│   └── package.json
│
└── README.md
```

---

## 🔧 Конфигурация

### Backend `.env`

| Переменная | Описание | Обязательно |
|------------|----------|-------------|
| `MONGO_URL` | MongoDB URI | ✅ |
| `DB_NAME` | Имя базы данных | ✅ |
| `JWT_SECRET_KEY` | Секрет для JWT | ✅ |
| `TELEGRAM_BOT_TOKEN` | Токен Telegram бота | ❌ |
| `LIVEKIT_URL` | URL LiveKit сервера | ❌ |
| `LIVEKIT_API_KEY` | LiveKit API ключ | ❌ |
| `LIVEKIT_API_SECRET` | LiveKit секрет | ❌ |

### Frontend `.env`

| Переменная | Описание |
|------------|----------|
| `REACT_APP_BACKEND_URL` | URL бэкенда |

---

## 📱 Основные страницы

| URL | Страница | Описание |
|-----|----------|----------|
| `/` | Главная | Каталог подкастов с фильтрами |
| `/podcast/{id}` | Подкаст | Плеер, комментарии, аналитика |
| `/library` | Библиотека | Saved, Liked, Плейлисты |
| `/progress` | Прогресс | XP, уровень, бейджи |
| `/members` | Участники | Список членов клуба |
| `/create` | Создание | Загрузка или Live |
| `/admin` | Админка | Управление клубом |

---

## 🐛 Решение проблем

### Backend не запускается
```bash
# Проверьте Python версию
python --version  # должен быть 3.11+

# Переустановите зависимости
pip install -r requirements.txt --force-reinstall
```

### Frontend не запускается
```bash
# Удалите node_modules и переустановите
rm -rf node_modules yarn.lock
yarn install
```

### MongoDB ошибка подключения
```bash
# Проверьте, запущен ли MongoDB
mongod --version
sudo systemctl start mongod  # Linux
brew services start mongodb-community  # Mac
```

### CORS ошибки
Убедитесь, что `REACT_APP_BACKEND_URL` указывает на правильный адрес бэкенда.

---

## 🚀 Деплой на продакшн

### 1. Сборка Frontend
```bash
cd frontend
yarn build
```

### 2. Настройка Production Backend
```bash
# Используйте gunicorn с uvicorn workers
pip install gunicorn
gunicorn server:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8001
```

### 3. Настройка Nginx (пример)
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # Frontend
    location / {
        root /var/www/fomo-voice-club/frontend/build;
        try_files $uri $uri/ /index.html;
    }

    # Backend API
    location /api {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 📞 Поддержка

Если у вас возникли проблемы:
1. Проверьте раздел "Решение проблем" выше
2. Откройте Issue в GitHub репозитории
3. Приложите логи и описание проблемы

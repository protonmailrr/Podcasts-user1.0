# 🚀 FOMO Voice Club - Deployment Guide

Полное руководство по деплою проекта на продакшн.

---

## 📋 Предварительные требования

- VPS/Cloud сервер (Ubuntu 22.04 рекомендуется)
- Доменное имя
- SSL сертификат (Let's Encrypt)
- MongoDB Atlas или self-hosted MongoDB

---

## 🖥️ Подготовка сервера

### 1. Обновление системы
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Установка Node.js 18
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm install -g yarn
```

### 3. Установка Python 3.11
```bash
sudo apt install -y python3.11 python3.11-venv python3-pip
```

### 4. Установка Nginx
```bash
sudo apt install -y nginx
sudo systemctl enable nginx
```

---

## 📦 Деплой Backend

### 1. Клонирование и настройка
```bash
cd /var/www
git clone https://github.com/your-org/fomo-voice-club.git
cd fomo-voice-club/backend

# Виртуальное окружение
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

# Настройка .env
cp .env.example .env
nano .env  # Редактируйте с продакшн значениями
```

### 2. Systemd сервис
```bash
sudo nano /etc/systemd/system/fomo-backend.service
```

```ini
[Unit]
Description=FOMO Voice Club Backend
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/fomo-voice-club/backend
Environment="PATH=/var/www/fomo-voice-club/backend/venv/bin"
ExecStart=/var/www/fomo-voice-club/backend/venv/bin/gunicorn server:app -w 4 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8001
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable fomo-backend
sudo systemctl start fomo-backend
```

---

## 📦 Деплой Frontend

### 1. Сборка
```bash
cd /var/www/fomo-voice-club/frontend

# Настройка .env
cp .env.example .env
nano .env
# Установите: REACT_APP_BACKEND_URL=https://api.yourdomain.com

# Установка и сборка
yarn install
yarn build
```

### 2. Копирование build
```bash
sudo mkdir -p /var/www/html/fomo
sudo cp -r build/* /var/www/html/fomo/
sudo chown -R www-data:www-data /var/www/html/fomo
```

---

## 🌐 Настройка Nginx

### Конфигурация
```bash
sudo nano /etc/nginx/sites-available/fomo-voice-club
```

```nginx
# Frontend
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    root /var/www/html/fomo;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://127.0.0.1:8001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}

# API subdomain (optional)
server {
    listen 443 ssl http2;
    server_name api.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Активация
```bash
sudo ln -s /etc/nginx/sites-available/fomo-voice-club /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## 🔒 SSL сертификат (Let's Encrypt)

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com -d api.yourdomain.com
```

---

## 🗄️ MongoDB Atlas

1. Создайте кластер на [MongoDB Atlas](https://cloud.mongodb.com/)
2. Создайте пользователя базы данных
3. Добавьте IP вашего сервера в whitelist
4. Получите connection string и добавьте в `.env`:
```env
MONGO_URL=mongodb+srv://user:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

---

## 🔄 Обновление проекта

```bash
cd /var/www/fomo-voice-club
git pull origin main

# Backend
cd backend
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart fomo-backend

# Frontend
cd ../frontend
yarn install
yarn build
sudo cp -r build/* /var/www/html/fomo/
```

---

## 📊 Мониторинг

### Логи Backend
```bash
sudo journalctl -u fomo-backend -f
```

### Логи Nginx
```bash
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Статус сервисов
```bash
sudo systemctl status fomo-backend
sudo systemctl status nginx
```

---

## ✅ Чек-лист деплоя

- [ ] Сервер настроен и обновлён
- [ ] Node.js и Python установлены
- [ ] MongoDB подключена
- [ ] Backend запущен как systemd сервис
- [ ] Frontend собран и размещён
- [ ] Nginx настроен
- [ ] SSL сертификат установлен
- [ ] Домен направлен на сервер
- [ ] Все .env файлы настроены для продакшн
- [ ] Резервное копирование настроено

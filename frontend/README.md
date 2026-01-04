# FOMO Voice Club - Frontend

React-приложение для платформы FOMO Voice Club.

## 🛠️ Технологии

- **React 18** - UI фреймворк
- **Tailwind CSS** - стилизация
- **shadcn/ui** - UI компоненты
- **React Router** - маршрутизация
- **Axios** - HTTP запросы
- **Zustand** - управление состоянием

---

## 📁 Структура

```
src/
├── components/
│   ├── ui/                 # shadcn/ui компоненты
│   │   ├── button.jsx
│   │   ├── card.jsx
│   │   ├── input.jsx
│   │   ├── tabs.jsx
│   │   ├── select.jsx
│   │   ├── slider.jsx
│   │   ├── sheet.jsx
│   │   ├── tooltip.jsx
│   │   └── ...
│   ├── library/            # Компоненты библиотеки
│   │   ├── LibraryPodcastCard.jsx
│   │   ├── LibraryPlaylistCard.jsx
│   │   └── ...
│   ├── CommentsSection.jsx  # Система комментариев
│   ├── GlobalPlayer.jsx    # Глобальный аудио плеер
│   ├── Navigation.jsx      # Навигация
│   ├── PodcastCard.jsx     # Карточка подкаста
│   └── WalletSheet.jsx     # Панель кошелька
│
├── pages/
│   ├── Home.jsx            # Главная страница
│   ├── PodcastDetail.jsx   # Страница подкаста
│   ├── Library.jsx         # Личная библиотека
│   ├── MyProgress.jsx      # Прогресс пользователя
│   ├── CreatePodcast.jsx   # Создание подкаста
│   ├── Members.jsx         # Участники клуба
│   ├── Admin.jsx           # Админ-панель
│   └── ...
│
├── context/
│   ├── WalletContext.jsx   # Контекст кошелька
│   └── AuthContext.jsx     # Контекст аутентификации
│
├── utils/                  # Вспомогательные функции
├── App.js                  # Главный компонент
└── index.js                # Точка входа
```

---

## 🚀 Запуск

```bash
# Установка зависимостей
yarn install

# Разработка
yarn start

# Сборка
yarn build

# Тесты
yarn test
```

---

## 📄 Страницы

### Home.jsx
- Каталог подкастов с горизонтальной прокруткой
- Поиск, сортировка, фильтры
- Группировка по категориям
- Статистика клуба и топ участников

### PodcastDetail.jsx
- Аудио плеер с прогрессом
- Like/Save кнопки
- Блоки Description, Transcript, AI Summary
- Аналитика (plays, views, likes, comments)
- Комментарии с ответами и реакциями

### Library.jsx
- Три вкладки: Saved, Liked, Playlists
- Управление плейлистами
- Удаление из сохранённых

### MyProgress.jsx
- XP и уровень пользователя
- 14 бейджей (monochrome дизайн)
- Priority Score и Engagement Score
- Информативные тултипы

### CreatePodcast.jsx
- Выбор режима: Live или Upload
- Поля: Title, Description, Category, Tags
- Загрузка обложки и аудио
- Доступ только для Admin/Owner

---

## 🎨 Компоненты

### CommentsSection
- Вложенные ответы (threading)
- Реакции на комментарии
- Цитирование
- Emoji picker

### GlobalPlayer
- Персистентный плеер внизу страницы
- Play/Pause, Seek, Skip
- Информация о текущем подкасте

### Navigation
- Адаптивное меню
- Live вкладка только для Admin/Owner
- Подключение кошелька

---

## ⚙️ Конфигурация

### .env
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

### tailwind.config.js
Настройка цветов, шрифтов, анимаций.

---

## 🧪 Тестовый режим

```javascript
// В консоли браузера
localStorage.setItem('testMode', 'owner');  // owner, admin, user
location.reload();
```

---

## 📝 Лицензия

MIT License

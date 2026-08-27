"""
Переводы для Telegram бота — расширенная версия
"""

TRANSLATIONS = {
    "ru": {
        # Основные кнопки
        "start": "👋 Привет, {name}!\n\nЯ многофункциональный бот. Выбери раздел:\n\n💡 Нажми *📍 Мой город* чтобы настроить автооповещения о погоде!",
        "btn_weather":    "🌤 Погода",
        "btn_currency":   "💶 Курс валют",
        "btn_news":       "📰 Новости",
        "btn_help":       "ℹ️ Помощь",
        "btn_city":       "📍 Мой город",
        "btn_alerts":     "🔔 Оповещения",
        "btn_language":   "🌐 Язык",
        "btn_books":      "📚 Книги",
        "btn_stats":      "📊 Статистика",
        "btn_history":    "💬 История",

        "btn_spotify":    "🎵 Музыка",
        "btn_back":       "⬅️ Назад",

        # Погода
        "ask_city":       "🏙 Введите название города на английском:\n\nПримеры: Munich, Berlin, Moscow",
        "city_saved":     "✅ Город *{city}* сохранён!\nБуду проверять погоду каждый час.",
        "current_city":   "🏙 Ваш текущий город: *{city}*\n\nВведите новый город:",
        "alerts_on":      "Оповещения включены 🔔",
        "alerts_off":     "Оповещения выключены 🔕",
        "no_city":        "⚠️ Сначала задайте город через *📍 Мой город*",
        "city_not_found": "❌ Город '{city}' не найден.",
        "weather_title":  "🌤 *Погода в {city}, {country}*\n_{desc}_\n\n",
        "temp":           "🌡 Температура: *{temp}°C* (ощущается {feels}°C)\n",
        "feel":           "🤔 Ощущение: {feel}\n",
        "humidity":       "💧 Влажность: {val}%\n",
        "wind":           "💨 Ветер: {val} км/ч\n",
        "visibility":     "👁 Видимость: {val} км\n",
        "pressure":       "🔵 Давление: {val} мбар\n",
        "uv":             "☀️ УФ-индекс: {val}\n",
        "forecast":       "\n📅 *Прогноз на 3 дня:*\n",
        "today":          "Сегодня",
        "tomorrow":       "Завтра",
        "day_after":      "Послезавтра",
        "rain_chance":    "Дождь",
        "warnings":       "\n\n⚠️ *Предупреждения:*\n",
        "warn_wind":      "💨 Сильный ветер! Будьте осторожны.",
        "warn_storm":     "🌪 Штормовой ветер! Не выходите.",
        "warn_frost":     "🧊 Опасный мороз! Риск обморожения.",
        "warn_heat":      "🌡 Опасная жара! Пейте воду.",
        "warn_uv":        "☀️ Опасный УФ-индекс!",
        "warn_rain":      "🌧 {label}: дождь {val}% — возьмите зонт!",
        "warn_snow":      "❄️ {label}: снег {val}%!",
        "warn_thunder":   "⛈ {label}: гроза!",
        "feels_scale": {
            "extreme_cold": "🥶 Экстремальный холод",
            "very_cold":    "🧊 Очень холодно",
            "cold":         "❄️ Холодно",
            "cool":         "🧥 Прохладно",
            "fresh":        "🙂 Комфортно прохладно",
            "comfort":      "😊 Комфортно",
            "warm":         "😅 Тепло",
            "hot":          "🥵 Жарко",
            "extreme_heat": "🔥 Экстремальная жара",
        },

        # Новости и валюты
        "news_title":     "📰 *Последние новости DW:*\n\n",
        "news_error":     "❌ Новости не найдены.",
        "rates_title":    "💶 *Курс валют на {date}*\n\n",

        # Книги
        "books_menu":     "📚 *Раздел книг*\n\nВыберите действие:",
        "btn_search":     "🔍 Поиск по названию",
        "btn_top":        "⭐ Топ книги (4-5 звёзд)",
        "btn_wishlist":   "🛒 Список желаний",
        "btn_schedule":   "📅 Расписание проверки",
        "ask_search":     "🔍 Введите название книги:",
        "search_result":  "📚 *Результаты поиска:*\n\n",
        "not_found":      "❌ Книги не найдены.",
        "top_books":      "⭐ *Книги с рейтингом 4-5 звёзд:*\n\n",
        "wishlist_empty": "🛒 Список желаний пуст.\nДобавьте книги через поиск.",
        "wishlist_title": "🛒 *Ваш список желаний:*\n\n",
        "wish_added":     "✅ *{name}* добавлена в список желаний!",
        "wish_exists":    "⚠️ Эта книга уже в списке желаний.",
        "wish_removed":   "✅ Книга удалена из списка желаний.",
        "wish_btn_add":   "➕ Добавить в желания",
        "wish_btn_del":   "🗑 Удалить из желаний",
        "schedule_set":   "📅 Расписание: проверка цен каждый день в *{time}*\nКнига из желаний найдена — получите уведомление!",
        "ask_schedule":   "⏰ Введите время проверки (формат 09:00):",
        "schedule_ok":    "✅ Расписание установлено на *{time}*",

        # Статистика
        "stats_title":    "📊 *Ваша статистика:*\n\n",
        "stats_requests": "🔢 Всего запросов: *{val}*\n",
        "stats_weather":  "🌤 Запросов погоды: *{val}*\n",
        "stats_news":     "📰 Запросов новостей: *{val}*\n",
        "stats_books":    "📚 Запросов книг: *{val}*\n",
        "stats_currency": "💶 Запросов валют: *{val}*\n",
        "stats_since":    "📅 Используете бота с: *{val}*\n",

        # История
        "history_title":  "💬 *Последние 10 запросов:*\n\n",
        "history_empty":  "История запросов пуста.",

        # Email
        "ask_email":      "📧 Введите ваш email для отчёта:",
        "email_sent":     "✅ Отчёт отправлен на *{email}*!",
        "email_error":    "❌ Ошибка отправки. Проверьте email.",
        "email_saved":    "✅ Email *{email}* сохранён!",

        # Spotify
        "spotify_title":  "🎵 *Музыка по погоде в {city}:*\n\n",
        "spotify_sunny":  "☀️ Солнечно — заряжайтесь энергией!\n🎵 Жанр: Pop / Dance\n🔗 [Открыть плейлист](https://open.spotify.com/genre/pop)",
        "spotify_rainy":  "🌧 Дождь — время для уюта!\n🎵 Жанр: Acoustic / Indie\n🔗 [Открыть плейлист](https://open.spotify.com/genre/indie_alt)",
        "spotify_cold":   "❄️ Холодно — согрейтесь музыкой!\n🎵 Жанр: Classical / Jazz\n🔗 [Открыть плейлист](https://open.spotify.com/genre/classical)",
        "spotify_hot":    "🔥 Жарко — летнее настроение!\n🎵 Жанр: Reggae / Latin\n🔗 [Открыть плейлист](https://open.spotify.com/genre/latin)",
        "spotify_cloudy": "⛅ Облачно — спокойная музыка!\n🎵 Жанр: Lo-fi / Chill\n🔗 [Открыть плейлист](https://open.spotify.com/genre/chill)",
        "no_city_music":  "⚠️ Сначала задайте город через *📍 Мой город*",

        # Общее
        "unknown_cmd":    "🤔 Не понимаю. Используй кнопки меню.",
        "choose_lang":    "🌐 Выберите язык / Sprache wählen / Choose language:",
        "lang_saved":     "✅ Язык изменён!",
        "help_text": (
            "📋 *Команды бота:*\n\n"
            "🌤 *Погода* — прогноз + предупреждения\n"
            "💶 *Курс валют* — EUR курсы\n"
            "📰 *Новости* — последние новости DW\n"
            "📚 *Книги* — поиск, рейтинг, список желаний\n"
            "🎵 *Музыка* — плейлист по погоде\n"
            "📊 *Статистика* — ваша активность\n"
            "💬 *История* — последние запросы\n"
            "📧 *Email отчёт* — отправить сводку\n"
            "📍 *Мой город* — настроить оповещения\n"
            "🌐 *Язык* — сменить язык"
        ),
    },

    "de": {
        "start": "👋 Hallo, {name}!\n\nIch bin ein Mehrzweck-Bot. Wähle einen Bereich:\n\n💡 Drücke *📍 Meine Stadt* für automatische Wetterbenachrichtigungen!",
        "btn_weather":    "🌤 Wetter",
        "btn_currency":   "💶 Wechselkurse",
        "btn_news":       "📰 Nachrichten",
        "btn_help":       "ℹ️ Hilfe",
        "btn_city":       "📍 Meine Stadt",
        "btn_alerts":     "🔔 Benachrichtigungen",
        "btn_language":   "🌐 Sprache",
        "btn_books":      "📚 Bücher",
        "btn_stats":      "📊 Statistik",
        "btn_history":    "💬 Verlauf",

        "btn_spotify":    "🎵 Musik",
        "btn_back":       "⬅️ Zurück",
        "ask_city":       "🏙 Stadt eingeben:\n\nBeispiele: Munich, Berlin, Hamburg",
        "city_saved":     "✅ Stadt *{city}* gespeichert!",
        "current_city":   "🏙 Aktuelle Stadt: *{city}*\n\nNeue Stadt:",
        "alerts_on":      "Benachrichtigungen aktiviert 🔔",
        "alerts_off":     "Benachrichtigungen deaktiviert 🔕",
        "no_city":        "⚠️ Bitte Stadt über *📍 Meine Stadt* festlegen",
        "city_not_found": "❌ Stadt '{city}' nicht gefunden.",
        "weather_title":  "🌤 *Wetter in {city}, {country}*\n_{desc}_\n\n",
        "temp":           "🌡 Temperatur: *{temp}°C* (gefühlt {feels}°C)\n",
        "feel":           "🤔 Gefühl: {feel}\n",
        "humidity":       "💧 Luftfeuchtigkeit: {val}%\n",
        "wind":           "💨 Wind: {val} km/h\n",
        "visibility":     "👁 Sichtweite: {val} km\n",
        "pressure":       "🔵 Luftdruck: {val} mbar\n",
        "uv":             "☀️ UV-Index: {val}\n",
        "forecast":       "\n📅 *3-Tage-Vorhersage:*\n",
        "today":          "Heute",
        "tomorrow":       "Morgen",
        "day_after":      "Übermorgen",
        "rain_chance":    "Regen",
        "warnings":       "\n\n⚠️ *Warnungen:*\n",
        "warn_wind":      "💨 Starker Wind!",
        "warn_storm":     "🌪 Sturm! Bitte drinnen bleiben.",
        "warn_frost":     "🧊 Gefährlicher Frost!",
        "warn_heat":      "🌡 Gefährliche Hitze!",
        "warn_uv":        "☀️ Gefährlicher UV-Index!",
        "warn_rain":      "🌧 {label}: Regen {val}%!",
        "warn_snow":      "❄️ {label}: Schnee {val}%!",
        "warn_thunder":   "⛈ {label}: Gewitter!",
        "feels_scale": {
            "extreme_cold": "🥶 Extremkälte",
            "very_cold":    "🧊 Sehr kalt",
            "cold":         "❄️ Kalt",
            "cool":         "🧥 Kühl",
            "fresh":        "🙂 Angenehm kühl",
            "comfort":      "😊 Angenehm",
            "warm":         "😅 Warm",
            "hot":          "🥵 Heiß",
            "extreme_heat": "🔥 Extreme Hitze",
        },
        "news_title":     "📰 *Aktuelle Nachrichten:*\n\n",
        "news_error":     "❌ Keine Nachrichten.",
        "rates_title":    "💶 *Wechselkurse vom {date}*\n\n",
        "books_menu":     "📚 Bücher\n\nAktion wählen:",
        "btn_search":     "🔍 Nach Titel suchen",
        "btn_top":        "⭐ Top Bücher (4-5 Sterne)",
        "btn_wishlist":   "🛒 Wunschliste",
        "btn_schedule":   "📅 Preischeck-Zeitplan",
        "ask_search":     "🔍 Buchtitel eingeben:",
        "search_result":  "📚 *Suchergebnisse:*\n\n",
        "not_found":      "❌ Keine Bücher gefunden.",
        "top_books":      "⭐ *Bücher mit 4-5 Sternen:*\n\n",
        "wishlist_empty": "🛒 Wunschliste ist leer.",
        "wishlist_title": "🛒 *Ihre Wunschliste:*\n\n",
        "wish_added":     "✅ *{name}* zur Wunschliste hinzugefügt!",
        "wish_exists":    "⚠️ Bereits in der Wunschliste.",
        "wish_removed":   "✅ Buch entfernt.",
        "wish_btn_add":   "➕ Zur Wunschliste",
        "wish_btn_del":   "🗑 Entfernen",
        "schedule_set":   "📅 Zeitplan: täglich um *{time}*",
        "ask_schedule":   "⏰ Uhrzeit eingeben (Format 09:00):",
        "schedule_ok":    "✅ Zeitplan auf *{time}* gesetzt",
        "stats_title":    "📊 *Ihre Statistik:*\n\n",
        "stats_requests": "🔢 Anfragen gesamt: *{val}*\n",
        "stats_weather":  "🌤 Wetteranfragen: *{val}*\n",
        "stats_news":     "📰 Nachrichtenanfragen: *{val}*\n",
        "stats_books":    "📚 Buchanfragen: *{val}*\n",
        "stats_currency": "💶 Währungsanfragen: *{val}*\n",
        "stats_since":    "📅 Nutzer seit: *{val}*\n",
        "history_title":  "💬 *Letzte 10 Anfragen:*\n\n",
        "history_empty":  "Verlauf ist leer.",

        "spotify_title":  "🎵 *Musik für das Wetter in {city}:*\n\n",
        "spotify_sunny":  "☀️ Sonnig!\n🎵 Genre: Pop / Dance\n🔗 [Playlist öffnen](https://open.spotify.com/genre/pop)",
        "spotify_rainy":  "🌧 Regnerisch!\n🎵 Genre: Acoustic / Indie\n🔗 [Playlist öffnen](https://open.spotify.com/genre/indie_alt)",
        "spotify_cold":   "❄️ Kalt!\n🎵 Genre: Classical / Jazz\n🔗 [Playlist öffnen](https://open.spotify.com/genre/classical)",
        "spotify_hot":    "🔥 Heiß!\n🎵 Genre: Reggae / Latin\n🔗 [Playlist öffnen](https://open.spotify.com/genre/latin)",
        "spotify_cloudy": "⛅ Bewölkt!\n🎵 Genre: Lo-fi / Chill\n🔗 [Playlist öffnen](https://open.spotify.com/genre/chill)",
        "no_city_music":  "⚠️ Bitte Stadt festlegen.",
        "unknown_cmd":    "🤔 Unbekannter Befehl.",
        "choose_lang":    "🌐 Выберите язык / Sprache wählen / Choose language:",
        "lang_saved":     "✅ Sprache geändert!",
        "help_text": (
            "📋 *Bot-Befehle:*\n\n"
            "🌤 *Wetter* — Vorhersage + Warnungen\n"
            "💶 *Kurse* — EUR Wechselkurse\n"
            "📰 *Nachrichten* — Aktuelle News\n"
            "📚 *Bücher* — Suche, Bewertung, Wunschliste\n"
            "🎵 *Musik* — Playlist nach Wetter\n"
            "📊 *Statistik* — Ihre Aktivität\n"
            "💬 *Verlauf* — Letzte Anfragen\n"
            "📧 *E-Mail* — Bericht senden\n"
            "📍 *Stadt* — Benachrichtigungen\n"
            "🌐 *Sprache* — Sprache ändern"
        ),
    },

    "en": {
        "start": "👋 Hello, {name}!\n\nI'm a multifunctional bot. Choose a section:\n\n💡 Press *📍 My City* to set up automatic weather alerts!",
        "btn_weather":    "🌤 Weather",
        "btn_currency":   "💶 Exchange Rates",
        "btn_news":       "📰 News",
        "btn_help":       "ℹ️ Help",
        "btn_city":       "📍 My City",
        "btn_alerts":     "🔔 Alerts",
        "btn_language":   "🌐 Language",
        "btn_books":      "📚 Books",
        "btn_stats":      "📊 Statistics",
        "btn_history":    "💬 History",

        "btn_spotify":    "🎵 Music",
        "btn_back":       "⬅️ Back",
        "ask_city":       "🏙 Enter city name:\n\nExamples: Munich, Berlin, London",
        "city_saved":     "✅ City *{city}* saved!",
        "current_city":   "🏙 Current city: *{city}*\n\nEnter new city:",
        "alerts_on":      "Alerts enabled 🔔",
        "alerts_off":     "Alerts disabled 🔕",
        "no_city":        "⚠️ Please set city via *📍 My City* first",
        "city_not_found": "❌ City '{city}' not found.",
        "weather_title":  "🌤 *Weather in {city}, {country}*\n_{desc}_\n\n",
        "temp":           "🌡 Temperature: *{temp}°C* (feels like {feels}°C)\n",
        "feel":           "🤔 Feels: {feel}\n",
        "humidity":       "💧 Humidity: {val}%\n",
        "wind":           "💨 Wind: {val} km/h\n",
        "visibility":     "👁 Visibility: {val} km\n",
        "pressure":       "🔵 Pressure: {val} mbar\n",
        "uv":             "☀️ UV Index: {val}\n",
        "forecast":       "\n📅 *3-Day Forecast:*\n",
        "today":          "Today",
        "tomorrow":       "Tomorrow",
        "day_after":      "Day after tomorrow",
        "rain_chance":    "Rain",
        "warnings":       "\n\n⚠️ *Warnings:*\n",
        "warn_wind":      "💨 Strong wind!",
        "warn_storm":     "🌪 Storm! Stay indoors.",
        "warn_frost":     "🧊 Dangerous frost!",
        "warn_heat":      "🌡 Dangerous heat!",
        "warn_uv":        "☀️ Dangerous UV index!",
        "warn_rain":      "🌧 {label}: rain {val}%!",
        "warn_snow":      "❄️ {label}: snow {val}%!",
        "warn_thunder":   "⛈ {label}: thunderstorm!",
        "feels_scale": {
            "extreme_cold": "🥶 Extreme cold",
            "very_cold":    "🧊 Very cold",
            "cold":         "❄️ Cold",
            "cool":         "🧥 Cool",
            "fresh":        "🙂 Comfortably cool",
            "comfort":      "😊 Comfortable",
            "warm":         "😅 Warm",
            "hot":          "🥵 Hot",
            "extreme_heat": "🔥 Extreme heat",
        },
        "news_title":     "📰 *Latest DW News:*\n\n",
        "news_error":     "❌ No news found.",
        "rates_title":    "💶 *Exchange rates on {date}*\n\n",
        "books_menu":     "📚 Books\n\nChoose action:",
        "btn_search":     "🔍 Search by title",
        "btn_top":        "⭐ Top Books (4-5 stars)",
        "btn_wishlist":   "🛒 Wishlist",
        "btn_schedule":   "📅 Price Check Schedule",
        "ask_search":     "🔍 Enter book title:",
        "search_result":  "📚 *Search results:*\n\n",
        "not_found":      "❌ No books found.",
        "top_books":      "⭐ *Books with 4-5 stars:*\n\n",
        "wishlist_empty": "🛒 Wishlist is empty.",
        "wishlist_title": "🛒 *Your wishlist:*\n\n",
        "wish_added":     "✅ *{name}* added to wishlist!",
        "wish_exists":    "⚠️ Already in wishlist.",
        "wish_removed":   "✅ Book removed from wishlist.",
        "wish_btn_add":   "➕ Add to wishlist",
        "wish_btn_del":   "🗑 Remove",
        "schedule_set":   "📅 Schedule: daily at *{time}*",
        "ask_schedule":   "⏰ Enter check time (format 09:00):",
        "schedule_ok":    "✅ Schedule set to *{time}*",
        "stats_title":    "📊 *Your Statistics:*\n\n",
        "stats_requests": "🔢 Total requests: *{val}*\n",
        "stats_weather":  "🌤 Weather requests: *{val}*\n",
        "stats_news":     "📰 News requests: *{val}*\n",
        "stats_books":    "📚 Books requests: *{val}*\n",
        "stats_currency": "💶 Currency requests: *{val}*\n",
        "stats_since":    "📅 Using bot since: *{val}*\n",
        "history_title":  "💬 *Last 10 requests:*\n\n",
        "history_empty":  "Request history is empty.",

        "spotify_title":  "🎵 *Music for weather in {city}:*\n\n",
        "spotify_sunny":  "☀️ Sunny — get energized!\n🎵 Genre: Pop / Dance\n🔗 [Open playlist](https://open.spotify.com/genre/pop)",
        "spotify_rainy":  "🌧 Rainy — cozy vibes!\n🎵 Genre: Acoustic / Indie\n🔗 [Open playlist](https://open.spotify.com/genre/indie_alt)",
        "spotify_cold":   "❄️ Cold — warm up with music!\n🎵 Genre: Classical / Jazz\n🔗 [Open playlist](https://open.spotify.com/genre/classical)",
        "spotify_hot":    "🔥 Hot — summer mood!\n🎵 Genre: Reggae / Latin\n🔗 [Open playlist](https://open.spotify.com/genre/latin)",
        "spotify_cloudy": "⛅ Cloudy — chill out!\n🎵 Genre: Lo-fi / Chill\n🔗 [Open playlist](https://open.spotify.com/genre/chill)",
        "no_city_music":  "⚠️ Please set your city first.",
        "unknown_cmd":    "🤔 Unknown command. Please use menu.",
        "choose_lang":    "🌐 Выберите язык / Sprache wählen / Choose language:",
        "lang_saved":     "✅ Language changed!",
        "help_text": (
            "📋 *Bot commands:*\n\n"
            "🌤 *Weather* — forecast + warnings\n"
            "💶 *Rates* — EUR exchange rates\n"
            "📰 *News* — latest news\n"
            "📚 *Books* — search, rating, wishlist\n"
            "🎵 *Music* — playlist by weather\n"
            "📊 *Statistics* — your activity\n"
            "💬 *History* — recent requests\n"
            "📧 *Email* — send report\n"
            "📍 *My City* — set up alerts\n"
            "🌐 *Language* — change language"
        ),
    },
}


def t(lang: str, key: str) -> str:
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)
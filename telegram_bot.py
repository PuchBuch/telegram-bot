"""
Многофункциональный Telegram бот — полная версия
=================================================
Установка:
    pip install pyTelegramBotAPI requests beautifulsoup4 lxml python-dotenv schedule

Запуск:
    python telegram_bot.py
"""

import telebot, requests, datetime, os, json, threading, schedule, time, re
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from translations import TRANSLATIONS, t

load_dotenv()

# ─── НАСТРОЙКИ ────────────────────────────────────────────────
TELEGRAM_TOKEN  = os.getenv("TELEGRAM_TOKEN")
USERS_FILE      = "users.json"
CHECK_INTERVAL  = 60
BASE_URL        = "https://books.toscrape.com/catalogue/"
RATING_MAP      = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
# ──────────────────────────────────────────────────────────────

bot     = telebot.TeleBot(TELEGRAM_TOKEN)
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


def md(text: str) -> str:
    """Markdown → HTML."""
    text = re.sub(r'\*(.+?)\*', r'<b>\1</b>', text)
    text = re.sub(r'_(.+?)_',   r'<i>\1</i>', text)
    text = re.sub(r'`(.+?)`',   r'<code>\1</code>', text)
    return text


def send(chat_id, text: str, **kwargs):
    """Отправляет сообщение — автоконвертация Markdown в HTML."""
    kwargs.setdefault("parse_mode", "HTML")
    kwargs.pop("parse_mode", None)
    try:
        bot.send_message(chat_id, md(text), parse_mode="HTML", **kwargs)
    except Exception:
        clean = re.sub(r'[*_`]', '', text)
        bot.send_message(chat_id, clean, **kwargs)


# ─── ПОЛЬЗОВАТЕЛИ ─────────────────────────────────────────────

def load_users() -> dict:
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_users(users: dict) -> None:
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)


def get_user(chat_id) -> dict:
    users = load_users()
    uid   = str(chat_id)
    if uid not in users:
        users[uid] = {
            "lang": "ru", "city": None, "alerts": True,
            "wishlist": [], "schedule_time": None,
            "stats": {"total": 0, "weather": 0, "news": 0, "books": 0, "currency": 0},
            "history": [], "since": datetime.datetime.now().strftime("%Y-%m-%d"),
        }
        save_users(users)
    return users[uid]


def set_user(chat_id, **kwargs) -> None:
    users = load_users()
    uid   = str(chat_id)
    if uid not in users:
        get_user(chat_id)
        users = load_users()
    users[uid].update(kwargs)
    save_users(users)


def add_stat(chat_id, key: str) -> None:
    users = load_users()
    uid   = str(chat_id)
    if uid not in users:
        get_user(chat_id)
        users = load_users()
    users[uid].setdefault("stats", {})
    users[uid]["stats"]["total"] = users[uid]["stats"].get("total", 0) + 1
    users[uid]["stats"][key]     = users[uid]["stats"].get(key, 0) + 1
    save_users(users)


def add_history(chat_id, entry: str) -> None:
    users = load_users()
    uid   = str(chat_id)
    if uid not in users:
        get_user(chat_id)
        users = load_users()
    hist = users[uid].get("history", [])
    hist.append(f"{datetime.datetime.now().strftime('%d.%m %H:%M')} — {entry}")
    users[uid]["history"] = hist[-10:]
    save_users(users)


def lang(chat_id) -> str:
    return get_user(str(chat_id)).get("lang", "ru")


# ─── КЛАВИАТУРЫ ───────────────────────────────────────────────

def is_btn(m, key):
    return m.text in [t("ru", key), t("de", key), t("en", key)]


def main_keyboard(chat_id):
    L = lang(chat_id)
    m = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    m.row(t(L, "btn_weather"),  t(L, "btn_currency"))
    m.row(t(L, "btn_news"),     t(L, "btn_books"))
    m.row(t(L, "btn_spotify"),  t(L, "btn_stats"))
    m.row(t(L, "btn_history"),  t(L, "btn_city"))
    m.row(t(L, "btn_alerts"),   t(L, "btn_language"))
    m.row(t(L, "btn_help"))
    return m


def books_keyboard(chat_id):
    L = lang(chat_id)
    m = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    m.row(t(L, "btn_search"),   t(L, "btn_top"))
    m.row(t(L, "btn_wishlist"), t(L, "btn_schedule"))
    m.row(t(L, "btn_back"))
    return m


# ─── СТАРТ ────────────────────────────────────────────────────

@bot.message_handler(commands=["start"])
def cmd_start(msg):
    get_user(msg.chat.id)
    L    = lang(msg.chat.id)
    name = msg.from_user.first_name
    send(msg.chat.id, t(L, "start").format(name=name),
         reply_markup=main_keyboard(msg.chat.id))


# ─── ЯЗЫК ─────────────────────────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_language"))
def choose_language(msg):
    mk = telebot.types.InlineKeyboardMarkup()
    mk.row(
        telebot.types.InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
        telebot.types.InlineKeyboardButton("🇩🇪 Deutsch", callback_data="lang_de"),
        telebot.types.InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
    )
    bot.send_message(msg.chat.id, t(lang(msg.chat.id), "choose_lang"), reply_markup=mk)


@bot.callback_query_handler(func=lambda c: c.data.startswith("lang_"))
def set_language(call):
    new_lang = call.data.split("_")[1]
    set_user(call.message.chat.id, lang=new_lang)
    bot.answer_callback_query(call.id)
    send(call.message.chat.id, t(new_lang, "lang_saved"),
         reply_markup=main_keyboard(call.message.chat.id))


# ─── ПОГОДА ───────────────────────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_weather"))
def ask_city(msg):
    add_stat(msg.chat.id, "weather")
    L    = lang(msg.chat.id)
    sent = bot.send_message(msg.chat.id, t(L, "ask_city"))
    bot.register_next_step_handler(sent, get_weather)


def feels_label(lang_code, feels):
    s = TRANSLATIONS[lang_code]["feels_scale"]
    if feels <= -20:   return s["extreme_cold"]
    elif feels <= -10: return s["very_cold"]
    elif feels <= 0:   return s["cold"]
    elif feels <= 10:  return s["cool"]
    elif feels <= 18:  return s["fresh"]
    elif feels <= 24:  return s["comfort"]
    elif feels <= 30:  return s["warm"]
    elif feels <= 37:  return s["hot"]
    else:              return s["extreme_heat"]


def get_weather(msg):
    city = msg.text.strip()
    L    = lang(msg.chat.id)
    add_history(msg.chat.id, f"погода: {city}")
    try:
        resp = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
        if resp.status_code != 200:
            send(msg.chat.id, t(L, "city_not_found").format(city=city))
            return
        data    = resp.json()
        current = data["current_condition"][0]
        area    = data["nearest_area"][0]
        weather = data["weather"]
        city_name = area["areaName"][0]["value"]
        country   = area["country"][0]["value"]
        temp      = current["temp_C"]
        feels     = int(current["FeelsLikeC"])
        humidity  = current["humidity"]
        wind      = current["windspeedKmph"]
        vis       = current["visibility"]
        pressure  = current["pressure"]
        uv        = current["uvIndex"]
        desc      = current["weatherDesc"][0]["value"]
        code      = int(current["weatherCode"])

        if code == 113:                          icon = "☀️"
        elif code in [116, 119]:                 icon = "⛅"
        elif code in [122, 143]:                 icon = "☁️"
        elif code in [176, 263, 266, 293, 296]:  icon = "🌦"
        elif code in [299, 302, 305, 308]:       icon = "🌧"
        elif code in [200, 386, 389]:            icon = "⛈"
        elif code in [320, 323, 326, 329, 332]:  icon = "🌨"
        else:                                    icon = "🌡"

        text  = t(L, "weather_title").format(city=city_name, country=country, desc=f"{icon} {desc}")
        text += t(L, "temp").format(temp=temp, feels=feels)
        text += t(L, "feel").format(feel=feels_label(L, feels))
        text += t(L, "humidity").format(val=humidity)
        text += t(L, "wind").format(val=wind)
        text += t(L, "visibility").format(val=vis)
        text += t(L, "pressure").format(val=pressure)
        text += t(L, "uv").format(val=uv)
        text += t(L, "forecast")

        labels = [t(L, "today"), t(L, "tomorrow"), t(L, "day_after")]
        for i, day in enumerate(weather[:3]):
            rain    = day["hourly"][4].get("chanceofrain", "0")
            sunrise = day["astronomy"][0]["sunrise"]
            sunset  = day["astronomy"][0]["sunset"]
            text += (
                f"\n<b>{labels[i]}</b> ({day['date']})\n"
                f"  🌡 {day['mintempC']}°C — {day['maxtempC']}°C\n"
                f"  ☁️ {day['hourly'][4]['weatherDesc'][0]['value']}\n"
                f"  🌧 {t(L,'rain_chance')}: {rain}%\n"
                f"  🌅 {sunrise} / 🌇 {sunset}\n"
            )

        warnings = []
        if int(wind) >= 50:   warnings.append(t(L, "warn_wind"))
        if int(wind) >= 80:   warnings.append(t(L, "warn_storm"))
        if feels <= -15:      warnings.append(t(L, "warn_frost"))
        if feels >= 35:       warnings.append(t(L, "warn_heat"))
        if int(uv) >= 8:      warnings.append(t(L, "warn_uv"))
        for i, day in enumerate(weather[:2]):
            rain_p = int(day["hourly"][4].get("chanceofrain", 0))
            snow_p = int(day["hourly"][4].get("chanceofsnow", 0))
            w_code = int(day["hourly"][4]["weatherCode"])
            lbl    = labels[i]
            if rain_p >= 70: warnings.append(t(L, "warn_rain").format(label=lbl, val=rain_p))
            if snow_p >= 70: warnings.append(t(L, "warn_snow").format(label=lbl, val=snow_p))
            if w_code in [386, 389]: warnings.append(t(L, "warn_thunder").format(label=lbl))
        if warnings:
            text += t(L, "warnings") + "\n".join(f"• {w}" for w in warnings)

        bot.send_message(msg.chat.id, md(text), parse_mode="HTML",
                         reply_markup=main_keyboard(msg.chat.id))
    except Exception as e:
        bot.send_message(msg.chat.id, f"❌ {e}")


# ─── МОЙ ГОРОД / ОПОВЕЩЕНИЯ ───────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_city"))
def ask_my_city(msg):
    L    = lang(msg.chat.id)
    user = get_user(str(msg.chat.id))
    city = user.get("city") or "—"
    sent = bot.send_message(msg.chat.id, t(L, "current_city").format(city=city))
    bot.register_next_step_handler(sent, save_my_city)


def save_my_city(msg):
    L = lang(msg.chat.id)
    set_user(str(msg.chat.id), city=msg.text.strip())
    send(msg.chat.id, t(L, "city_saved").format(city=msg.text.strip()),
         reply_markup=main_keyboard(msg.chat.id))


@bot.message_handler(func=lambda m: is_btn(m, "btn_alerts"))
def toggle_alerts(msg):
    L    = lang(msg.chat.id)
    user = get_user(str(msg.chat.id))
    if not user.get("city"):
        send(msg.chat.id, t(L, "no_city"))
        return
    new_val = not user.get("alerts", True)
    set_user(str(msg.chat.id), alerts=new_val)
    status = t(L, "alerts_on") if new_val else t(L, "alerts_off")
    bot.send_message(msg.chat.id, status, reply_markup=main_keyboard(msg.chat.id))


# ─── КУРС ВАЛЮТ ───────────────────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_currency"))
def get_rates(msg):
    L = lang(msg.chat.id)
    add_stat(msg.chat.id, "currency")
    add_history(msg.chat.id, "курс валют")
    try:
        resp  = requests.get("https://api.exchangerate-api.com/v4/latest/EUR", timeout=10)
        data  = resp.json()
        rates = data["rates"]
        text  = t(L, "rates_title").format(date=data["date"])
        text += (
            f"🇺🇸 EUR → USD: <code>{rates.get('USD',0):.4f}</code>\n"
            f"🇬🇧 EUR → GBP: <code>{rates.get('GBP',0):.4f}</code>\n"
            f"🇨🇭 EUR → CHF: <code>{rates.get('CHF',0):.4f}</code>\n"
            f"🇷🇺 EUR → RUB: <code>{rates.get('RUB',0):.4f}</code>\n"
            f"🇵🇱 EUR → PLN: <code>{rates.get('PLN',0):.4f}</code>\n"
            f"🇨🇿 EUR → CZK: <code>{rates.get('CZK',0):.4f}</code>\n"
        )
        bot.send_message(msg.chat.id, md(text), parse_mode="HTML",
                         reply_markup=main_keyboard(msg.chat.id))
    except Exception as e:
        bot.send_message(msg.chat.id, f"❌ {e}")


# ─── НОВОСТИ ──────────────────────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_news"))
def get_news(msg):
    L = lang(msg.chat.id)
    add_stat(msg.chat.id, "news")
    add_history(msg.chat.id, "новости")
    try:
        rss  = {"ru": "https://rss.dw.com/rdf/rss-ru-all",
                "de": "https://rss.dw.com/rdf/rss-de-all",
                "en": "https://rss.dw.com/rdf/rss-en-all"}.get(L)
        resp  = requests.get(rss, timeout=10)
        soup  = BeautifulSoup(resp.content, "xml")
        items = soup.find_all("item")[:5]
        if not items:
            bot.send_message(msg.chat.id, t(L, "news_error"))
            return
        text = t(L, "news_title")
        for i, item in enumerate(items, 1):
            title = item.find("title").get_text(strip=True)
            link  = item.find("link").get_text(strip=True)
            text += f'{i}. <a href="{link}">{title}</a>\n\n'
        bot.send_message(msg.chat.id, md(text), parse_mode="HTML",
                         disable_web_page_preview=True,
                         reply_markup=main_keyboard(msg.chat.id))
    except Exception as e:
        bot.send_message(msg.chat.id, f"❌ {e}")


# ─── КНИГИ ────────────────────────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_books"))
def books_menu(msg):
    L = lang(msg.chat.id)
    add_stat(msg.chat.id, "books")
    bot.send_message(msg.chat.id, t(L, "books_menu"), reply_markup=books_keyboard(msg.chat.id))


@bot.message_handler(func=lambda m: is_btn(m, "btn_back"))
def go_back(msg):
    bot.send_message(msg.chat.id, "✅", reply_markup=main_keyboard(msg.chat.id))


def fetch_books(min_rating=0, max_pages=3) -> list[dict]:
    books = []
    for page in range(1, max_pages + 1):
        try:
            resp = requests.get(f"{BASE_URL}page-{page}.html", headers=HEADERS, timeout=10)
            resp.encoding = "utf-8"
            soup = BeautifulSoup(resp.text, "html.parser")
            for item in soup.select("article.product_pod"):
                name_tag   = item.select_one("h3 a")
                price_tag  = item.select_one("p.price_color")
                rating_tag = item.select_one("p.star-rating")
                name   = name_tag["title"] if name_tag else "—"
                price  = price_tag.get_text(strip=True) if price_tag else "?"
                rating = RATING_MAP.get(rating_tag["class"][1] if rating_tag else "Zero", 0)
                if rating >= min_rating:
                    books.append({"name": name, "price": price, "rating": rating})
        except Exception:
            pass
    return books


@bot.message_handler(func=lambda m: is_btn(m, "btn_search"))
def ask_search(msg):
    L    = lang(msg.chat.id)
    sent = bot.send_message(msg.chat.id, t(L, "ask_search"))
    bot.register_next_step_handler(sent, do_search)


def do_search(msg):
    L       = lang(msg.chat.id)
    query   = msg.text.strip().lower()
    add_history(msg.chat.id, f"поиск: {query}")
    books   = fetch_books()
    results = [b for b in books if query in b["name"].lower()]
    if not results:
        bot.send_message(msg.chat.id, t(L, "not_found"), reply_markup=books_keyboard(msg.chat.id))
        return
    text = t(L, "search_result")
    for b in results[:10]:
        text += f"{'⭐' * b['rating']} {b['name']} — {b['price']}\n"
    bot.send_message(msg.chat.id, md(text), parse_mode="HTML",
                     reply_markup=books_keyboard(msg.chat.id))


@bot.message_handler(func=lambda m: is_btn(m, "btn_top"))
def top_books(msg):
    L     = lang(msg.chat.id)
    add_history(msg.chat.id, "топ книги")
    books = fetch_books(min_rating=4)
    if not books:
        bot.send_message(msg.chat.id, t(L, "not_found"))
        return
    text = t(L, "top_books")
    for b in books[:15]:
        text += f"{'⭐' * b['rating']} {b['name']} — {b['price']}\n"
    bot.send_message(msg.chat.id, md(text), parse_mode="HTML",
                     reply_markup=books_keyboard(msg.chat.id))


@bot.message_handler(func=lambda m: is_btn(m, "btn_wishlist"))
def show_wishlist(msg):
    L    = lang(msg.chat.id)
    user = get_user(str(msg.chat.id))
    wl   = user.get("wishlist", [])
    if not wl:
        bot.send_message(msg.chat.id, t(L, "wishlist_empty"),
                         reply_markup=books_keyboard(msg.chat.id))
        return
    books = fetch_books()
    text  = t(L, "wishlist_title")
    for name in wl:
        found = next((b for b in books if name.lower() in b["name"].lower()), None)
        price = f"— {found['price']}" if found else "— ?"
        text += f"🛒 {name} {price}\n"
    mk = telebot.types.InlineKeyboardMarkup()
    mk.add(telebot.types.InlineKeyboardButton(t(L, "wish_btn_add"), callback_data="wish_add"))
    bot.send_message(msg.chat.id, md(text), parse_mode="HTML", reply_markup=mk)


@bot.callback_query_handler(func=lambda c: c.data == "wish_add")
def wish_add_prompt(call):
    L    = lang(call.message.chat.id)
    sent = bot.send_message(call.message.chat.id, t(L, "ask_search"))
    bot.register_next_step_handler(sent, wish_add_book)
    bot.answer_callback_query(call.id)


def wish_add_book(msg):
    L    = lang(msg.chat.id)
    name = msg.text.strip()
    user = get_user(str(msg.chat.id))
    wl   = user.get("wishlist", [])
    if name in wl:
        bot.send_message(msg.chat.id, t(L, "wish_exists"), reply_markup=books_keyboard(msg.chat.id))
        return
    wl.append(name)
    set_user(str(msg.chat.id), wishlist=wl)
    send(msg.chat.id, t(L, "wish_added").format(name=name), reply_markup=books_keyboard(msg.chat.id))


@bot.message_handler(func=lambda m: is_btn(m, "btn_schedule"))
def ask_schedule(msg):
    L    = lang(msg.chat.id)
    sent = bot.send_message(msg.chat.id, t(L, "ask_schedule"))
    bot.register_next_step_handler(sent, set_schedule)


def set_schedule(msg):
    L        = lang(msg.chat.id)
    time_str = msg.text.strip()
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        set_user(str(msg.chat.id), schedule_time=time_str)
        send(msg.chat.id, t(L, "schedule_ok").format(time=time_str),
             reply_markup=books_keyboard(msg.chat.id))
    except ValueError:
        bot.send_message(msg.chat.id, "❌ Формат: 09:00", reply_markup=books_keyboard(msg.chat.id))


# ─── МУЗЫКА ───────────────────────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_spotify"))
def get_music(msg):
    L    = lang(msg.chat.id)
    user = get_user(str(msg.chat.id))
    city = user.get("city")
    add_history(msg.chat.id, "музыка")
    if not city:
        send(msg.chat.id, t(L, "no_city_music"))
        return
    try:
        resp    = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
        data    = resp.json()
        current = data["current_condition"][0]
        temp    = int(current["temp_C"])
        code    = int(current["weatherCode"])

        if code in [200, 386, 389, 299, 302, 305, 308, 176]: mood = "rainy"
        elif code in [320, 323, 326, 329, 332]:               mood = "cold"
        elif code == 113 and temp >= 25:                       mood = "hot"
        elif code == 113:                                      mood = "sunny"
        else:                                                  mood = "cloudy"

        text = t(L, "spotify_title").format(city=city) + t(L, f"spotify_{mood}")
        bot.send_message(msg.chat.id, md(text), parse_mode="HTML",
                         reply_markup=main_keyboard(msg.chat.id))
    except Exception as e:
        bot.send_message(msg.chat.id, f"❌ {e}")


# ─── СТАТИСТИКА ───────────────────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_stats"))
def show_stats(msg):
    L    = lang(msg.chat.id)
    user = get_user(str(msg.chat.id))
    s    = user.get("stats", {})
    text = t(L, "stats_title")
    text += t(L, "stats_requests").format(val=s.get("total", 0))
    text += t(L, "stats_weather").format(val=s.get("weather", 0))
    text += t(L, "stats_news").format(val=s.get("news", 0))
    text += t(L, "stats_books").format(val=s.get("books", 0))
    text += t(L, "stats_currency").format(val=s.get("currency", 0))
    text += t(L, "stats_since").format(val=user.get("since", "—"))
    bot.send_message(msg.chat.id, md(text), parse_mode="HTML",
                     reply_markup=main_keyboard(msg.chat.id))


# ─── ИСТОРИЯ ──────────────────────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_history"))
def show_history(msg):
    L    = lang(msg.chat.id)
    user = get_user(str(msg.chat.id))
    hist = user.get("history", [])
    if not hist:
        bot.send_message(msg.chat.id, t(L, "history_empty"), reply_markup=main_keyboard(msg.chat.id))
        return
    text = t(L, "history_title")
    for i, h in enumerate(reversed(hist), 1):
        text += f"{i}. {h}\n"
    bot.send_message(msg.chat.id, md(text), parse_mode="HTML",
                     reply_markup=main_keyboard(msg.chat.id))


# ─── ПОМОЩЬ ───────────────────────────────────────────────────

@bot.message_handler(func=lambda m: is_btn(m, "btn_help"))
def show_help(msg):
    L = lang(msg.chat.id)
    bot.send_message(msg.chat.id, md(t(L, "help_text")), parse_mode="HTML",
                     reply_markup=main_keyboard(msg.chat.id))


@bot.message_handler(commands=["help"])
def cmd_help(msg):
    show_help(msg)


# ─── ФОНОВАЯ ПРОВЕРКА ─────────────────────────────────────────

def check_weather_alerts():
    users = load_users()
    for uid, data in users.items():
        if not data.get("alerts") or not data.get("city"):
            continue
        L    = data.get("lang", "ru")
        city = data["city"]
        try:
            resp = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
            if resp.status_code != 200: continue
            d       = resp.json()
            current = d["current_condition"][0]
            weather = d["weather"]
            wind    = int(current["windspeedKmph"])
            feels   = int(current["FeelsLikeC"])
            uv      = int(current["uvIndex"])
            labels  = [t(L, "today"), t(L, "tomorrow")]
            warnings = []
            if wind >= 50:   warnings.append(t(L, "warn_wind"))
            if wind >= 80:   warnings.append(t(L, "warn_storm"))
            if feels <= -15: warnings.append(t(L, "warn_frost"))
            if feels >= 35:  warnings.append(t(L, "warn_heat"))
            if uv >= 8:      warnings.append(t(L, "warn_uv"))
            for i, day in enumerate(weather[:2]):
                rain_p = int(day["hourly"][4].get("chanceofrain", 0))
                snow_p = int(day["hourly"][4].get("chanceofsnow", 0))
                w_code = int(day["hourly"][4]["weatherCode"])
                lbl    = labels[i]
                if rain_p >= 70: warnings.append(t(L, "warn_rain").format(label=lbl, val=rain_p))
                if snow_p >= 70: warnings.append(t(L, "warn_snow").format(label=lbl, val=snow_p))
                if w_code in [386, 389]: warnings.append(t(L, "warn_thunder").format(label=lbl))
            if warnings:
                text = f"⚠️ <b>{city}</b>\n\n" + "\n".join(f"• {w}" for w in warnings)
                bot.send_message(uid, text, parse_mode="HTML")
        except Exception as e:
            print(f"Alert error {uid}: {e}")


def check_wishlist_schedule():
    users = load_users()
    now   = datetime.datetime.now().strftime("%H:%M")
    for uid, data in users.items():
        if data.get("schedule_time") != now: continue
        wl = data.get("wishlist", [])
        if not wl: continue
        L     = data.get("lang", "ru")
        books = fetch_books()
        for wish in wl:
            found = next((b for b in books if wish.lower() in b["name"].lower()), None)
            if found:
                text = f"🛒 <b>{wish}</b>\n💰 {found['price']}"
                bot.send_message(uid, text, parse_mode="HTML")


def run_scheduler():
    schedule.every(CHECK_INTERVAL).minutes.do(check_weather_alerts)
    schedule.every().day.at("07:00").do(check_weather_alerts)
    schedule.every().day.at("19:00").do(check_weather_alerts)
    schedule.every().minute.do(check_wishlist_schedule)
    while True:
        schedule.run_pending()
        time.sleep(30)


# ─── НЕИЗВЕСТНАЯ КОМАНДА ──────────────────────────────────────

@bot.message_handler(func=lambda m: True)
def unknown(msg):
    L = lang(msg.chat.id)
    bot.send_message(msg.chat.id, t(L, "unknown_cmd"), reply_markup=main_keyboard(msg.chat.id))


# ─── ЗАПУСК ───────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("Telegram бот запущен! 🇷🇺 🇩🇪 🇬🇧")
    print(f"Время: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    threading.Thread(target=run_scheduler, daemon=True).start()
    bot.infinity_polling()
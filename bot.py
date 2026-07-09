import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "Бот жұмыс істеп тұр!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ===== ТОКЕНДІ ҚОЙЫҢЫЗ =====
TOKEN = "8145235496:AAEmVo271zNlbOVyoRlgb1I9QkmOWrxMBVw"

# Логинг
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ============ АЛМАТЫ ТУРАЛЫ МӘЛІМЕТ ============
ALMATY_STATS = {
    "population": "2,225,000+ адам",
    "area": "682 км²",
    "density": "3,263 адам/км²",
    "foundation": "1854 жыл",
    "timezone": "UTC+5 (Астана уақыты)"
}

# ============ КӨРІКТІ ОРЫНДАР (СУРЕТТЕРІМЕН) ============
ATTRACTIONS = {
    "koktobe": {
        "name": "🏔️ Көктөбе",
        "emoji": "🏔️",
        "description": "✨ Алматының ең биік нүктесі (1100 м).\n🏰 Айналмалы телевежа, бақылау алаңы\n🍫 Шоколад фабрикасы, аттракциондар\n🌃 Түнгі Алматының керемет көрінісі",
        "address": "📍 Көктөбе көшесі, 1",
        "price": "💰 1000-3000 теңге",
        "time": "🕐 09:00 - 23:00",
        "image": "https://koktobe.com/storage/pages/November2024/fnilnttJzYB2jVpNpfCr.webp"
    },
    "medeu": {
        "name": "🏔️ Медеу",
        "emoji": "🏔️",
        "description": "⛷️ Әлемдегі ең биік тау-шаңғы курорты (1691 м)\n❄️ Қыста - шаңғы, жазда - треккинг\n🏊 Жазғы ашық бассейн\n🌄 Керемет тау пейзаждары",
        "address": "📍 Медеу шатқалы",
        "price": "💰 2000-8000 теңге",
        "time": "🕐 08:00 - 22:00",
        "image": "https://guideservice.kz/wp-content/uploads/2025/04/medeu-scaled-e1642653334143.jpg"
    },
    "shymbulak": {
        "name": "⛷️ Шымбұлақ",
        "emoji": "⛷️",
        "description": "🏔️ Алматының басты тау-шаңғы курорты (2260 м)\n🎿 Жыл бойы жұмыс істейді\n🚠 Жылдам аспалы жол\n🌨️ Қыста - шаңғы, жазда - треккинг",
        "address": "📍 Шымбұлақ шатқалы",
        "price": "💰 5000-15000 теңге",
        "time": "🕐 09:00 - 21:00",
        "image": "https://arendacar.kz/wp-content/uploads/sites/16/2025/09/MxHIGphG.jpg"
    },
    "panfilov": {
        "name": "🌳 Панфилов саябағы",
        "emoji": "🌳",
        "description": "🌲 Қаланың орталығындағы тарихи саябақ\n⛪ Вознесенск соборы\n🕊️ 28 панфиловшылар мемориалы\n🌸 Әдемі гүлзарлар мен субұрқақтар",
        "address": "📍 Қонаев көшесі",
        "price": "💰 Тегін",
        "time": "🕐 24/7",
        "image": "https://www.advantour.com/img/kazakhstan/almaty/panfilov-park/28panfilov-guardsmen1.jpg"
    },
    "ascension": {
        "name": "⛪ Вознесенск соборы",
        "emoji": "⛪",
        "description": "⛪ Алматыдағы ең әдемі православие шіркеуі\n🌳 Ағаштан салынған, ең биік ағаш ғимарат\n✨ 1907 жылы салынған\n📸 Суретке түсуге тамаша орын",
        "address": "📍 Панфилов саябағы",
        "price": "💰 Тегін",
        "time": "🕐 07:00 - 19:00",
        "image": "https://mitropolia.kz/images/01_cont/88/888/0953.jpg"
    },
    "green_bazaar": {
        "name": "🛒 Көк базар",
        "emoji": "🛒",
        "description": "🛍️ Алматының ең көне және үлкен базары\n🍎 Жеміс-жидектер, дәмдеуіштер\n🧀 Ұлттық тағамдар, құрт, ірімшік\n🎁 Кәдесыйлар мен сыйлықтар",
        "address": "📍 Зенков көшесі, 1",
        "price": "💰 Тегін (кіру)",
        "time": "🕐 09:00 - 19:00",
        "image": "https://eurasia.travel/wp-content/uploads/2024/10/2.-Green-Bazaar-Almaty.jpg"
    },
    "arbat": {
        "name": "🎨 Арбат көшесі",
        "emoji": "🎨",
        "description": "🎨 Жаяу жүргіншілер көшесі\n🎭 Суретшілер, музыканттар\n🗿 Қызықты мүсіндер\n🛍️ Дүкендер мен кафелер",
        "address": "📍 Жібек жолы көшесі",
        "price": "💰 Тегін",
        "time": "🕐 10:00 - 22:00",
        "image": "https://sxodim.com/uploads/posts/2023/03/28/optimized/7ef6872e1e781ab8248624fe437a65e0_1400x790-q-85.jpg"
    },
    "presidential_park": {
        "name": "🌿 Президент саябағы",
        "emoji": "🌿",
        "description": "🌳 Алматыдағы ең үлкен және әдемі саябақ\n⛲ Керемет фонтандар\n🚴 Веложолдар мен пикник алаңдары\n🌅 Тау көрінісімен бірге демалу",
        "address": "📍 Назарбаев даңғылы",
        "price": "💰 Тегін",
        "time": "🕐 08:00 - 22:00",
        "image": "https://sxodim.com/uploads/posts/2023/06/02/optimized/7c5e87252a89aa14f87f4c3b4af2d4ad_1400x790-q-85.jpg"
    },
    "zoo": {
        "name": "🐘 Алматы хайуанаттар бағы",
        "emoji": "🐘",
        "description": "🐅 Қазақстандағы ең үлкен хайуанаттар бағы\n🦁 200+ жануар түрі\n🦒 Африка саваннасы, жыртқыштар\n🌿 Жасыл аймақта серуендеу",
        "address": "📍 Ерубаев көшесі, 22",
        "price": "💰 500-1500 теңге",
        "time": "🕐 09:00 - 18:00",
        "image": "https://almatyzoo.kz/wp-content/uploads/2026/04/almatyzoo.png"
    },
    "big_almaty_lake": {
        "name": "🏞️ Үлкен Алматы көлі",
        "emoji": "🏞️",
        "description": "💎 Алматыдан 28 км жердегі тау көлі\n💧 Керемет көгілдір су түсі\n🏔️ Тау пейзаждары мен таза ауа\n📸 Фотосессия үшін тамаша орын",
        "address": "📍 Іле Алатауы ұлттық паркі",
        "price": "💰 1000 теңге (кіру)",
        "time": "🕐 08:00 - 20:00",
        "image": "https://kz.kazgeo.kz/userfiles/N1hTyJWWHoM.jpg"
    },
    "kolsay": {
        "name": "🏞️ Көлсай көлдері",
        "emoji": "🏞️",
        "description": "💎 Алматы облысындағы 3 керемет көл\n🏔️ Таулар арасындағы айдай көлдер\n⛺ Жаяу саяхат, кемпинг\n📸 Табиғат фотосуреттері",
        "address": "📍 Көлсай ауылы",
        "price": "💰 1500 теңге",
        "time": "🕐 24/7",
        "image": "https://static.tildacdn.pro/tild3734-3066-4062-b963-343839616161/_2.jpg"
    },
    "charyn": {
        "name": "🏜️ Шарын шатқалы",
        "emoji": "🏜️",
        "description": "🏜️ Гранд-Каньонға ұқсас шатқал\n🎨 Қызыл жарлар, таңғажайып көрініс\n📸 Фотосуреттерге тамаша\n⛺ Кемпинг және серуендеу",
        "address": "📍 Шарын ұлттық паркі",
        "price": "💰 1500 теңге",
        "time": "🕐 08:00 - 20:00",
        "image": "https://akyldy.kz/wp-content/uploads/2025/03/sharyn-shatqaly-twraly-qyzyqty-maelimetter.jpg"
    }
}

# ============ ҚОҒАМДЫҚ КӨЛІК ============
TRANSPORT = {
    "metro": {
        "name": "🚇 Метро",
        "stations": "11 станция",
        "price": "80 теңге",
        "student_price": "40 теңге",
        "time": "06:00 - 00:00"
    },
    "bus": {
        "name": "🚌 Автобус",
        "routes": "120+ маршрут",
        "price": "80 теңге",
        "student_price": "40 теңге",
        "time": "06:00 - 23:00"
    },
    "trolleybus": {
        "name": "🔌 Троллейбус",
        "routes": "10 маршрут",
        "price": "80 теңге",
        "student_price": "40 теңге",
        "time": "06:00 - 22:00"
    },
    "taxi": {
        "name": "🚕 Такси",
        "companies": "Яндекс Go, Uber, Оңайлық",
        "price": "500-2000 теңге",
        "time": "24/7"
    }
}

# ============ БОТ КОМАНДАЛАРЫ ============
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏙️ Алматы туралы", callback_data='stats')],
        [InlineKeyboardButton("🗺️ Көрікті орындар", callback_data='attractions')],
        [InlineKeyboardButton("🚌 Қоғамдық көлік", callback_data='transport')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "🌆 **Алматыға қош келдіңіз!**\n\n"
        "🏔️ Мен сізге Алматы қаласы туралы туристік ақпарат беремін:\n"
        "• Қала туралы негізгі мәліметтер\n"
        "• Көрікті орындар мен бағалар\n"
        "• Қоғамдық көлік\n\n"
        "👇 Төмендегі батырмаларды таңдаңыз"
    )

    await update.message.reply_text(welcome_text, parse_mode='Markdown', reply_markup=reply_markup)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🏙️ **Алматы қаласы туралы**\n\n"
        f"👨‍👩‍👧‍👦 Халық саны: {ALMATY_STATS['population']}\n"
        f"📐 Ауданы: {ALMATY_STATS['area']}\n"
        f"📊 Халық тығыздығы: {ALMATY_STATS['density']}\n"
        f"📅 Құрылған жылы: {ALMATY_STATS['foundation']}\n"
        f"🕐 Уақыт белдеуі: {ALMATY_STATS['timezone']}\n\n"
        "🏔️ Теңіз деңгейінен биіктігі: 700-900 м\n"
        "🌡️ Орташа жылдық температура: +10°C"
    )

    keyboard = [[InlineKeyboardButton("🔙 Артқа", callback_data='back_main')]]

    if update.callback_query:
        await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.message.reply_text(text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))

async def attractions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    row = []
    for key, attr in ATTRACTIONS.items():
        row.append(InlineKeyboardButton(attr['name'], callback_data=f'place_{key}'))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    keyboard.append([InlineKeyboardButton("🔙 Артқа", callback_data='back_main')])

    reply_markup = InlineKeyboardMarkup(keyboard)

    # ТҮЗЕТУ: Ескі хабарламаны өшіріп, жаңасын жіберу
    try:
        await update.callback_query.delete_message()
        await update.callback_query.message.reply_text(
            "🗺️ **Алматының көрікті орындары:**\n\n🏔️ Төмендегі орындарды таңдап, суреттер мен толық ақпаратты көріңіз 👇",
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    except:
        await update.callback_query.edit_message_text(
            "🗺️ **Алматының көрікті орындары:**\n\n🏔️ Төмендегі орындарды таңдап, суреттер мен толық ақпаратты көріңіз 👇",
            parse_mode='Markdown',
            reply_markup=reply_markup
        )

async def place_detail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    place_key = query.data.replace('place_', '')
    place = ATTRACTIONS.get(place_key)

    if place:
        text = (
            f"✨ **{place['name']}** ✨\n\n"
            f"{place['description']}\n\n"
            f"{place['address']}\n"
            f"{place['price']}\n"
            f"{place['time']}"
        )

        keyboard = [
            [InlineKeyboardButton("🔙 Көрікті орындар", callback_data='attractions')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        try:
            await query.delete_message()
            await query.message.reply_photo(
                photo=place['image'],
                caption=text,
                parse_mode='Markdown',
                reply_markup=reply_markup
            )
        except Exception as e:
            await query.edit_message_text(
                text,
                parse_mode='Markdown',
                reply_markup=reply_markup
            )

async def transport(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "🚌 **Алматы қоғамдық көлігі**\n\n"

    for key, t in TRANSPORT.items():
        text += f"**{t['name']}**\n"
        if key == "taxi":
            text += f"• Қызметтер: {t['companies']}\n"
        elif key == "metro":
            text += f"• Станциялар: {t['stations']}\n"
        else:
            text += f"• Маршруттар: {t['routes']}\n"

        text += f"• Бағасы: {t['price']}\n"
        if "student_price" in t:
            text += f"• Студенттік: {t['student_price']}\n"
        text += f"• Жұмыс уақыты: {t['time']}\n\n"

    text += "💳 **Төлем әдістері:**\n"
    text += "• Онлайн төлем (Оңай, Kaspi, QR код)\n"
    text += "• Транспорт картасы\n"
    text += "• Қолма-қол ақша\n\n"

    text += "📱 **Пайдалы қосымшалар:**\n"
    text += "• 2GIS - Алматы картасы\n"
    text += "• Яндекс.Карты - навигация\n"
    text += "• Оңайлық - такси\n"
    text += "• Яндекс Go - такси және көлік"

    keyboard = [[InlineKeyboardButton("🔙 Артқа", callback_data='back_main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        # Батырма арқылы шақырылды
        await update.callback_query.answer()
        try:
            await update.callback_query.edit_message_text(
                text, parse_mode='Markdown', reply_markup=reply_markup
            )
        except Exception as e:
            logging.error(f"Transport handler (callback) error: {e}")
            try:
                await update.callback_query.edit_message_text(
                    text, reply_markup=reply_markup
                )
            except Exception as e2:
                logging.error(f"Transport handler (plain text) error: {e2}")
    else:
        # /transport командасы арқылы шақырылды
        await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def back_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏙️ Алматы туралы", callback_data='stats')],
        [InlineKeyboardButton("🗺️ Көрікті орындар", callback_data='attractions')],
        [InlineKeyboardButton("🚌 Қоғамдық көлік", callback_data='transport')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "🌆 **Алматыға қош келдіңіз!**\n\n"
        "👇 Төмендегі батырмаларды таңдаңыз"
    )

    if update.callback_query:
        await update.callback_query.edit_message_text(
            welcome_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            welcome_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )

# ============ НЕГІЗГІ ФУНКЦИЯ ============
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("attractions", attractions))
    app.add_handler(CommandHandler("transport", transport))

    app.add_handler(CallbackQueryHandler(place_detail, pattern='^place_'))
    app.add_handler(CallbackQueryHandler(back_main, pattern='^back_main$'))
    app.add_handler(CallbackQueryHandler(stats, pattern='^stats$'))
    app.add_handler(CallbackQueryHandler(attractions, pattern='^attractions$'))
    app.add_handler(CallbackQueryHandler(transport, pattern='^transport$'))

    print("=" * 50)
    print("🎨  СТИЛЬДІ АЛМАТЫ БОТЫ ІСКЕ ҚОСЫЛДЫ!")
    print("=" * 50)
    print("📋 Қолда бар мүмкіндіктер:")
    print("   🏙️  Алматы туралы статистика")
    print("   🗺️  12 көрікті орын (суреттерімен)")
    print("   🚌  Қоғамдық көлік")
    print("=" * 50)

    app.run_polling()

if __name__ == "__main__":
    keep_alive()  # БІРІНШІ веб-серверді фондық режимде қосамыз
    main()        # СОСЫН БАРЫП ботты іске қосамыз

import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Aapka new bot token
BOT_TOKEN = '8478992800:AAHjKPRjBMCL8EUQocQHVFBhs894LR-FEjM'

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Fixed reply texts
WELCOME_TEXT = (
    "WELCOME TRADER BM ALWAYS WITH YOU ❤️\n\n"
    "Asslamualikum, Ayaan here! I wish aapki trading journey profitable ho.\n\n"
    "Main yahan hoon aapki madad ke liye — kabhi bhi!\n\n"
    "Check the menu buttons, ye aapki madad karega. 😊"
)

BUTTON_VIP = (
    "WANT TO JOIN MENTOR VIP 🏆\n\n"
    "𝗦𝘁𝗲𝗽 𝟭:- FREE MENTOR VIP join karne ke liye Binomo ya Quotex ka new account banaye niche diyehue link se 👇\n\n"
    "Binomo: https://binomo.com/en?a=67b579d50117\n\n"
    "Quotex: https://broker-qx.pro/?lid=1375315\n\n"
    "𝗦𝘁𝗲𝗽 𝟮:- New account me ₹2000 deposit kijiye 💸\n\n"
    "𝗦𝘁𝗲𝗽 𝟯:- Trader ID bhejiye @Ayaan_Mentor pe.\n\n"
    "Uske baad aapko lifetime FREE VIP access milega 💚\n\n"
    "NOTE: Account banane se pehle browser ka data clear kar lijiye"
)

BUTTON_EBOOKS = (
    "@Ayaan_Mentor par DM kijiye — aapko helpful trading PDF's bheji jayegi📘\n\n"
    "Agar aap trading sikhna chahte ho, to jo PDF send karenge hum bhot kaam ki hai apke trading journey main.\n\n"
    "Start sharpening your knowledge. Let's grow together, Happy trading journey 💝💐"
)

BUTTON_CHANNEL = (
    "https://t.me/BinaryMentor07\n\n"
    "Join kijiye hamara free public trading channel, jisme apko free signal, guidance aur learning content milange. 📈📚"
)

BUTTON_CONTACT = (
    "@Ayaan_Mentor\n"
    "Aapka koi bhi sawal hai? aap mujhse upar diye gaye username pe directly baat kar sakte hai, bina hesitation DM kijiye, bs ek bar 'ayaan bhai' lekh ke msg send kiijiye 👋🤗"
)

BUTTON_ADMIN = (
    "@Imshoeb yaha message kijiye or jo doubts h boliye reply milega turant.\n\n"
    "BM ALWAYS WITH YOU HAPPY TRADING ❤️😊"
)

# Create a Reply Keyboard with 5 fixed buttons
keyboard = [
    [KeyboardButton("JOIN MENTOR VIP🏆")],
    [KeyboardButton("TRADING E BOOKS📚")],
    [KeyboardButton("OUR FREE CHANNEL👑")],
    [KeyboardButton("CONTACT WITH AYAAN💠")],
    [KeyboardButton("ADMIN")]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

def start(update: Update, context: CallbackContext) -> None:
    """Handles /start command."""
    update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

def handle_message(update: Update, context: CallbackContext) -> None:
    """Replies based on the button pressed."""
    user_text = update.message.text.strip()
    if user_text == "JOIN MENTOR VIP🏆":
        update.message.reply_text(BUTTON_VIP)
    elif user_text == "TRADING E BOOKS📚":
        update.message.reply_text(BUTTON_EBOOKS)
    elif user_text == "OUR FREE CHANNEL👑":
        update.message.reply_text(BUTTON_CHANNEL)
    elif user_text == "CONTACT WITH AYAAN💠":
        update.message.reply_text(BUTTON_CONTACT)
    elif user_text == "ADMIN":
        update.message.reply_text(BUTTON_ADMIN)
    else:
        update.message.reply_text("Sorry, I didn't understand that. Please use the menu buttons.")

def main() -> None:
    """Start the bot."""
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Message handler for button replies
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start webhook for Railway deployment:
    PORT = 8000
    updater.start_webhook(listen="0.0.0.0", 
                          port=PORT, 
                          url_path=BOT_TOKEN)

    # Set the webhook URL.
    # Replace 'YOUR_RAILWAY_APP_DOMAIN' with your actual Railway app URL.
    webhook_url = f"https://YOUR_RAILWAY_APP_DOMAIN/{BOT_TOKEN}"
    updater.bot.setWebhook(webhook_url)
    logger.info("Webhook set to: %s", webhook_url)

    updater.idle()

if __name__ == '__main__':
    main()

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '8478992800:AAGkMZXQ5LVYMEaHkjh6LRvpn_8mSuIz-pE'

def start(update: Update, context: CallbackContext) -> None:
    buttons = [['JOIN MENTOR VIP🏆'], ['TRADING E BOOKS📚'], ['OUR CHANNEL'], ['CONTACT WITH AYAN']]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    update.message.reply_text(
        'WELCOME TRADER BM ALWAYS WITH YOU ❤️\n\n'
        'Asslamualikum Ayaan here, I wish aapki trading journey profitable ho & I\'m here to help and guide you anytime.\n\n'
        'Check The Menu Buttons, Ye Aapki Madad Karega. 😊',
        reply_markup=reply_markup
    )

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text == 'JOIN MENTOR VIP🏆':
        update.message.reply_text(
            "VIP Group Join Karne Ke Liye Yeh Steps Follow Karo:\n\n"
            "1. Apna name & screenshot bhejo\n"
            "2. Payment info:\n"
            "UPI ID: ayaansharma@ybl\n"
            "Fee: ₹499 Lifetime\n"
            "3. Uske baad VIP group ka link milega ✅"
        )
    elif text == 'TRADING E BOOKS📚':
        update.message.reply_text("Yahan aapko trading seekhne ke liye best E-books milengi:\nhttps://t.me/ayaanmentor")
    elif text == 'OUR CHANNEL':
        update.message.reply_text("Join Our Official Channel for Updates:\nhttps://t.me/ayaanmentor")
    elif text == 'CONTACT WITH AYAN':
        update.message.reply_text("Contact Me On Telegram:\n@Ayaan_Mentor")
    else:
        update.message.reply_text("Please use the menu buttons below 👇")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

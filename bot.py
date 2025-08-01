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
            'WANT TO JOIN MENTOR VIP 🏆\n\n'
            '𝗦𝘁𝗲𝗽 𝟭:- FREE MENTOR VIP join karne ke liye Binomo ya fir Quotex ka link se new account register kar lijiye👇\n'
            'Binomo: https://binomo.com/en?a=67b579d50117\n'
            'Quotex: https://broker-qx.pro/?lid=1375315\n\n'
            '𝗦𝘁𝗲𝗽 𝟮:- Apne account me ₹2000 deposit kijiye 💸\n'
            '𝗦𝘁𝗲𝗽 𝟯:- Apna Trader ID mujhe bhejiye (profile section me).\n'
            'Send it Here: @Ayaan_Mentor\n\n'
            'Fir aapko lifetime free MENTOR VIP access milega! 💚\n'
            'NOTE: Account banane se pehle browser ka data clear kar lena.'
        )
    elif text == 'TRADING E BOOKS📚':
        update.message.reply_text(
            '@Ayaan_Mentor pe DM karo. PDF helpful hogi trading learn karne ke liye.\n\n'
            'Sharpen your knowledge & grow together. Happy trading journey 💝💐'
        )
    elif text == 'OUR CHANNEL':
        update.message.reply_text(
            'https://t.me/BinaryMentor07\n\n'
            'Join hamara channel for daily sure‑shot signals aur learning content.'
        )
    elif text == 'CONTACT WITH AYAN':
        update.message.reply_text(
            '@Ayaan_Mentor\n\n'
            'Koi bhi sawal ho toh directly mujhe DM kijiye. Main help ke liye yahan hoon 👋🤗'
        )
    else:
        update.message.reply_text("Please use the menu buttons 👇")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

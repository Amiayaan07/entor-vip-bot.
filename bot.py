from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '8478992800:AAGkMZXQ5LVYMEaHkjh6LRvpn_8mSuIz-pE'

def start(update: Update, context: CallbackContext) -> None:
    buttons = [['JOIN MENTOR VIP🏆'], ['TRADING E BOOKS📚'], ['OUR CHANNEL'], ['CONTACT WITH AYAN']]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    update.message.reply_text(
        'WELCOME TRADER BM ALWAYS WITH YOU ❤️\n\n'
        'Asslamualikum ayaan here, I wish aapki trading journey profitable ho & I\'m here to help and guide you anytime.\n\n'
        'Check The Menu Buttons, Ye Aapki Madad Karega. 😊',
        reply_markup=reply_markup
    )

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text == 'JOIN MENTOR VIP🏆':
        update.message.reply_text(
            'WANT TO JOIN MENTOR VIP 🏆\n\n'
            '𝗦𝘁𝗲𝗽 𝟭:- FREE MENTOR VIP join karne ke liye Binomo ya fir Quotex ka niche hue link se new account register kar lijiye👇\n\n'
            'Binomo: https://binomo.com/en?a=67b579d50117\n'
            'Quotex: https://broker-qx.pro/?lid=1375315\n\n'
            '𝗦𝘁𝗲𝗽 𝟮:- Uske baad apne new account me minimum ₹2000 deposit kar lijiye 💸\n'
            '𝗦𝘁𝗲𝗽 𝟯:- Then mujhe apna trader ID send kr dijiye jo profile section me hota h.\n\n'
            'Send it Here: @Ayaan_Mentor\n\n'
            'Fir aapko MENTOR VIP ka lifetime access mil jayega totally free 💚\n\n'
            'IMPORTANT NOTE: New account banane se pahle apne Browser ka data clear kar lijiye.'
        )
    elif text == 'TRADING E BOOKS📚':
        update.message.reply_text(
            '@Ayaan_Mentor yaha dm kijiye jo PDF aapko send kiya jayega aapke liye bhot helpful hoga aagar app trading sikhna chhate h,\n\n'
            'So start sharpening your knowledge & let\'s grow together. Happy trading journey 💝💐'
        )
    elif text == 'OUR CHANNEL':
        update.message.reply_text(
            'https://t.me/BinaryMentor07\n\n'
            'Join kijiye hamara channel, for daily sure-shot signal and learning content.'
        )
    elif text == 'CONTACT WITH AYAN':
        update.message.reply_text(
            '@Ayaan_Mentor Aapka koi bhi sawal hai? aap mujhse upar diye gaye username pe directly mujhse baat kar sakte hai 👋🤗'
        )
    else:
        update.message.reply_text("Please use the menu buttons.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

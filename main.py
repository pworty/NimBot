from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, ConversationHandler, \
    MessageHandler, Filters
from nim import nim
from bot_data import TOKEN, PROXY

NIM_SOLVE = 0

menu_keyboard = [['/nim_start']]
menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True)


def start(update, context):
    update.message.reply_text("Hello! I am NimBot. I can help you cheat on exams\n\n"
                              "What I can do:\n"
                              "/nim_start - access nim problems menu\n\n\n\n"
                              "/katya",
                              reply_markup=menu_markup)


def nim_start(update, context):
    update.message.reply_text('Enter values: S N1 ADD MULTIPLY\n\n'
                              'Separate values with spaces')
    return NIM_SOLVE


def nim_solve(update, context):
    message = update.message.text
    nim(*map(int, message.split()))
    chat_id = update.message.chat_id
    f = open("Nim.xlsx", "rb")
    context.bot.send_document(chat_id=chat_id, document=f)


def katya(update, context):
    update.message.reply_text("Катя у меня лучше проект не будет тебе никакой таблицы")


def cancel(update, context):
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN, use_context=True)

    create_chat = ConversationHandler(
        entry_points=[CommandHandler('nim_start', nim_start)],

        states={
            NIM_SOLVE: [MessageHandler(Filters.text, nim_solve, pass_user_data=True)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
        allow_reentry=True
    )

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('katya', katya))
    dp.add_handler(create_chat)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

from telegram import Update
from telegram.ext import ContextTypes

async def show_user_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get('language', 'English')
    MESSAGE = "هذا كل شيء قمت بتخزينه" if lang == "Arabic" else "This is everything you had me store"
    chat_id = update.message.chat_id
    bot = context.bot
    context.user_data['name'] = update.message.from_user.first_name
    await bot.send_message(chat_id=chat_id, text=
        f"{MESSAGE}:\n\n{dict_to_str(context.user_data)}"
    )


def dict_to_str(dictionary: dict) -> str:
    return "\n".join(f"{key}: {value}" for key, value in dictionary.items())

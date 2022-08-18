import datetime
import re
from telegram import Update
from telegram.ext import CallbackContext

# Globals

async def callback_alarm(context: CallbackContext):
    await context.bot.send_message(chat_id=context.job.chat_id, text=f'{context.job.data}')

async def callback_timer(update: Update, context: CallbackContext):
    duration = parse_time_string( str(context.args[0]) )
    is_arabic = context.user_data.get('language', 'English') == 'Arabic'
    REMINDER_SET = "تم ضبط المذكرة!" if is_arabic else "Reminder set!"
    text = ' '.join(context.args[1:])
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id=chat_id, text=f'{REMINDER_SET}')
    # Set the alarm:
    context.job_queue.run_once(callback_alarm, duration, data=text, chat_id=chat_id)

def parse_time_string(time_string: str) -> int:
    # Example: '1w 1d 2h 3m 4s'
    weeks = re.findall(r'\d+w', time_string)
    weeks = 0 if len(weeks) == 0 else int(weeks[0][:-1])

    days = re.findall(r'\d+d', time_string)
    days = 0 if len(days) == 0 else int(days[0][:-1])

    hours = re.findall(r'\d+h', time_string)
    hours = 0 if len(hours) == 0 else int(hours[0][:-1])

    minutes = re.findall(r'\d+m', time_string)
    minutes = 0 if len(minutes) == 0 else int(minutes[0][:-1])

    seconds = re.findall(r'\d+s', time_string)
    seconds = 0 if len(seconds) == 0 else int(seconds[0][:-1])
    time = datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    return time.total_seconds()


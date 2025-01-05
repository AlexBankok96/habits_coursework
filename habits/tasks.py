from celery import shared_task
from datetime import datetime
from habits.models import Habits
from habits.services import send_telegram_message


def should_send_reminder(habit):
    if habit.period == 'daily':
        return True  # Для ежедневных привычек
    elif habit.period == 'weekly':
        return datetime.now().weekday() == 0  # Каждую неделю в понедельник
    elif habit.period == 'monthly':
        return datetime.now().day == 1  # 1-го числа каждого месяца
    return False


@shared_task
def send_habit_reminders():
    for habit in Habits.objects.filter(is_public=True):
        if should_send_reminder(habit):
            send_telegram_message(habit.owner.telegram_chat_id, f"Напоминание: {habit.action}")

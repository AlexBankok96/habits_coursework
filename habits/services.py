import requests
from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_telegram_message(chat_id, message):
    """
    Отправка сообщения в телеграм-чат
    :param chat_id: ID чата
    :param message: текст сообщения
    :return: HTTP-ответ
    """
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    response = requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
    return response

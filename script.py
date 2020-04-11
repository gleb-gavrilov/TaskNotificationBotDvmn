import requests
import time
import telegram
from telegram import utils
from urllib.parse import urljoin
import os
from dotenv import load_dotenv
import textwrap


def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)


def main():
    load_env()
    headers = {
        'Authorization': 'Token {}'.format(os.getenv('dvmn_token'))
    }
    url = 'https://dvmn.org/api/long_polling/'
    timestamp = time.time()
    while True:
        try:
            response = requests.get(url, headers=headers, params={'timestamp': timestamp}, timeout=60)
            response.raise_for_status()
            response_data = response.json()
            if response_data['status'] == 'timeout':
                timestamp = response_data['timestamp_to_request']
            elif response_data['status'] == 'found':
                send_message(response_data['new_attempts'])
                timestamp = response_data['last_attempt_timestamp']
                print('Обнаружен ответ по задаче!')
        except requests.exceptions.ReadTimeout:
            print('timeout!')
        except ConnectionError:
            print('Проблемы с соединением')


def send_message(attempts):
    proxy = telegram.utils.request.Request(proxy_url=os.getenv('proxy_socks5'))
    bot = telegram.Bot(token=os.getenv('telegram_token'), request=proxy)
    status = 'Принято 👍'
    text = '''
            Хэй!
            Тут по твоей задаче кое-что ответили
            Статус: {}
            Тема модуля: {}
            URL: {}
         '''
    text = textwrap.dedent(text)
    for attempt in attempts:
        if attempt['is_negative']:
            status = 'Возвращена в работу 😔'
        title = attempt['lesson_title']
        lesson_url = urljoin('https://dvmn.org/', attempt['lesson_url'])
        text = text.format(status, title, lesson_url)
    bot.send_message(chat_id=os.getenv('my_telegram_id'), text=text)


if __name__ == '__main__':
    main()

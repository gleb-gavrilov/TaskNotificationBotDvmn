import requests
import time
import telegram
from telegram import utils
from urllib.parse import urljoin
from config import token_telegram, my_telegram_id, proxy, token_dvm


def main():
    headers = {
        'Authorization': 'Token ' + token_dvm
    }
    url = 'https://dvmn.org/api/long_polling/'
    is_one_more_request = False
    while True:
        if not is_one_more_request:
            timestamp = time.time()
        try:
            response = requests.get(url, headers=headers, params={'timestamp': timestamp})
            response.raise_for_status()
            response_data = response.json()
            if response_data['status'] == 'timeout':
                timestamp = response_data['timestamp_to_request']
            elif response_data['status'] == 'found':
                send_message(response_data['new_attempts'])
                timestamp = response_data['last_attempt_timestamp']
            is_one_more_request = True
        except requests.exceptions.ReadTimeout:
            print('timeout')
            is_one_more_request = False
        except ConnectionError:
            print('Проблемы с соединением')
            is_one_more_request = False


def send_message(api_answers):
    config_proxy = telegram.utils.request.Request(proxy_url=proxy)
    bot = telegram.Bot(token=token_telegram, request=config_proxy)
    status_task = 'Принято 👍'
    text = 'Хэй!\nТут по твоей работе кое-что ответили\nСтатус: {}\nТема модуля: {}\nURL: {}'
    for api_answer in api_answers:
        if api_answer['is_negative']:
            status_task = 'Возвращена в работу 😔'
        text = text.format(status_task, api_answer['lesson_title'], urljoin('https://dvmn.org/', api_answer['lesson_url']))

    bot.send_message(chat_id=my_telegram_id, text=text)


if __name__ == '__main__':
    main()

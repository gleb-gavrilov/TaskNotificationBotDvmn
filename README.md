# Бот для уведомления о проверке заданий

Бот отправляет через телеграм уведомление о проверке заданий. Основные токены:
* telegram_token ( токен от бота телеграма )
* my_telegram_id ( ваш телеграм айди )
* proxy_socks5 ( прокси socks5 )
* dvmn_token ( токен от девмана )

лежат в файле `.env` ( должен находиться в корне проекта ), который скрыт в `.gitignore` от коммитов. Там находятся только вышеуказанные переменные.


Для работы бота понадобятся четыре сторонние библиотеки:
* ##### requests ( `pip install requests==2.23.0` ) 
* ##### python-telegram-bot ( `pip install python-telegram-bot==12.5.1` )
* ##### PySocks ( `pip install python-telegram-bot[socks]==1.7.1` )
* ##### python-dotenv ( `pip install python-dotenv==0.12.0` )
Либо можно установить всё сразу `pip install -r requirements.txt`

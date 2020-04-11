# Бот для уведомления о проверке заданий

Бот отправляет через телеграм уведомление о проверке заданий. Основные токены:
* token_telegram 
* my_telegram_id 
* proxy 
* token_dvmn

лежат в файле `config.py`, его я по понятным причинам не коммитил. Там находятся только вышеуказанные переменные.


Для работы бота понадобятся три библиотеки:
* ##### requests ( `pip install requests==2.23.0` ) 
* ##### python-telegram-bot ( `pip install python-telegram-bot==12.5.1` )
* ##### PySocks ( `pip install python-telegram-bot[socks]==1.7.1` )
Либо можно установить всё сразу `pip install -r requirements.txt`

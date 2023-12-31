
# Публикуем комиксы из xkcd во Вконтакте
Скрипт публикует случайный комикс с сайта  [xkcd.com](https://xkcd.com/) на стену сообщества в VK.

## Требования
Для работы должен быть установлен python3. А также необходимо установить библиотеки requests, python-dotenv, 
которые описаны в файле requirements.txt
Чтобы установить python3 скачайте и ознакомьтесь с инструкцией по установке на сайте [python.org](https://www.python.org/downloads/)

## Как установить
Необходимые библиотеки устанавливаются командой:
```bash
pip install -r requirements.txt
```

## Настройки
Необходимо чтобы в дирректории проекта был файл .env, в котором содержаться переменные окружения:
* VK_TOKEN_ID - Токен пользователя. Где взять токен описано в [документации вконтакте](https://vk.com/dev/access_token).
* VK_USER_ID - id пользователя
* VK_GROUP_ID - id сообщества, на стену которого будем публиковать комикс.


## Пример запуска скрипта
```bash
python main.py
```

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
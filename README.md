# Avito-Test-Case

## Требуется:

Аккаунт в Slack, workspace в Slack, 3 канала, описанных в 
`config.json`

## Установка:

- склонировать репозиторий

### Подготовка к запуску

- создать приложение для Slack чата
- добавить разрешения для приложения `chat:write`
- подключить приложение к существующему workspace
- получить OAuth token для приложения и заменить его в файле `config.json`
- добавить приложение во все созданные каналы (Сведения о канале -> Интеграции 
-> Приложения -> Добавить приложение)

### Запуск

- из папки с проектом запустить команду `pip install slackclient`
- запустить `main.py` и проверить, что в каналы в Slack: 
test1, test2, test3 пришли уведомления

## Unit тесты

Запустить `/Tests/senderTest.py` и проверить, что тесты завершились с кодом `Ok`

- описан положительный тест на класс `Sender`, отвечающий за отправку
сообщений
- описан отрицательный тест на класс `Sender`, отвечающий за отправку
сообщений

## end-to-end тесты

Запустить `/Tests/mainTest.py` и проверить, что тест завершился с кодом `Ok`

- описан положительный тест в `mainTest.py` - отправляются тестовые сообщения 
и проверяется, дошли ли они успешно


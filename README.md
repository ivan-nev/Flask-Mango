# Тестовое задание 


## Задание 1

Написать bash или python или groovy скрипт, который будет контролировать потребление памяти и генерировать alarm путем отправки http запроса на API.

```shell
#python
import psutil
import requests

memory_info = psutil.virtual_memory()

# запись информации о свободной памяти через Flask в бд Mango (Задание 2)
response = requests.post('http://127.0.0.1:8080', json={'memory': memory_info.free, 'device': 'my_comp'})
print(response.status_code)
```


## Задание 2 

Создать docker-compose.yml разворачивающий приложение на python с простой реализацией REST API. Решение должно состоять из двух контейнеров:

а) Любая NoSQL DB.

б) Приложение на python, с использованием Flask, которое слушает на порту 8080 и принимает только методы GET, POST, PUT.

в) Создаем значение ключ=значение, изменяем ключ=новое_значение, читаем значение ключа.

г) Вновь созданные объекты должны создаваться, изменяться и читаться из NoSQL DB.

Создано приложение на python, с использованием Flask и Mango с комбинацией из первого задания.

POST запрос на порт 8080. Сервер его обрабатывает и записывает в базу данных Mango количество свободной памяти,
время, имя устройства. 

GET запрос получает все записи с возможностью пагинации

PUT запрос позволяет переименовывать устройства в БД

запуск контейнеров
```shell
docker-compose up -d
```
Примеры запросов в client.py
from pprint import pprint

import psutil
import requests

memory_info = psutil.virtual_memory()

# запись информации о свободной памяти
response = requests.post('http://127.0.0.1:8080', json={'memory': memory_info.free, 'device': 'my_comp'})
print(response.status_code)
print(response.json())

# # Переименование устройства
response = requests.put('http://127.0.0.1:8080/my_comp', json={'device': 'comp'})
print(response.status_code)
print(response.json())
#
#  Вывод данных о состоянии памяти
response = requests.get('http://127.0.0.1:8080/all', params={'page': 1, 'limit': 10})
print(response.status_code)
pprint(response.json())

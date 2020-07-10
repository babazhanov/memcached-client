# memcached-client
Клиент Memcached для Python

### Установка
Необходимо установить и запустить сервер Memcached. Для Windows в директории src можно запустить memcached.exe.

### Использование
```python
from memcahed import Client
client = Client('localhost')
client.connect()
client.set('key1', 'value1')
value1 = client.get('key1') # 'value1'
```

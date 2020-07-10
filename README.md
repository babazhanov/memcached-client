# memcached-client
Клиент Memcached для Python

### Установка
Необходимо установить и запустить сервер [Memcached](https://memcached.org/). Для Windows в директории srv можно запустить memcached.exe.

### Использование
```python
from memcahed import Client
client = Client('localhost')
client.connect()
client.set('key1', 'value1')
value1 = client.get('key1') # 'value1'
```

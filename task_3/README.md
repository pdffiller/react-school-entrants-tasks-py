# Задание 3. Реализовать шаблон проектирования `Publish-Subscribe`.

Необходимо создать класс Emitter, реализующий шаблон `Publish-Subscribe`, и содержащий
два метода:

  * `on(event, handler)` - связывает обработчик `handler` с событием `event`
  * `emit(event, data)` - генерирует событие `event`, вызывает все обработчики, 
  связанные с этим событием (если такие есть) и передает им в качестве аргумента `data`

## Например:

```python
from task_3 import Emitter

emitter = Emitter()

def print_connected(data):
    print('We have been connected to %s' % data)

def print_disconnected(data):
    print('We disconnected from %s' % data)

emitter.on('connect', print_connected)
emitter.on('disconnect', print_disconnected)

emitter.emit('connect', 'http-server')
# prints to console:
# > We have been connected to http-server
emitter.emit('connect', 'websocket')
# prints to console:
# > We have been connected to websocket

emitter.emit('disconnect', 'websocket')
# prints to console:
# > We disconnected from websocket
emitter.emit('disconnect', 'http-server')
# prints to console:
# > We disconnected from http-server
```

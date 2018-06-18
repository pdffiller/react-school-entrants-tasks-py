import unittest
from unittest.mock import MagicMock
from task_3 import Emitter

class EmitterTest(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(Emitter(), Emitter)
    
    def test_single_event_single_handler(self):
        handler = MagicMock()
        data = MagicMock()
        emitter = Emitter()
        emitter.on('event', handler)
        emitter.emit('event', data)
        handler.assert_called_once_with(data)
    
    def test_single_event_many_handlers(self):
        handler1 = MagicMock()
        handler2 = MagicMock()
        data = MagicMock()
        emitter = Emitter()
        emitter.on('event', handler1)
        emitter.on('event', handler2)
        emitter.emit('event', data)
        handler1.assert_called_once_with(data)
        handler2.assert_called_once_with(data)
    
    def test_many_events_single_handler(self):
        handler = MagicMock()
        data1 = MagicMock()
        data2 = MagicMock()
        data3 = MagicMock()
        emitter = Emitter()
        emitter.on('event-1', handler)
        emitter.on('event-2', handler)
        emitter.on('event-3', handler)
        emitter.emit('event-1', data1)
        emitter.emit('event-2', data2)
        emitter.emit('event-3', data3)
        self.assertEqual(handler.call_count, 3)
        self.assertEqual(handler.call_args_list, [
                         ((data1, ), ),
                         ((data2, ), ),
                         ((data3, ), )])
    
    def test_no_call_on_other_event(self):
        handler = MagicMock()
        data = MagicMock()
        emitter = Emitter()
        emitter.on('event', handler)
        emitter.emit('other-event', data)
        self.assertEqual(handler.call_count, 0)

if __name__ == '__main__':
    unittest.main()

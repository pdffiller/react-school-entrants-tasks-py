# -*- coding: utf-8 -*- 


class Emitter:
    def __init__(self):
        """Создает экземпляр класса Emitter."""
        pass

    def on(self, event, handler):
        """ связывает обработчик handler с событием event

        Parameters
        ---------
        event : str
            событие
        handler : func
            обработчик
        """
        pass

    def emit(self, event, data):
        """ Генерирует событие event -- вызывает все связанные с ним
            обработчики, в которые передает аргумент data

        Parameters
        ----------
        event : str
            событие
        data
            данные, которые необходимо передать обработчикам
        """
        pass

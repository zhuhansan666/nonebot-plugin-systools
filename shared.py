from typing import Literal

FLAG = Literal['none', 'keepLatest', 'keepEarliest']
FLAGS = list[FLAG]

EventNames = Literal['checkUpdate']

class BaseEvent:
    def __init__(self, name: EventNames, target: float, flags: FLAGS | None=None):
        """
        target -> 时间戳
        """
        self.__name = name
        self.__target = target
        self.__flags = [] if flags is None else flags

    @property
    def name(self):
        return self.__name
    
    @property
    def target(self):
        return self.__target
    
    @property
    def flags(self):
        return self.__flags

class CheckUpdateEvent(BaseEvent):
    def __init__(self, target: float, flags: FLAGS | None = None):
        super().__init__('checkUpdate', target, flags)

Events = BaseEvent | CheckUpdateEvent
EventList = list[Events]

eventList: EventList = []

globalDict = {
    'process': {
        'list': []  # {'process': {'stdout': stdout, 'stderr': stderr, 'stdin': stdin}, 'session': Session, 'killed': False, 'closed': (process.returncode is not None), 'process': process}
    }
}

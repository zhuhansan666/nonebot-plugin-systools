import time
from asyncio import iscoroutine
from nonebot import logger
from typing import Literal, Callable
from nonebot.exception import MatcherException

from ..shared import EventNames, EventList, Events, eventList

eventHandles = {}
def on(name: EventNames, callback: Callable):
    eventHandles[name] = callback

def off(name: EventNames):
    if (name in eventHandles.keys()):
        eventHandles.pop(name)

async def getMaxMin(eventList: EventList, rule: Literal['max', 'min']) -> Events | None:
    if (len(eventList)) <= 0:
        return

    return sorted(eventList, key=lambda item: item.target)[0 if rule == 'min' else -1]

async def remove(eventList: EventList):
    eventList = eventList.copy()
    
    for item in eventList:
        if ('keepLatest' in item.flags):
            tempList = []
            for item1 in eventList:
                if (item.name == item1.name and 'keepLatest' in item1.flags):
                    tempList.append(item1)
            earliestTime = await getMaxMin(tempList, 'max')
            if earliestTime:
                earliestTime = earliestTime.target
                for item1 in eventList:
                    if (item.name == item1.name and \
                        'keepLatest' in item1.flags and \
                            item1.target < earliestTime):
                        eventList.remove(item1)
        elif ('keepEarliest' in item.flags):
            tempList = []
            for item1 in eventList:
                if (item.name == item1.name and 'keepEarliest' in item1.flags):
                    tempList.append(item1)
            earliestTime = await getMaxMin(tempList, 'max')
            if earliestTime:
                earliestTime = earliestTime.target
                for item1 in eventList:
                    if (item.name == item1.name and \
                        'keepEarliest' in item1.flags and \
                            item1.target > earliestTime):
                        eventList.remove(item1)


async def loop(eventList: EventList):
    await remove(eventList)
    for event in eventList:
        if time.time() >= event.target:
            func = eventHandles.get(event.name)
            if (func):
                try:
                    result = func()
                    if (iscoroutine(result)):  # 如果是异步函数, 用 asyncio 的 iscoroutine
                        await result
                except MatcherException:
                    raise  # 排除 nonebot 所处理的异常 (如: FinishedException)
                except Exception as e:
                    logger.debug(f'运行 {event.name} 的事件处理函数错误: {repr(e)}')

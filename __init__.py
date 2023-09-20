from nonebot.plugin import PluginMetadata
from .config import Config
__plugin_meta__ = PluginMetadata(
    name="系统助手",
    description="系统助手 For Nonebot",
    usage="systool",
    type="application",
    homepage="https://github.com/zhuhansan666/nonebot-plugin-systools",
    config=Config,
    supported_adapters="~onebot.v11",
)
import time
from nonebot import on_command, require, logger
from nonebot.exception import MatcherException

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler

from .shared import eventList, CheckUpdateEvent
from .events.loop import loop, on
from .events.processLoop import processLoop

from .commands.exec import taskrun

scheduler.add_job(
    loop, "interval", seconds=0, name='systools_events_loop', id='systools_events_loop', kwargs={'eventList': eventList}  # 1s 检查一次
)

scheduler.add_job(
    processLoop, "interval", seconds=0, name='systools_process_loop', id='systools_process_loop'
)

logger.debug('systools 初始化成功')

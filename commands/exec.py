import asyncio
from sys import platform
from traceback import format_exc
from threading import Thread
from subprocess import Popen, STDOUT, PIPE
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.exception import MatcherException

from ..shared import globalDict

processDict = globalDict['process']
processQueue = processDict['list']

taskrun = on_command('taskrun')
@taskrun.handle()
async def taskrun_func(args: Message = CommandArg()):
    command = args.extract_plain_text()

    await taskrun.send(f'开始运行 {command}')

    try:
        encoding = 'gbk' if platform == 'win32' else 'utf-8'
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
    except MatcherException:
        raise
    except Exception as e:
        await taskrun.send(f'运行失败: {format_exc()}')

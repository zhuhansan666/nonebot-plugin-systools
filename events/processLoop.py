from sys import platform

from asyncio import iscoroutine
from subprocess import Popen

from ..shared import globalDict

processDict = globalDict['process']
processQueue = processDict['list']

async def processLoop():
    pass
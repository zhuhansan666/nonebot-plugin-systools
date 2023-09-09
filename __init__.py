import nonebot
from nonebot import on_command #引入on_command参数（必须）
from nonebot.adapters import Message #引入消息数组
from nonebot.params import CommandArg #引入消息分词
from .Ping import *
配置 = nonebot.get_driver().config
command_starts = list(nonebot.get_driver().config.command_start)
default_start = command_starts[0]

syshelp = on_command("syshelp")
@syshelp.handle()
async def handle_function(args: Message = CommandArg()):
    内容 = args.extract_plain_text()  #取命令后跟的内容
    if 内容 := 内容:
        return 0
    else:
        await syshelp.finish(f"""Systools帮助菜单
{command_starts}syshelp | 显示帮助菜单
{command_starts}ping | Ping网站延迟
{command_starts}whois | 获取网站Whois信息
{command_starts}sysinfo | 获取系统信息""")
        
ping = on_command("ping")
@ping.handle()
async def handle_function(args: Message = CommandArg()):
    内容 = args.extract_plain_text
    结果 = await ping(内容)
    await ping.finish(结果)

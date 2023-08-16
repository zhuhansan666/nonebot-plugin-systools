import nonebot
from nonebot import on_command #引入on_command参数（必须）
from nonebot.adapters import Message #引入消息数组
from nonebot.params import CommandArg #引入消息分词
配置 = nonebot.get_driver().config
command_starts = list(nonebot.get_driver().config.command_start)
default_start = command_starts[0]




systool = on_command("systool")
@systool.handle()
async def handle_function(args: Message = CommandArg()):
    内容 = args.extract_plain_text()  #取命令后跟的内容
    if 内容 := 内容:
        if 内容 == "help":
            return 0
    else:
        await systool.send("您好像没有添加任何参数，已默认输出帮助菜单")
        await systool.finish(f'''Systools帮助菜单
{default_start}systool  #Systools菜单
{default_start}systool ''')
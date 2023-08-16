import nonebot
from nonebot import on_command #引入on_command参数（必须）
from nonebot.adapters import Message #引入消息数组
from nonebot.params import CommandArg #引入消息分词
配置 = nonebot.get_driver().config
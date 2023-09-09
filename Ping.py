import socket
import requests
from nonebot import logger

def ping(ip):
    if ip:
        newip = ip.replace('http://', '').replace('https://', '')
        if ':' in newip:
            newip = newip.split(':')[0]

        if '/' in newip or '\\' in newip:
            newip = newip.split('/')[0].split('\\')[0]

        if newip != ip:
            ip = newip
            logger.debug(f"注意: IP 已自动格式化为 {ip}")
            print(f"注意: IP 已自动格式化为 {ip}")

    try:
        ip = socket.gethostbyname(ip)
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if not data:
            return "请求失败，返回值不符合 JSON 标准"
        elif data.get("status") == "fail":
            return f"请求失败，请检查 IP 是否正确\n错误信息: {data.get('message')}"

        ip_query_info = f"""请求返回
IP: {data.get("query")}
IP 属地: {data.get("continent")} {data.get("country")} {data.get("regionName")} {data.get("city")} {data.get("district")}
{f"运营商: {data.get('isp')}" if data.get('isp') else ''}
{f"组织名称: {data.get('org')}" if data.get('org') else ''}
{f"公司归属: {data.get('as')}" if data.get('as') else ''}
{f"DNS 查询信息: {data.get('reverse')}" if data.get('reverse') else ''}
{'该 IP 使用移动数据连接' if data.get('mobile') else ''}
{'该 IP 是代理服务器/虚拟专用网络服务器/洋葱路由出口地址' if data.get('proxy') else ''}
{'该 IP 是数据中心/网络托管商' if data.get('hosting') else ''}
"""
        return ip_query_info
    except Exception as e:
        return f"请求失败\n{str(e)}"
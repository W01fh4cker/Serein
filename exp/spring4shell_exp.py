#!/usr/bin/env python3
# coding=utf-8
import random
import requests
import threading
import tkinter as tk
from tkinter import scrolledtext
import tkinter.ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from urllib import parse as urlparse
default_headers = {
    'User-Agent': 'spring4shell-scan (https://github.com/fullhunt/spring4shell-scan)',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    'Accept': '*/*'
}

timeout = 4

def get_random_string(length=7):
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(length))

def parse_url(url):
    """
    Parses the URL.
    """

    # Url: https://example.com/login.jsp
    url = url.replace('#', '%23')
    url = url.replace(' ', '%20')

    if ('://' not in url):
        url = str("http://") + str(url)
    scheme = urlparse.urlparse(url).scheme

    # FilePath: /login.jsp
    file_path = urlparse.urlparse(url).path
    if (file_path == ''):
        file_path = '/'

    return({"scheme": scheme,
            "site": f"{scheme}://{urlparse.urlparse(url).netloc}",
            "host":  urlparse.urlparse(url).netloc.split(":")[0],
            "file_path": file_path})


def set_url_path(url, path="/"):
    url_parsed = parse_url(url)
    return f'{url_parsed["site"]}{path}'


def get_waf_bypass_payloads():
    random_string = get_random_string()
    payloads = []
    with open("payloads.txt", "r") as f:
        for payload in f.readlines():
            payload = payload.replace("{{random}}", random_string)
            payloads.append(payload.strip())
    return payloads


def verify_base_request(url, method):
    r = requests.request(url=url,
                         method=method,
                         headers=default_headers,
                         verify=False,
                         timeout=timeout)
    return r.status_code


def test_url_cve_2022_22965(url):
    main_payload = "class.module.classLoader[{{random}}]={{random}}"
    main_payload = main_payload.replace("{{random}}", get_random_string())
    payloads = []
    payloads.append(main_payload)
    # payloads.extend(get_waf_bypass_payloads())
    global payload_all
    for payload_all in payloads:
        parameter, value = payload_all.split("=")
        spring_text.insert(END, chars=f"[•] URL: {url} | PAYLOAD: {payload_all}\n")
        spring_text.see(END)
        try:
            r = requests.request(url=url,
                                 method="POST",
                                 headers=default_headers,
                                 verify=False,
                                 timeout=timeout,
                                 data={parameter: value})
            if r.status_code not in (200, 404) and verify_base_request(url, "POST") != r.status_code:
                return True
        except Exception as e:
            spring_text.insert(END, chars=f"EXCEPTION: {e}\n")
            spring_text.see(END)
        try:
            r = requests.request(url=url,
                                 method="GET",
                                 headers=default_headers,
                                 verify=False,
                                 timeout=timeout,
                                 params={parameter: value})
            if r.status_code not in (200, 404) and verify_base_request(url, "GET") != r.status_code:
                return True
        except Exception as e:
            spring_text.insert(END, chars=f"EXCEPTION: {e}\n")
            spring_text.see(END)
    return False

def spring_exp():
    urls = []
    with open("修正后的url.txt", "r") as f:
        for i in f.readlines():
            i = i.strip()
            if i == "" or i.startswith("#"):
                continue
            urls.append(i)

    vulnerable_hosts = []
    for url in urls:
        spring_text.insert(END, chars=f"[•] URL: {url}\n")
        spring_text.see(END)
        spring_text.insert(END, chars="[%] Checking for Spring4Shell RCE CVE-2022-22965.\n")
        spring_text.see(END)
        result = test_url_cve_2022_22965(url)
        if result:
            spring_text.insert(END, chars="[!!!] Target Affected (CVE-2022-22965)\n")
            spring_text.see(END)
            vulnerable_hosts.append(url)
            with open("存在漏洞的url.txt","a+") as f:
                f.write("url:" + url + " | PAYLOAD:" + payload_all + "\n")
        else:
            spring_text.insert(END, chars="[•] Target does not seem to be vulnerable.\n")
            spring_text.see(END)
    if len(vulnerable_hosts) == 0:
        spring_text.insert(END, chars="[•] No affected targets were discovered.\n")
        spring_text.see(END)
    else:
        spring_text.insert(END, chars=f"[!] Total Vulnerable Hosts: {len(vulnerable_hosts)}\n")
        spring_text.see(END)
        for host in vulnerable_hosts:
            spring_text.insert(END, chars=f"[!] {host}\n")
            spring_text.see(END)


def run_spring4shell():
    try:
        spring_exp()
    except KeyboardInterrupt:
        spring_text.insert(END, chars="\nKeyboardInterrupt Detected.\n")
        spring_text.see(END)
        spring_text.insert(END, chars="Exiting...\n")
        spring_text.see(END)
        exit(0)
def spring4shell_gui():
    spring = tk.Tk()
    spring.geometry("820x520")
    spring.title("Spring4shell一把梭")
    spring.resizable(0, 0)
    spring.iconbitmap('logo.ico')
    try:
        import requests.packages.urllib3
        requests.packages.urllib3.disable_warnings()
    except Exception:
        pass
    global spring_text
    spring_text = scrolledtext.ScrolledText(spring,width=107, height=28)
    spring_text.grid(row=4, columnspan=3, padx=20, pady=10)
    spring_text.insert(END, chars='[•] CVE-2022-22965 - Spring4Shell RCE Scanner\n')
    spring_text.see(END)
    t = threading.Thread(target=run_spring4shell)
    t.setDaemon(True)
    t.start()
    spring.mainloop()
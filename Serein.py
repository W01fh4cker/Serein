# -*- coding: utf-8 -*-
import configparser
import ctypes
import shodan
from exp.Thinkphp_5_0_x_gethell import *
from exp.CVE_2022_22954 import *
from exp.spring4shell_exp import *
from exp.hkv_rce import *
from exp.xrk_rce import *
from exp.CVE_2022_26134 import *
from exp.yync_rce import *
from exp.sonicwall_ssl_vpn import *
from exp.yyu8_testsql import *
from exp.CVE_2022_23337 import *
from exp.f5_big_ip import *
from exp.harbor import *
from exp.dvr_login_bypass import *
from exp.metabase_readfile import *
from exp.ruijie_admin_passwd_leak import *
from exp.magicflow_readfile import *
from exp.CVE_2022_8515 import *
from exp.CVE_2020_25078 import *
from exp.fumengyun_sql import *
from exp.VOS3000_readfile import *
from exp.kkFileView_readfile_CVE_2021_43734 import *
from exp.CVE_2022_29464 import *
from exp.SolarView_rce_CVE_2022_29303 import *
from exp.Fortigate_CVE_2018_13379 import *
from exp.Microsoft_proxyshell_cve_2021_34473 import *
from exp.Citrix_rce_cve_2019_19781 import *
from exp.ruijie_phpinfo_leak import *
from exp.Tenda_W15E_config_leak import *
from exp.Sapido_RCE import *
from exp.Zyxel_rce_CVE_2022_30525 import *
from exp.Apache_Hadoop_Yarn_RPC_RCE import *
from exp.wordpress_any_file_read_CVE_2022_1119 import *
from exp.VoIPmonitor_RCE_CVE_2021_30461 import *
from exp.clickhouse_unauthorized_visit import *
from exp.Weaver_HrmCareerApplyPerView_sql import *
from exp.E_Weaver_any_file_read import *
from exp.Rails_anyfile_read_cve_2019_5418 import *
from exp.Landray_oa_treexml_rce import *
from exp.xiaomi_wifi_anyfile_read_cve_2019_18371 import *
from exp.Dap_2020_anyfile_read_cve_2021_27250 import *
from exp.Franklin_Fueling_Systems_anyfile_read_cve_2021_46417 import *
from exp.FW_Eoffice_unauthorized import *
from exp.zabbix_sql import *
from exp.zabbix_auth_bypass import *
from exp.apache_spark_cve_2022_33891 import *
from exp.doccms_keyword_sql import *
from exp.fikker_weak_password import *
from exp.iceWarp_webClient_rce import *
from exp.node_red_anyfile_read import *
import json
import threading
from tkinter.messagebox import *
import ttkbootstrap as ttk
import urllib.parse
import urllib.request
import re
import threadpool
import urllib.parse
import urllib.request
import ssl
from urllib.error import HTTPError
import time
import tldextract
from fake_useragent import UserAgent
import os
import requests
import base64
window = tk.Tk()
window.title("Serein 【一款多nday批量利用工具】     Copyright © 2022     By: W01fh4cker     Blog: http://www.w01f.org     【*****************免责声明：软件仅限在所检测网站授权范围内使用，禁止使用该软件进行违法操作，否则后果自负！*****************】")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{width}x{height}')
# window.resizable(0, 0)
myappid = "W01f.Serein.1.0"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
window.wm_iconbitmap('logo.ico')
notebook = ttk.Notebook(window,bootstyle="info")
frameOne = ttk.Frame(window)
frameTwo = ttk.Frame(window)
frameSix = ttk.Frame(window)
frameThree = ttk.Frame(window)
frameFour = ttk.Frame(window)
frameFive = ttk.Frame(window)
def show_about():
    showinfo("关于作者", "一个乡村爱好者，一个旅行爱好者 。\nCodes build our world.\n微信：W01fh4cker\nGitHub：http://github.com/W01fh4cker\nmy blog：http://www.w01f.org")
def show_help():
    showinfo("遇到了问题？","请立即联系微信：W01fh4cker")
def getFofaConfig(section, key):
    config = configparser.ConfigParser()
    a = os.path.split(os.path.realpath(__file__))
    path = 'fofa配置.conf'
    config.read(path)
    return config.get(section, key)
def getHunterConfig(section, key):
    config = configparser.ConfigParser()
    a = os.path.split(os.path.realpath(__file__))
    path = 'hunter配置.conf'
    config.read(path)
    return config.get(section, key)
def getShodanConfig(section, key):
    config = configparser.ConfigParser()
    a = os.path.split(os.path.realpath(__file__))
    path = 'shodan配置.conf'
    config.read(path)
    return config.get(section, key)
def fofa_saveit_first():
    email = fofa_text1.get()
    key = fofa_text2.get()
    with open("fofa配置.conf","a+") as f:
        f.write(f"[data]\nemail={email}\nkey={key}")
        f.close()
    showinfo("保存成功！","请继续使用fofa搜索模块！下一次将自动读取，不再需要配置！")
    text3.insert(END,f"【+】保存成功！请继续使用fofa搜索模块！下一次将会自动读取，不再需要配置！您的email是：{email}；为保护您的隐私，api-key不会显示。\n")
    text3.see(END)
    fofa_info.destroy()
def fofa_saveit_twice():
    global email_r,key_r
    if not os.path.exists("fofa配置.conf"):
        fofa_saveit_first()
    else:
        email_r = getFofaConfig("data", "email")
        key_r = getFofaConfig("data", "key")
def fofa_info():
    global fofa_info,fofa_text1,fofa_text2,fofa_text3
    fofa_info = tk.Tk()
    fofa_info.title("fofa配置")
    fofa_info.geometry('230x100')
    fofa_info.resizable(0, 0)
    fofa_info.iconbitmap('logo.ico')
    fofa_email = tk.StringVar(fofa_info,value="填注册fofa的email")
    fofa_text1 = ttk.Entry(fofa_info, bootstyle="success", width=30, textvariable=fofa_email)
    fofa_text1.grid(row=0, column=1, padx=5, pady=5)
    fofa_key = tk.StringVar(fofa_info,value="填email对应的key")
    fofa_text2 = ttk.Entry(fofa_info, bootstyle="success", width=30, textvariable=fofa_key)
    fofa_text2.grid(row=1, column=1, padx=5, pady=5)
    button1 = ttk.Button(fofa_info, text="点击保存", command=fofa_saveit_twice, width=30, bootstyle="info")
    button1.grid(row=2, column=1, padx=5, pady=5)
    fofa_info.mainloop()
def hunter_saveit_first():
    hunter_apikey = hunter_text1.get()
    hunter_cooki = hunter_text2.get()
    with open("hunter配置.conf","a+") as f:
        f.write(f"[data]\nhunter_api_key={hunter_apikey}\nhunter_cookie={hunter_cooki}")
        f.close()
    showinfo("保存成功！","请继续使用hunter搜索模块！下一次将自动读取，不再需要配置！")
    text15.insert(END,f"【+】保存成功！请继续使用hunter搜索模块！下一次将会自动读取，不再需要配置！为保护您的隐私，鹰图平台的api-key和cookie不会显示。\n")
    text15.see(END)
    hunter_info.destroy()
def hunter_saveit_twice():
    global hunter_api_key,hunter_cookie
    if not os.path.exists("hunter配置.conf"):
        hunter_saveit_first()
    else:
        hunter_api_key = getHunterConfig("data", "hunter_api_key")
        hunter_cookie = getHunterConfig("data", "hunter_cookie")
def hunter_info():
    global hunter_info,hunter_text1,hunter_text1,hunter_text2
    hunter_info = tk.Tk()
    hunter_info.title("hunter配置")
    hunter_info.geometry('445x100')
    hunter_info.resizable(0, 0)
    hunter_info.iconbitmap('logo.ico')
    hunter_api_key = tk.StringVar(hunter_info,value="填写hunter的api-key")
    hunter_text1 = ttk.Entry(hunter_info, bootstyle="success", width=61, textvariable=hunter_api_key)
    hunter_text1.grid(row=0, column=0, padx=5, pady=5)
    hunter_cookie = tk.StringVar(hunter_info,value="填写经过base64加密后的hunter.qianxin.com的cookie\n(注意去掉末尾的等号)")
    hunter_text2 = ttk.Entry(hunter_info, bootstyle="success", width=61, textvariable=hunter_cookie)
    hunter_text2.grid(row=1, column=0, padx=5, pady=5)
    hunter_button = ttk.Button(hunter_info, text="点击保存（若需修改配置，请自行修改当前目录下的【hunter配置.conf】）", command=hunter_saveit_twice, width=61, bootstyle="info")
    hunter_button.grid(row=2, column=0, padx=5, pady=5)
    hunter_info.mainloop()
def shodan_saveit_first():
    key = shodan_key_text.get()
    with open("shodan配置.conf","a+") as f:
        f.write(f"[data]\nshodan_api_key={key}")
        f.close()
    showinfo("保存成功！","请继续使用shodan搜索模块！下一次将自动读取，不再需要配置！")
    shodan_log_text.insert(END,f"【+】保存成功！请继续使用shodan搜索模块！下一次将会自动读取，不再需要配置！\n")
    shodan_log_text.see(END)
    shodan_info.destroy()
def shodan_saveit_twice():
    global shodan_api_key
    if not os.path.exists("shodan配置.conf"):
        showerror("出错了","您还没有对shodan模块进行配置！请重新打开软件并点击右上角的【软件配置--shodan配置】配置。")
        shodan_info()
    else:
        shodan_api_key = getShodanConfig("data", "shodan_api_key")
def shodan_info():
    global shodan_info,shodan_key_text
    shodan_info = tk.Tk()
    shodan_info.title("shodan配置")
    shodan_info.geometry('250x70')
    shodan_info.resizable(0, 0)
    shodan_info.iconbitmap('logo.ico')
    shodan_key = tk.StringVar(shodan_info,value="填写您的的key")
    shodan_key_text = ttk.Entry(shodan_info, bootstyle="success", width=33, textvariable=shodan_key)
    shodan_key_text.grid(row=0, column=0, padx=5, pady=5)
    shodan_key_button = ttk.Button(shodan_info, text="点击保存", command=shodan_saveit_first, width=33, bootstyle="info")
    shodan_key_button.grid(row=1, column=0, padx=5, pady=5)
    shodan_info.mainloop()
def app_proxy():
    showinfo("这个还没实现呢~","已经列入我的To-do List里面啦！")
def clean_url():
    showwarning("谨慎操作！","点击此按钮会导致保存采集的url的文件全部清空！谨慎操作！")
    if os.path.exists("urls.txt"):
        os.remove("urls.txt")
    if os.path.exists("host.txt"):
        os.remove("host.txt")
    if os.path.exists("修正后的url.txt"):
        os.remove("修正后的url.txt")
    showinfo("清空成功","文件夹下的保存采集的url的文件已经全部清空。")
menubar = ttk.Menu(window)
loginmenu = ttk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='软件配置',menu=loginmenu)
loginmenu.add_command(label='fofa配置',command=fofa_info)
loginmenu.add_command(label='hunter配置',command=hunter_info)
loginmenu.add_command(label='shodan配置',command=shodan_info)
loginmenu.add_command(label='代理',command=app_proxy)
actionmenu = ttk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='操作',menu=actionmenu)
actionmenu.add_command(label='清空采集文件',command=clean_url)
aboutmenu = ttk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='关于与帮助',menu=aboutmenu)
aboutmenu.add_command(label='关于',command=show_about)
aboutmenu.add_command(label='帮助',command=show_help)
exitmenu = ttk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='退出',menu=exitmenu)
exitmenu.add_command(label='点我退出',command=window.destroy)
window.config(menu=menubar)
def fofa():
    fofa_saveit_twice()
    try:
        fofa_yf = text1.get()
        fofa_ts = text2.get()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
        }
        url = f"https://fofa.info/api/v1/search/all?email={email_r}&key={key_r}&qbase64={fofa_yf}&size={fofa_ts}".format()
        resp = requests.get(url=url, headers=headers)
        if resp.status_code == -1:
            showerror('出错了！', '账号信息有误。请检查您的email和key是否填写正确！')
            text3.insert(END, chars="【×】出错了！账号信息有误,请检查您的email和key是否填写正确！\n")
            text3.see(END)
        elif resp.status_code == -4:
            showerror('出错了！', '请求参数有误')
            text3.insert(END, chars="【×】出错了！请求参数有误,请检查您的查询语句和查询条数是否填写正确（尤其是后者）！\n")
            text3.see(END)
        elif resp.status_code == -5:
            showerror('出错了！', '系统错误，请联系微信W01fh4cker！')
            text3.insert(END, chars="【×】出错了！系统错误，请联系微信W01fh4cker！\n")
            text3.see(END)
        else:
            res = json.loads((resp.content).decode('utf-8'))
            xlen = len(res["results"])
            showinfo('开始采集', '程序开始采集url，请耐心等待，不要关闭程序。')
            text3.insert(END, chars="【+】开始采集！程序开始采集url，请耐心等待，不要关闭程序。\n")
            text3.see(END)
            for i in range(xlen):
                with open("urls.txt", "a+") as f:
                    url = res["results"][i][0]
                    f.write(url + "\n")
            for j in range(xlen):
                with open("host.txt", "a+") as f:
                    host = res["results"][j][1]
                    f.write(host + "\n")
            with open("urls.txt", 'r') as f:
                ln = f.readlines()
                for j in ln:
                    url = j.strip()
                    if url[:7] == 'http://' or url[:8] == 'https://':
                        with open("修正后的url.txt", 'a+') as f:
                            text3.insert(END, chars=url + "\n")
                            text3.see(END)
                            f.write(url + '\n')
                    else:
                        newurl = 'http://' + str(url)
                        with open("修正后的url.txt", 'a+') as f:
                            text3.insert(END, chars=newurl + "\n")
                            text3.see(END)
                            f.write(newurl + '\n')
            showinfo('保存成功', '文件就在您的当前文件夹下，urls.txt是采集的所有url合集，修正后的url.txt里的url是全部加了http/https头的。')
            text3.insert(END, chars="【+】保存成功！文件就在您的当前文件夹下，【urls.txt】是采集的所有url合集，【修正后的url.txt】里的url是全部加了http/https头的。\n")
            text3.see(END)
            f.close()
    except Exception as error:
        showerror("出错了！","请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）或是否使用了代理软件；\n若确实没问题，请立即联系微信W01fh4cker！")
        text3.insert(END, chars="【×】出错了！请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）或是否使用了代理软件；若确实没问题，请立即联系微信W01fh4cker！\n")
        text3.see(END)
def thread_fofa():
    t = threading.Thread(target=fofa)
    t.setDaemon(True)
    t.start()
def hunter_query():
    showinfo('开始采集', '程序开始采集url，中间会可能出现卡顿现象，请耐心等待，不要关闭程序。')
    text15.insert(END, chars="【√】程序开始采集url，中间会可能出现卡顿现象，请耐心等待，不要关闭程序。\n")
    text15.see(END)
    hunter_saveit_twice()
    global i
    global number
    number = 1
    i = 0
    api_key = hunter_api_key
    query_sentence = text8.get()
    hunter_ts = text9.get()
    hunter_ts = int(hunter_ts)
    hunter_pagenum_to_query = hunter_ts / 100
    if hunter_pagenum_to_query < 1:
        hunter_num = 2
        page_size = hunter_ts
    else:
        hunter_num = hunter_pagenum_to_query + 1
        page_size = 100
    hunter_num = int(hunter_num)
    hunter_asset_type = text11.get()
    hunter_start_time = text13.get()
    hunter_end_time = text14.get()
    hunter_status_code = text12.get()
    try:
        for j in range(1,hunter_num):
            url = 'https://hunter.qianxin.com/openApi/search?api-key=' + str(api_key) + '&search=' + str(
                query_sentence) + '&page=' + str(j) + '&page_size=' + str(page_size) + '&is_web=' + str(
                hunter_asset_type) + '&start_time=' + str(hunter_start_time) + '&end_time=' + str(hunter_end_time) + '&status_code=' + str(hunter_status_code)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
                'Cookie': hunter_cookie
            }
            resp = requests.get(url=url, headers=headers)
            global res
            res = json.loads((resp.content).decode('utf-8'))
            global first_url
            hunter_res_num = res["data"]["total"]
            if hunter_res_num == "0":
                text15.insert(END, chars=f"【*】当前共查询到0条数据，请检查您base64加密前的语句并重启软件查询\n")
                text15.see(END)
            else:
                pass
            for i in range(len(res["data"]["arr"])):
                if (hunter_res_num == 0):
                    text15.insert(END, chars="【*】当前共查询到0条数据。\n")
                    text15.see(END)
                    break
                else:
                    try:
                        its_ip = res["data"]["arr"][i]["ip"]
                        its_url = res["data"]["arr"][i]["url"]
                        if its_ip == "违规数据无法查看" or its_url == "违规数据无法查看":
                            pass
                        else:
                            with open("修正后的url.txt","a+") as m:
                                m.write(its_url + "\n")
                            with open("host.txt","a+") as m:
                                m.write(its_ip + "\n")
                            if its_ip is None:
                                pass
                            else:
                                first_url = str(its_url)
                    except:
                        i = i + 1
                    time.sleep(0.2)
            time.sleep(0.2)
            if j == hunter_pagenum_to_query:
                text15.insert(END, chars=f"【*】当前共查询到{hunter_res_num}条数据！\n")
                text15.see(END)
                consume_quota = res["data"]["consume_quota"]
                rest_quota = res["data"]["rest_quota"]
                text17.insert(END,"【+】" + consume_quota + "\n【+】" + rest_quota + "\n")
                showinfo('保存成功', '文件就在您的当前文件夹下，urls.txt是采集的所有url合集，修正后的url.txt里的url是全部加了http/https头的。')
                text15.insert(END, chars="【+】保存成功！文件就在您的当前文件夹下，【urls.txt】是采集的所有url合集，【修正后的url.txt】里的url是全部加了http/https头的。\n")
                text15.see(END)
            else:
                pass
    except Exception as hunter_error:
        showerror("出错了！","报错内容："+ str(hunter_error) + "\n，如果您无法解决，请立即联系微信W01fh4cker！")
        text15.insert(END, chars="【×】出错了！报错内容："+ str(hunter_error) + "，如果您无法解决，请立即联系微信W01fh4cker！")
        text15.see(END)
def check_code():
    if (res["code"] == 200):
        pass
    elif (res["code"] == 401):
        text15.insert(END,"\n【×】起始/结束时间参数格式错误，格式应为2021-07-17 00:00:00\n")
        text15.see(END)
    elif (res["code"] == 401):
        text15.insert(END,"\n【×】无权限，请检查您的api-key和cookie是否填写正确！\n")
        text15.see(END)
    else:
        text15.insert(END,"\n【×】其他错误，请立即联系微信W01fh4cker\n")
        text15.see(END)
def save_url():
    with open("修正后的url.txt", 'a+', encoding='utf-8') as f:
        f.write(first_url + '\n')
def check_url_format():
    with open("修正后的url.txt",'r') as f:
        ln = f.readlines()
        for j in ln:
            url = j.strip()
            if url[:7] == 'http://' or url[:8] == 'https://':
                pass
            else:
                url = 'http://' + str(url)
                with open("修正后的url.txt",'w') as h:
                    h.write(url + '\n')
def hunter():
    hunter_query()
    check_code()
    save_url()
    check_url_format()
def shodan_search(key):
    shodan_saveit_twice()
    showinfo('开始采集', '程序开始采集url，请耐心等待，不要关闭程序。')
    shodan_log_text.insert(END, "【√】程序开始采集url，请耐心等待，不要关闭程序。\n")
    shodan_log_text.see(END)
    SHODAN_API_KEY = key
    api = shodan.Shodan(SHODAN_API_KEY)
    api_info = api.info()
    api_info_json = json.dumps(api_info, sort_keys=True, indent=4, separators=(',', ':'))
    shodan_log_text.insert(END, chars=str(api_info_json) + "\n")
    shodan_log_text.see(END)
    try:
        shodan_search_sentence = shodan_yf_text.get()
        shodan_number = shodan_ts_text.get()
        shodan_number = int(shodan_number)
        page_number = shodan_number / 100
        pagenumber = page_number + 1
        pagenumber = int(pagenumber)
        for j in range(1, pagenumber):
            results = api.search(shodan_search_sentence, page=j)
            for i in range(0,100):
                with open('修正后的url.txt', 'a+') as f:
                    ip_str = results['matches'][i]['ip_str']
                    port = results['matches'][i]['port']
                    if port is not None:
                        shodan_got_url1 = "https://" + str(ip_str) + ":" + str(port) + '\n'
                        f.write(shodan_got_url1)
                        shodan_log_text.insert(END, chars=shodan_got_url1)
                        shodan_log_text.see(END)
                    else:
                        shodan_got_url2 = "https://" + str(ip_str) + '\n'
                        f.write(shodan_got_url2)
                        shodan_log_text.insert(END, chars=shodan_got_url2)
                        shodan_log_text.see(END)
        showinfo('保存成功', '文件就在您的当前文件夹下的【修正后的url.txt】里。')
        shodan_log_text.insert(END, chars="【+】保存成功！文件就在您的当前文件夹下的【修正后的url.txt】里。\n")
        shodan_log_text.see(END)
    except Exception as e:
        showerror("出错了","请检查您的账号是否有调用API查询该语句的权限！")
        shodan_log_text.insert(END,"【×】出错了，请检查您的账号是否有调用API查询该语句的权限！报错内容："+ str(e) + "\n")
        shodan_log_text.see(END)
def thread_shodan():
    SHODAN_API_KEY = getShodanConfig("data","shodan_api_key")
    max_thread_num = 100
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    future = executor.submit(shodan_search, SHODAN_API_KEY)
group1 = ttk.LabelFrame(frameOne, text="fofa搜索模块",bootstyle="info")
group1.grid(row=0,column=0,padx=10, pady=10)
notebook.add(frameOne, text='fofa搜索')
fofa_yf = tk.StringVar(value="填写base64后的fofa语法")
text1 = ttk.Entry(group1, bootstyle="success", width=50, textvariable=fofa_yf)
text1.grid(row=0, column=0, padx=5, pady=5)
fofa_ts = tk.StringVar(value="填写查询条数(根据自己的会员情况填写)")
text2 = ttk.Entry(group1, bootstyle="success", width=35, textvariable=fofa_ts)
text2.grid(row=0, column=1, padx=5, pady=5)
text3 = scrolledtext.ScrolledText(group1, width=115, height=38)
text3.grid(row=1, columnspan=3, padx=10, pady=10)
button1 = ttk.Button(group1, text="点击查询", command=thread_fofa, width=20, bootstyle="info")
button1.grid(row=0, column=2, padx=5, pady=5)
group2 = ttk.LabelFrame(frameOne, text="fofa查询语法参考",bootstyle="info")
group2.grid(row=0,column=1,padx=10, pady=10)
text5 = scrolledtext.ScrolledText(group2, width=82, height=41)
text5.insert(END,r"""直接输入查询语句，将从标题，html内容，http头信息，url字段中搜索

• title="abc" 从标题中搜索abc。例：标题中有北京的网站

• header="abc" 从http头中搜索abc。例：jboss服务器

• body="abc" 从html正文中搜索abc。例：正文包含Hacked by

• domain="qq.com" 搜索根域名带有qq.com的网站。例： 根域名是qq.com的网站

• host=".gov.cn" 从url中搜索.gov.cn,注意搜索要用host作为名称。例： 政府网站, 教育网站

• port="443" 查找对应443端口的资产。例： 查找对应443端口的资产

• ip="1.1.1.1" 从ip中搜索包含1.1.1.1的网站,注意搜索要用ip作为名称。例： 查询IP为220.181.111.1的网站; 如果想要查询网段，可以是： ip="220.181.111.1/24"，例如查询IP为220.181.111.1的C网段资产

• protocol="https" 搜索指定协议类型(在开启端口扫描的情况下有效)。例： 查询https协议资产

• city="Hangzhou" 搜索指定城市的资产。例： 搜索指定城市的资产

• region="Zhejiang" 搜索指定行政区的资产。例： 搜索指定行政区的资产

• country="CN" 搜索指定国家(编码)的资产。例： 搜索指定国家(编码)的资产

• cert="google" 搜索证书(https或者imaps等)中带有google的资产。例： 搜索证书(https或者imaps等)中带有google的资产

• banner=users && protocol=ftp 搜索FTP协议中带有users文本的资产。例： 搜索FTP协议中带有users文本的资产

• type=service 搜索所有协议资产，支持subdomain和service两种。例： 搜索所有协议资产

• os=windows 搜索Windows资产。例： 搜索Windows资产

• server=="Microsoft-IIS/7.5" 搜索IIS 7.5服务器。例： 搜索IIS 7.5服务器

• app="海康威视-视频监控" 搜索海康威视设备，更多app规则。例： 搜索海康威视设备

• after="2017" && before="2017-10-01" 时间范围段搜索。例： 时间范围段搜索，注意： after是大于并且等于，before是小于，这里after="2017" 就是日期大于并且等于 2017-01-01 的数据，而 before="2017-10-01" 则是小于 2017-10-01 的数据

• asn="19551" 搜索指定asn的资产。例： 搜索指定asn的资产

• org="Amazon.com, Inc." 搜索指定org(组织)的资产。例： 搜索指定org(组织)的资产

• base_protocol="udp" 搜索指定udp协议的资产。例： 搜索指定udp协议的资产

• is_ipv6=true 搜索ipv6的资产,只接受true和false。例： 搜索ipv6的资产

• is_domain=true 搜索域名的资产,只接受true和false。例： 搜索域名的资产

• ip_ports="80,443" 或者 ports="80,443" 搜索同时开放80和443端口的ip资产(以ip为单位的资产数据)。例： 搜索同时开放80和443端口的ip

• ip_country="CN" 搜索中国的ip资产(以ip为单位的资产数据)。例： 搜索中国的ip资产

• ip_region="Zhejiang" 搜索指定行政区的ip资产(以ip为单位的资产数据)。例： 搜索指定行政区的资产

• ip_city="Hangzhou" 搜索指定城市的ip资产(以ip为单位的资产数据)。例： 搜索指定城市的资产

• ip_after="2019-01-01" 搜索2019-01-01以后的ip资产(以ip为单位的资产数据)。例： 搜索2019-01-01以后的ip资产

• ip_before="2019-01-01" 搜索2019-01-01以前的ip资产(以ip为单位的资产数据)。例： 搜索2019-01-01以前的ip资产

 

高级搜索：可以使用括号 和 && || !=等符号，如

title="powered by" && title!=discuz

title!="powered by" && body=discuz

( body="content=\"WordPress" || (header="X-Pingback" && header="/xmlrpc.php" && body="/wp-includes/") ) && host="gov.cn"

新增==完全匹配的符号，可以加快搜索速度，比如查找qq.com所有host，可以是domain=="qq.com"

关于建站软件的搜索语法请参考：组件列表

 

注意事项:

* 如果查询表达式有多个与或关系，尽量在外面用（）包含起来

剩下来，就是发挥你想象力的时候了 ；）""")
text5.config(state='disabled')
text5.grid(row=0, column=0, padx=10, pady=10)
notebook.add(frameFive, text='hunter搜索')
group9 = ttk.LabelFrame(frameFive, text="hunter搜索模块",bootstyle="info")
group9.grid(row=0,column=0,padx=5, pady=5)
hunter_query_sentence = tk.StringVar(group9, value="填写加密后的hunter语句")
text8 = ttk.Entry(group9, bootstyle="success", width=45, textvariable=hunter_query_sentence)
text8.grid(row=0, column=0, padx=5, pady=5)
hunter_pagenum_to_query = tk.StringVar(group9, value="填写想要查询数据的条数")
text9 = ttk.Entry(group9, bootstyle="success", width=35, textvariable=hunter_pagenum_to_query)
text9.grid(row=0, column=1, padx=5, pady=5)
hunter_asset_type = tk.StringVar(group9, value="填写资产类型，1代表”web资产“，2代表”非web资产“，3代表”全部“")
text11 = ttk.Entry(group9, bootstyle="success", width=91, textvariable=hunter_asset_type)
text11.grid(row=0, column=2,columnspan=2,padx=5, pady=5)
hunter_status_code_select = tk.StringVar(group9, value="状态码列表，以逗号分隔，如”200“")
text12 = ttk.Entry(group9, bootstyle="success", width=45, textvariable=hunter_status_code_select)
text12.grid(row=1, column=0, padx=5, pady=5)
hunter_start_time = tk.StringVar(group9, value="开始时间，格式为2021-07-17 00:00:00")
text13 = ttk.Entry(group9, bootstyle="success", width=35, textvariable=hunter_start_time)
text13.grid(row=1, column=1, padx=5, pady=5)
hunter_end_time = tk.StringVar(group9, value="结束时间，格式为2022-07-17 00:00:00")
text14 = ttk.Entry(group9, bootstyle="success", width=35, textvariable=hunter_end_time)
text14.grid(row=1, column=2, padx=5, pady=5)
hunter_query_button = ttk.Button(group9,text="点击查询",command=hunter,width=51,bootstyle="primary")
hunter_query_button.grid(row=1,column=3,columnspan=2,padx=5,pady=5)
text15 = scrolledtext.ScrolledText(group9,width=178, height=15)
text15.grid(row=2,column=0,columnspan=4,padx=5,pady=5)
group10 = ttk.LabelFrame(frameFive, text="hunter查询语法参考",bootstyle="info")
group10.grid(row=1,column=0,padx=5, pady=5)
text16 = scrolledtext.ScrolledText(group10,width=178, height=19)
text16.grid(row=0,column=0,padx=5,pady=5)
text16.insert(END,"【+】语法查询请参考文档：https://hunter.qianxin.com/home/helpCenter?r=2-2\n")
text16.see(END)
group11 = ttk.LabelFrame(frameFive, text="hunter积分明细",bootstyle="info")
group11.grid(row=0,rowspan=2,column=1,padx=5, pady=5)
text17 = scrolledtext.ScrolledText(group11,width=23, height=42)
text17.grid(row=0,column=0,padx=5,pady=5)
notebook.add(frameSix, text='Shodan搜索')
shodan_search_group = ttk.LabelFrame(frameSix, text="Shodan搜索模块",bootstyle="info")
shodan_log_text = scrolledtext.ScrolledText(shodan_search_group,width=112, height=40)
shodan_log_text.grid(row=1,columnspan=3,padx=5,pady=5)
shodan_yf = tk.StringVar(value="直接填写shodan语法（不需要加密）")
shodan_yf_text = ttk.Entry(shodan_search_group, bootstyle="success", width=50, textvariable=shodan_yf)
shodan_yf_text.grid(row=0, column=0, padx=5, pady=5)
shodan_ts = tk.StringVar(value="填写查询条数(根据自己的会员情况填写)")
shodan_ts_text = ttk.Entry(shodan_search_group, bootstyle="success", width=35, textvariable=shodan_ts)
shodan_ts_text.grid(row=0,column=1,padx=5, pady=5)
shodan_search_button = ttk.Button(shodan_search_group, text="点击查询", command=thread_shodan, width=20, bootstyle="info")
shodan_search_button.grid(row=0, column=2, padx=5, pady=5)
shodan_search_group.grid(row=0,column=0,padx=5, pady=5)
shodan_yufa_group = ttk.LabelFrame(frameSix, text="Shodan语法参考",bootstyle="info")
shodan_yufa_group.grid(row=0,column=1,padx=5, pady=5)
shodan_yufa_text = scrolledtext.ScrolledText(shodan_yufa_group,width=89, height=42)
shodan_yufa_text.grid(row=1,column=4,padx=5,pady=5)
shodan_yufa_text.insert(END,r"""------限定国家和城市
限定国家country:"CN"
限定城市city:"ShangHai"

------限定主机名或域名
hostname:.org
hostname:"google"
hostname:baidu.com

------限定组织或机构
org:"alibaba"

------限定系统OS版本
os:"Windows Server 2008 R2"
os:"Windows 7 or 8"
os:"Linux 2.6.x"

------限定端口
port:22
port:80

------指定网段
net:"59.56.19.0/24"

------指定使用的软件或产品
product:"Apache httpd"
product:"nginx"
product:"Microsoft IIS httpd"
product:"mysql"

------指定CVE漏洞编号
vuln:"CVE-2014-0723"

------指定网页内容
http.html:"hello world"

------指定网页标题
http.title:"hello"

------指定返回响应码
http.status:200

------指定返回中的server类型
http.server:Apache/2.4.7
http.server:PHP

------指定地理位置
geo:"31.25,121.44"

------指定ISP供应商
isp:"China Telecom"
""")
shodan_yufa_text.see(END)
notebook.add(frameTwo, text='nday利用集合')
group3 = ttk.LabelFrame(frameTwo, text="nday一键利用模块",bootstyle="info")
group3.grid(row=0,column=0,padx=10, pady=10)
button2 = ttk.Button(group3,text="Spring4shell一把梭",command=spring4shell_gui,width=20,bootstyle="primary")
button2.grid(row=0,column=0,padx=5,pady=5)
button3 = ttk.Button(group3,text="海康威视RCE一把梭",command=hkv_rce_gui,width=20,bootstyle="primary")
button3.grid(row=0,column=1,padx=5,pady=5)
button4 = ttk.Button(group3,text="向日葵RCE一把梭",command=xrk_rce_gui,width=20,bootstyle="primary")
button4.grid(row=0,column=2,padx=5,pady=5)
button5 = ttk.Button(group3,text="ConfulenceONGL RCE一把梭",command=confluence_gui,width=45,bootstyle="info")
button5.grid(row=1,columnspan=2,padx=5,pady=5)
button6 = ttk.Button(group3,text="用友NC RCE一把梭",command=yync_rce_gui,width=20,bootstyle="primary")
button6.grid(row=0,column=3,padx=5,pady=5)
button7 = ttk.Button(group3,text="SonicWall SSL-VPN RCE一把梭",command=sonicwall_ssl_vpn_gui,width=45,bootstyle="info")
button7.grid(row=1,column=2,columnspan=2,padx=5,pady=5)
button8 = ttk.Button(group3,text="用友 U8 OA test.jsp SQL注入一把梭",command=yyu8_testsql_gui,width=45,bootstyle="primary")
button8.grid(row=0,column=4,padx=5,pady=5)
button9 = ttk.Button(group3,text="Dede v5.7.87 SQL注入一把梭",command=dedesql_gui,width=45,bootstyle="info")
button9.grid(row=1,column=4,columnspan=2,padx=5,pady=5)
button10 = ttk.Button(group3,text="F5 BIG-IP 远程代码执行漏洞一把梭",command=f5_big_ip_gui,width=45,bootstyle="primary")
button10.grid(row=2,columnspan=2,padx=5,pady=5)
button11 = ttk.Button(group3,text="Harbor 未授权创建管理员漏洞一把梭",command=harbor_gui,width=45,bootstyle="primary")
button11.grid(row=2,column=2,columnspan=2,padx=5,pady=5)
button12 = ttk.Button(group3,text="DVR 登录绕过漏洞(CVE-2018-9995)一把梭",command=dvr_login_bypass_gui,width=45,bootstyle="primary")
button12.grid(row=2,column=4,columnspan=2,padx=5,pady=5)
button13 = ttk.Button(group3,text="MetaBase任意文件读取漏洞(CVE-2021-41277)一把梭",command=metabase_readfile_gui,width=45,bootstyle="primary")
button13.grid(row=3,column=0,columnspan=2,padx=5,pady=5)
button13.grid(row=3,column=0,columnspan=2,padx=5,pady=5)
button14 = ttk.Button(group3,text="VMware服务端模板注入漏洞(CVE-2022-22954)一把梭",command=vmware_one_access_ssti_gui,width=45,bootstyle="primary")
button14.grid(row=3,column=2,columnspan=2,padx=5,pady=5)
button15 = ttk.Button(group3,text="Thinkphp 5.0.x通杀gethell一把梭",command=Thinkphp_5_0_x_gethell_gui,width=45,bootstyle="primary")
button15.grid(row=3,column=4,columnspan=2,padx=5,pady=5)
button16 = ttk.Button(group3,text="锐捷 EG易网关管理员账号密码泄露一把梭",command=ruijie_admin_passwd_leak_gui,width=45,bootstyle="info")
button16.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
button17 = ttk.Button(group3,text="MagicFlow防火墙网关任意文件读取一把梭",command=magicflow_readfile_gui,width=45,bootstyle="info")
button17.grid(row=4,column=2,columnspan=2,padx=5,pady=5)
button18 = ttk.Button(group3,text="DrayTek企业网络设备 远程命令执行一把梭",command=vigor_rce_gui,width=45,bootstyle="info")
button18.grid(row=4,column=4,columnspan=2,padx=5,pady=5)
button19 = ttk.Button(group3,text="D-Link DCS系列监控账号密码信息泄露一把梭",command=dcs_admin_passwd_leak_gui,width=45,bootstyle="success")
button19.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
button20 = ttk.Button(group3,text="孚盟云 AjaxMethod.ashx SQL注入一把梭",command=fumengyun_sql_gui,width=45,bootstyle="success")
button20.grid(row=5,column=2,columnspan=2,padx=5,pady=5)
button21 = ttk.Button(group3,text="昆石网络虚拟运营支撑系统任意文件读取漏洞一把梭",command=VOS3000_redfile_gui,width=45,bootstyle="success")
button21.grid(row=5,column=4,columnspan=2,padx=5,pady=5)
button22 = ttk.Button(group3,text="kkFileView getCorsFile 任意文件读取漏洞一把梭",command=kkFileView_readfile_CVE_2021_43734_gui,width=45,bootstyle="success")
button22.grid(row=6,column=0,columnspan=2,padx=5,pady=5)
button23 = ttk.Button(group3,text="WSO2远程命令执行漏洞(CVE-2022-29464)一把梭",command=CVE_2022_29464_gui,width=45,bootstyle="success")
button23.grid(row=6,column=2,columnspan=2,padx=5,pady=5)
button24 = ttk.Button(group3,text="SolarView RCE漏洞(CVE-2022-29303)一把梭",command=SolarView_rce_CVE_2022_29303_gui,width=45,bootstyle="success")
button24.grid(row=6,column=4,columnspan=2,padx=5,pady=5)
button25 = ttk.Button(group3,text="Fortinet任意文件读取漏洞(CVE-2018-13379)一把梭",command=Fortigate_CVE_2018_13379_gui,width=45,bootstyle="warning")
button25.grid(row=7,column=0,columnspan=2,padx=5,pady=5)
button26 = ttk.Button(group3,text="Microsoft Exchange RCE(CVE-2021-34473)一把梭",command=Microsoft_proxyshell_cve_2021_34473_gui,width=45,bootstyle="warning")
button26.grid(row=7,column=2,columnspan=2,padx=5,pady=5)
button27 = ttk.Button(group3,text="Citrix远程代码执行漏洞(CVE_2019_19781)一把梭",command=Citrix_rce_cve_2019_19781_gui,width=45,bootstyle="warning")
button27.grid(row=7,column=4,columnspan=2,padx=5,pady=5)
button28 = ttk.Button(group3,text="锐捷EG易网关 phpinfo.view.php 信息泄露漏洞一把梭",command=ruijie_phpinfo_leak_gui,width=45,bootstyle="warning")
button28.grid(row=8,column=0,columnspan=2,padx=5,pady=5)
button29 = ttk.Button(group3,text="Tenda W15E企业级路由器配置文件泄漏漏洞一把梭",command=Tenda_W15E_config_leak_gui,width=45,bootstyle="warning")
button29.grid(row=8,column=2,columnspan=2,padx=5,pady=5)
button30 = ttk.Button(group3,text="Sapido 多款路由器 远程命令执行漏洞一把梭",command=Sapido_RCE_gui,width=45,bootstyle="warning")
button30.grid(row=8,column=4,columnspan=2,padx=5,pady=5)
button31 = ttk.Button(group3,text="Zyxel USG 远程命令执行漏洞一把梭",command=Zyxel_rce_CVE_2022_30525_gui,width=45,bootstyle="primary")
button31.grid(row=9,column=0,columnspan=2,padx=5,pady=5)
button32 = ttk.Button(group3,text="Apache Hadoop Yarn RPC 远程命令执行漏洞一把梭",command=Apache_Hadoop_Yarn_RPC_RCE_gui,width=45,bootstyle="primary")
button32.grid(row=9,column=2,columnspan=2,padx=5,pady=5)
button33 = ttk.Button(group3,text="WordPress任意文件读取漏洞(CVE-2022-1119)一把梭",command=wordpress_any_file_read_CVE_2022_1119_gui,width=45,bootstyle="primary")
button33.grid(row=9,column=4,columnspan=2,padx=5,pady=5)
button34 = ttk.Button(group3,text="VoIPmonitor 远程命令执行漏洞(CVE-2021-30461)一把梭",command=VoIPmonitor_RCE_CVE_2021_30461_gui,width=45,bootstyle="primary")
button34.grid(row=10,column=0,columnspan=2,padx=5,pady=5)
button35 = ttk.Button(group3,text="ClickHouse API 数据库接口未授权访问漏洞一把梭",command=clickhouse_unauthorized_visit_gui,width=45,bootstyle="primary")
button35.grid(row=10,column=2,columnspan=2,padx=5,pady=5)
button36 = ttk.Button(group3,text="泛微OA HrmCareerApplyPerView.jsp SQL注入漏洞一把梭",command=Weaver_HrmCareerApplyPerView_sql_gui,width=45,bootstyle="primary")
button36.grid(row=10,column=4,columnspan=2,padx=5,pady=5)
button37 = ttk.Button(group3,text="泛微OA HrmCareerApplyPerView.jsp SQL注入漏洞一把梭",command=E_Weaver_any_file_read_gui,width=45,bootstyle="success")
button37.grid(row=11,column=0,columnspan=2,padx=5,pady=5)
button38 = ttk.Button(group3,text="Rails Accept 任意文件读取漏洞(CVE-2019-5418)一把梭",command=Rails_anyfile_read_cve_2019_5418_gui,width=45,bootstyle="success")
button38.grid(row=11,column=2,columnspan=2,padx=5,pady=5)
button39 = ttk.Button(group3,text="蓝凌OA treexml.tmpl 远程命令执行漏洞一把梭",command=Landray_oa_treexml_rce_gui,width=45,bootstyle="success")
button39.grid(row=11,column=4,columnspan=2,padx=5,pady=5)
button40 = ttk.Button(group3,text="小米路由器任意文件读取漏洞(CVE-2019-18371)一把梭",command=xiaomi_wifi_anyfile_read_cve_2019_18371_gui,width=45,bootstyle="warning")
button40.grid(row=12,column=0,columnspan=2,padx=5,pady=5)
button41 = ttk.Button(group3,text="D-LINK DAP-2020任意文件读取漏洞(CVE-2021-27250)一把梭",command=Dap_2020_anyfile_read_cve_2021_27250_gui,width=45,bootstyle="warning")
button41.grid(row=12,column=2,columnspan=2,padx=5,pady=5)
button42 = ttk.Button(group3,text="Franklin任意文件读取漏洞(CVE-2021-46417)一把梭",command=Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_gui,width=45,bootstyle="warning")
button42.grid(row=12,column=4,columnspan=2,padx=5,pady=5)
button43 = ttk.Button(group3,text="泛微Eoffice未授权访问一把梭",command=fw_unauthorized_gui,width=45,bootstyle="warning")
button43.grid(row=13,column=0,columnspan=2,padx=5,pady=5)
button44 = ttk.Button(group3,text="Zabbix_popup.php注入漏洞一把梭",command=zabbix_sql_gui,width=45,bootstyle="warning")
button44.grid(row=13,column=2,columnspan=2,padx=5,pady=5)
button45 = ttk.Button(group3,text="Zabbix4.4_未授权访问一把梭",command=zabbix_auth_gui,width=45,bootstyle="warning")
button45.grid(row=13,column=4,columnspan=2,padx=5,pady=5)
button46 = ttk.Button(group3,text="Apache Spark RCE漏洞(CVE-2022-33891)一把梭",command=apache_spark_cve_2022_33891_gui,width=45,bootstyle="primary")
button46.grid(row=14,column=0,columnspan=2,padx=5,pady=5)
button46 = ttk.Button(group3,text="DocCMS keyword SQL注入漏洞一把梭",command=doccms_keyword_sql_gui,width=45,bootstyle="primary")
button46.grid(row=14,column=2,columnspan=2,padx=5,pady=5)
button47 = ttk.Button(group3,text="Fikker 管理平台弱口令漏洞一把梭",command=fikker_weak_password_gui,width=45,bootstyle="primary")
button47.grid(row=14,column=4,columnspan=2,padx=5,pady=5)
button48 = ttk.Button(group3,text="IceWarp WebClient远程命令执行漏洞一把梭",command=iceWarp_webClient_rce_gui,width=45,bootstyle="primary")
button48.grid(row=15,column=0,columnspan=2,padx=5,pady=5)
button49 = ttk.Button(group3,text="Node-RED ui_base 任意文件读取漏洞一把梭",command=node_red_anyfile_read_gui,width=45,bootstyle="primary")
button49.grid(row=15,column=2,columnspan=2,padx=5,pady=5)
notebook.add(frameThree, text='IP反查域名+权重查询')
def ip138_chaxun(ip, ua):
    ip138_headers = {
        'Host': 'site.ip138.com',
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://site.ip138.com/'
    }
    ip138_url = 'https://site.ip138.com/' + str(ip) + '/'
    try:
        ip138_res = requests.get(url=ip138_url, headers=ip138_headers, timeout=2).text
        if '<li>暂无结果</li>' not in ip138_res:
            result_site = re.findall(r"""</span><a href="/(.*?)/" target="_blank">""", ip138_res)
            return result_site
    except:
        pass
def aizhan_chaxun(ip, ua):
    aizhan_headers = {

        'Host': 'dns.aizhan.com',
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://dns.aizhan.com/'}
    aizhan_url = 'https://dns.aizhan.com/' + str(ip) + '/'
    try:
        aizhan_r = requests.get(url=aizhan_url, headers=aizhan_headers, timeout=2).text
        aizhan_nums = re.findall(r'''<span class="red">(.*?)</span>''', aizhan_r)
        if int(aizhan_nums[0]) > 0:
            aizhan_domains = re.findall(r'''rel="nofollow" target="_blank">(.*?)</a>''', aizhan_r)
            return aizhan_domains
    except:
        pass
def catch_result(i):
    ua_header = UserAgent()
    i = i.strip()
    try:
        ip = i.split(':')[1].split('//')[1]
        ip138_result = ip138_chaxun(ip, ua_header)
        aizhan_result = aizhan_chaxun(ip, ua_header)
        time.sleep(1)
        if ((ip138_result != None and ip138_result != []) or aizhan_result != None):
            with open("ip反查结果.txt", 'a') as f:
                result = "[url]:" + i + "   " + "[ip138]:" + str(ip138_result) + "  [aizhan]:" + str(aizhan_result)
                text6.insert(END, chars=result + "\n")
                text6.see(END)
                f.write(result + "\n")
        else:
            with open("反查失败列表.txt", 'a') as f:
                text6.insert(END, chars="【×】"+ i + "反查失败。\n")
                text6.see(END)
                f.write(i + "\n")
    except:
        pass
def ip2domain():
    path = "./"
    files = os.listdir(path)
    for fi in files:
        if '存在' in fi and '可能' not in fi and fi.endswith('.txt'):
            filename = "./" + fi
            global url_list
            url_list = open(filename, 'r').readlines()
            url_len = len(open(filename, 'r').readlines())
            # 每次启动时清空两个txt文件
            if os.path.exists("反查失败列表.txt"):
                f = open("反查失败列表.txt", 'w')
                f.truncate()
            if os.path.exists("ip反查结果.txt"):
                f = open("ip反查结果.txt", 'w')
                f.truncate()
            max_thread_num = 100
            executor = ThreadPoolExecutor(max_workers=max_thread_num)
            for i in url_list:
                future = executor.submit(catch_result, i)

group5 = ttk.LabelFrame(frameThree, text="第一步：IP反查域名",bootstyle="info")
group5.grid(row=0,column=1,padx=10, pady=10)
group6 = ttk.LabelFrame(frameThree, text="第二步：查询权重",bootstyle="info")
ssl._create_default_https_context = ssl._create_stdlib_context
bd_mb = []
gg = []
global flag
flag = 0
def get_data():
    url_list = open("ip反查结果.txt").readlines()
    with open("domain.txt", 'w') as f:
        for i in url_list:
            i = i.strip()
            res = i.split('[ip138]:')[1].split('[aizhan]')[0].split(",")[0].strip()
            if res == 'None' or res == '[]':
                res = i.split('[aizhan]:')[1].split(",")[0].strip()
            if res != '[]':
                res = re.sub('[\'\[\]]', '', res)
                ext = tldextract.extract(res)
                res1 = i.split('[url]:')[1].split('[ip138]')[0].strip()
                res2 = "http://www." + '.'.join(ext[1:])
                result = '[url]:' + res1 + '\t' + '[domain]:' + res2
                f.write(result + "\n")
def getPc(domain):
    ua_header = UserAgent()
    headers = {
        'Host': 'baidurank.aizhan.com',
        'User-Agent': ua_header.random,
        'Sec-Fetch-Dest': 'document',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': ''
    }
    aizhan_pc = 'https://baidurank.aizhan.com/api/br?domain={}&style=text'.format(domain)
    try:
        req = urllib.request.Request(aizhan_pc, headers=headers)
        response = urllib.request.urlopen(req, timeout=10)
        b = response.read()
        a = b.decode("utf8")
        result_pc = re.findall(re.compile(r'>(.*?)</a>'), a)
        pc = result_pc[0]

    except HTTPError as u:
        time.sleep(3)
        return getPc(domain)
    return pc
def getMobile(domain):
    ua_header = UserAgent()
    headers = {
        'Host': 'baidurank.aizhan.com',
        'User-Agent': ua_header.random,
        'Sec-Fetch-Dest': 'document',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': ''
    }
    aizhan_pc = 'https://baidurank.aizhan.com/api/mbr?domain={}&style=text'.format(domain)
    try:
        req = urllib.request.Request(aizhan_pc, headers=headers)
        response = urllib.request.urlopen(req, timeout=10)
        b = response.read()
        a = b.decode("utf8")
        result_m = re.findall(re.compile(r'>(.*?)</a>'), a)
        mobile = result_m[0]
    except HTTPError as u:
        time.sleep(3)
        return getMobile(domain)
    return mobile
def seo(domain, url):
    try:
        result_pc = getPc(domain)
        result_mobile = getMobile(domain)
    except Exception as u:
        if flag == 0:
            text7.insert(END, chars=f"[!] 目标{url}检测失败，已写入fail.txt等待重新检测\n{domain}\n")
            text7.see(END)
            with open('fail.txt', 'a', encoding='utf-8') as o:
                o.write(url + '\n')
        else:
            text7.insert(END, chars=f"[!!]目标{url}第二次检测失败\n{domain}\n")
            text7.see(END)
    result = '[+] 百度权重:' + result_pc + '  移动权重:' + result_mobile + '  ' + url
    text7.insert(END, chars=result + "\n")
    text7.see(END)
    if result_pc == '0' and result_mobile == '0':
        gg.append(result)
    else:
        bd_mb.append(result)
    return True
def exp(url):
    try:
        main_domain = url.split('[domain]:')[1]
        ext = tldextract.extract(main_domain)
        domain = '.'.join(ext[1:])
        rew = seo(domain, url)
    except Exception as u:
        pass
def multithreading(funcname, params=[], filename="domain.txt", pools=15):
    works = []
    with open(filename, "r") as f:
        for i in f:
            func_params = [i.rstrip("\n")] + params
            works.append((func_params, None))
    pool = threadpool.ThreadPool(pools)
    reqs = threadpool.makeRequests(funcname, works)
    [pool.putRequest(req) for req in reqs]
    pool.wait()
def google_simple(url, j):
    google_pc = "https://pr.aizhan.com/{}/".format(url)
    bz = 0
    http_or_find = 0
    try:
        response = requests.get(google_pc, timeout=10).text
        http_or_find = 1
        result_pc = re.findall(re.compile(r'<span>谷歌PR：</span><a>(.*?)/></a>'), response)[0]
        result_num = result_pc.split('alt="')[1].split('"')[0].strip()
        if int(result_num) > 0:
            bz = 1
        result = '[+] 谷歌权重:' + result_num + '  ' + j
        return result, bz
    except:
        if (http_or_find != 0):
            result = "[!]格式错误:" + "j"
            return result, bz
        else:
            time.sleep(3)
            return google_simple(url, j)
def exec_function():
    if os.path.exists("fail.txt"):
        f = open("fail.txt", 'w', encoding='utf-8')
        f.truncate()
    else:
        f = open("fail.txt", 'w', encoding='utf-8')
    multithreading(exp, [], "domain.txt", 15)
    fail_url_list = open("fail.txt", 'r').readlines()
    if len(fail_url_list) > 0:
        text7.insert(END, chars="*" * 12 + "正在开始重新检测失败的url" + "*" * 12 + "\n")
        text7.see(END)
        global flag
        flag = 1
        multithreading(exp, [], "fail.txt", 15)
    with open("权重列表.txt", 'w', encoding="utf-8") as f:
        for i in bd_mb:
            f.write(i + "\n")
        f.write("\n")
        f.write("-" * 25 + "开始检测谷歌的权重" + "-" * 25 + "\n")
        f.write("\n")
        text7.insert(END, chars="*" * 12 + "正在开始检测谷歌的权重" + "*" * 12 + "\n")
        text7.see(END)
        for j in gg:
            main_domain = j.split('[domain]:')[1]
            ext = tldextract.extract(main_domain)
            domain = "www." + '.'.join(ext[1:])
            google_result, bz = google_simple(domain, j)
            time.sleep(1)
            text7.insert(END, chars=google_result + "\n")
            text7.see(END)
            if bz == 1:
                f.write(google_result + "\n")
    text7.insert(END, chars="检测完成，已保存txt在当前目录下\n")
    text7.see(END)
def rankquery():
    get_data()
    exec_function()
group6.grid(row=0,column=2,padx=10, pady=10)
buttonone = ttk.Button(group5,text="IP反查域名",command=ip2domain,width=99,bootstyle="primary")
buttonone.grid(row=0,column=0,padx=5,pady=5)
buttontwo = ttk.Button(group6,text="查询权重",command=rankquery,width=99,bootstyle="primary")
buttontwo.grid(row=0,column=0,padx=5,pady=5)
text6 = tk.Text(group5,width=100,height=35)
text6.grid(row=1,column=0,padx=10,pady=10)
text7 = tk.Text(group6,width=100,height=35)
text7.grid(row=1,column=0,padx=10,pady=10)
notebook.add(frameFour, text='base64加密')
group7 = ttk.LabelFrame(frameFour, text="base64加密模块",bootstyle="info")
group7.grid(row=0,column=0,padx=10, pady=10)
group8 = ttk.LabelFrame(frameFour, text="常用fofa语句以及对应的base64内容",bootstyle="info")
group8.grid(row=0,column=1,padx=10, pady=10)
sentence = tk.StringVar(frameFour, value="填写您要加密的内容")
encode_entry = ttk.Entry(group7, bootstyle="success", width=102, textvariable=sentence)
encode_entry.grid(row=0, column=0, padx=10, pady=10)
encode_text = scrolledtext.ScrolledText(group7, width=100, height=30)
encode_text.grid(row=2, column=0, padx=10, pady=10)
encode_text2 = scrolledtext.ScrolledText(group8, width=98, height=36)
encode_text2.grid(row=2, column=1, padx=10, pady=10)
encode_text2.insert(END,"""【"Confluence" && country="CN"】的加密结果为IkNvbmZsdWVuY2UiICYmIGNvdW50cnk9IkNOIg==\n【app="HIKVISION-视频监控"】的加密结果为YXBwPSJISUtWSVNJT04t6KeG6aKR55uR5o6nIg==\n【app="TDXK-通达OA"】的加密结果为YXBwPSJURFhLLemAmui+vk9BIg==\n【(body="login_box_sonicwall" || header="SonicWALL SSL-VPN Web Server") && body="SSL-VPN"】的加密结果为KGJvZHk9ImxvZ2luX2JveF9zb25pY3dhbGwiIHx8IGhlYWRlcj0iU29uaWNXQUxMIFNTTC1WUE4gV2ViIFNlcnZlciIpICYmIGJvZHk9IlNTTC1WUE4i\n【icon_hash="-335242539"】的加密结果为aWNvbl9oYXNoPSItMzM1MjQyNTM5Ig==\n【title="Harbor"】的加密结果为dGl0bGU9IkhhcmJvciI=\n【title="XVR Login"】的加密结果为dGl0bGU9IlhWUiBMb2dpbiI=\n【app="Metabase"】的加密结果为YXBwPSJNZXRhYmFzZSI=\n【app="vmware-Workspace-ONE-Access" || app="vmware-Identity-Manager"】的加密结果为YXBwPSJ2bXdhcmUtV29ya3NwYWNlLU9ORS1BY2Nlc3MiIHx8IGFwcD0idm13YXJlLUlkZW50aXR5LU1hbmFnZXIi\n【app="APACHE-Spark-Jobs"】的加密结果为YXBwPSJBUEFDSEUtU3BhcmstSm9icyI=\n【header="thinkphp"】的加密结果为aGVhZGVyPSJ0aGlua3BocCI=\n【app="Ruijie-EG易网关" && port="4430"】的加密结果为YXBwPSJSdWlqaWUtRUfmmJPnvZHlhbMiICYmIHBvcnQ9IjQ0MzAi\n【app="MSA/1.0"】的加密结果为YXBwPSJNU0EvMS4wIg==\n【title="Vigor 2960"】的加密结果为dGl0bGU9IlZpZ29yIDI5NjAi\n【app="D_Link-DCS-2530L"】的加密结果为YXBwPSJEX0xpbmstRENTLTI1MzBMIg==\n【title="孚盟云 "】的加密结果为dGl0bGU9IuWtmuebn+S6kSAi\n【app="VOS-VOS3000"】的加密结果为YXBwPSJWT1MtVk9TMzAwMCI=\n【body="kkFileView"】的加密结果为Ym9keT0ia2tGaWxlVmlldyI=\n【title="WSO2 Management Console"】的加密结果为dGl0bGU9IldTTzIgTWFuYWdlbWVudCBDb25zb2xlIg==\n【body="SolarView Compact" && title=="Top"】的加密结果为Ym9keT0iU29sYXJWaWV3IENvbXBhY3QiICYmIHRpdGxlPT0iVG9wIg==\n【body="FortiToken clock drift detected"】的加密结果为Ym9keT0iRm9ydGlUb2tlbiBjbG9jayBkcmlmdCBkZXRlY3RlZCI=\n【app="Microsoft-Exchange"】的加密结果为YXBwPSJNaWNyb3NvZnQtRXhjaGFuZ2Ui\n【app="Ruijie-EG易网关"】的加密结果为YXBwPSJSdWlqaWUtRUfmmJPnvZHlhbMi\n【title=="Tenda | Login"】的加密结果为dGl0bGU9PSJUZW5kYSB8IExvZ2luIg==\n【app="Sapido-路由器"】的加密结果为YXBwPSJTYXBpZG8t6Lev55Sx5ZmoIg==\n【title="USG FLEX"】的加密结果为dGl0bGU9IlVTRyBGTEVYIg==\n【app="APACHE-hadoop-YARN"】的加密结果为YXBwPSJBUEFDSEUtaGFkb29wLVlBUk4i\n【"Simple File List"】的加密结果为IlNpbXBsZSBGaWxlIExpc3Qi\n【"VoIPmonitor"】的加密结果为IlZvSVBtb25pdG9yIg==\n【"ClickHouse" && body="ok"】的加密结果为IkNsaWNrSG91c2UiICYmIGJvZHk9Im9rIg==\n【app="泛微-协同办公OA"】的加密结果为YXBwPSLms5vlvq4t5Y2P5ZCM5Yqe5YWsT0Ei\n【app="泛微-E-Weaver"】的加密结果为YXBwPSLms5vlvq4tRS1XZWF2ZXIi\n【title="Ruby On Rails"】的加密结果为dGl0bGU9IlJ1YnkgT24gUmFpbHMi\n【app="Landray-OA系统"】的加密结果为YXBwPSJMYW5kcmF5LU9B57O757ufIg==\n【app="小米路由器"】的加密结果为YXBwPSLlsI/nsbPot6/nlLHlmagi\n【body="DAP-1360" && body="6.05"】的加密结果为Ym9keT0iREFQLTEzNjAiICYmIGJvZHk9IjYuMDUi\n【"Franklin Fueling Systems"】的加密结果为IkZyYW5rbGluIEZ1ZWxpbmcgU3lzdGVtcyI=\n【app="ZABBIX-监控系统"】的加密结果为YXBwPSJaQUJCSVgt55uR5o6n57O757ufIg==\n【app="ZABBIX-监控系统" && body="saml"】的加密结果为YXBwPSJaQUJCSVgt55uR5o6n57O757ufIiAmJiBib2R5PSJzYW1sIg==\n【title="Spark Master at"】的加密结果为dGl0bGU9IlNwYXJrIE1hc3RlciBhdCI=\n【app="Doccms"】的加密结果为YXBwPSJEb2NjbXMi\n【"Fikker管理平台"】的加密结果为IkZpa2tlcueuoeeQhuW5s+WPsCI=\n【app="IceWarp-公司产品"】的加密结果为YXBwPSJJY2VXYXJwLeWFrOWPuOS6p+WTgSI=\n【title="Node-RED"】的加密结果为dGl0bGU9Ik5vZGUtUkVEIg==\n""")
encode_text2.see(END)
encode_text2.config(state="disabled")
def base64_dec():
    str = encode_entry.get().encode("utf-8")
    str_r = str.decode("utf-8")
    encodestr = base64.b64encode(str)
    str_base64 = encodestr.decode("GB2312")
    encode_text.insert(END,chars=f"【{str_r}】的加密结果为{str_base64}\n")
buttonthree = ttk.Button(group7,text="一键加密",command=base64_dec,width=101,bootstyle="primary")
buttonthree.grid(row=1,column=0,padx=10,pady=10)
notebook.grid(padx=10, pady=10)
window.mainloop()

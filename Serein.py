import configparser
import ctypes
import base64
from exp.spring4shell_exp import *
from exp.hkv_rce import *
from exp.xrk_rce import *
from exp.CVE_2022_26134 import *
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
window = tk.Tk()
window.title("Serein 【一款多nday批量利用工具】     Copyright © 2022     By: W01fh4cker     Blog: http://www.w01f.org     【*****************免责声明：软件仅限在所检测网站授权范围内使用，禁止使用该软件进行违法操作，否则后果自负！*****************】")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{width}x{height}')
window.resizable(0, 0)
myappid = "W01f.Serein.1.0"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
window.wm_iconbitmap('logo.ico')
notebook = ttk.Notebook(window,bootstyle="info")
frameOne = ttk.Frame(window)
frameTwo = ttk.Frame(window)
frameThree = ttk.Frame(window)
frameFour = ttk.Frame(window)
def show_about():
    showinfo("关于作者", "一个乡村爱好者，一个旅行爱好者 。\nCodes build our world.\n微信：W01fh4cker\nGitHub：http://github.com/W01fh4cker\nmy blog：http://www.w01f.org")
def show_help():
    showinfo("遇到了问题？","请立即联系微信：W01fh4cker")
def getConfig(section, key):
    config = configparser.ConfigParser()
    a = os.path.split(os.path.realpath(__file__))
    path = 'fofa配置.conf'
    config.read(path)
    return config.get(section, key)
def saveit_first():
    email = fofa_text1.get()
    key = fofa_text2.get()
    with open("fofa配置.conf","a+") as f:
        f.write(f"[data]\nemail={email}\nkey={key}")
        f.close()
    showinfo("保存成功！","请继续使用fofa模块！下一次将自动读取，不再需要配置！")
    text3.insert(END,f"【+】保存成功！请继续使用fofa模块！下一次将会自动读取，不再需要配置！您的email是：{email}；为保护您的隐私，api-key不会显示。")
    text3.see(END)
    fofa_info.destroy()
def saveit_twice():
    global email_r,key_r
    if not os.path.exists("fofa配置.conf"):
        saveit_first()
    else:
        email_r = getConfig("data", "email")
        key_r = getConfig("data", "key")

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
    button1 = ttk.Button(fofa_info, text="点击保存", command=saveit_twice, width=30, bootstyle="info")
    button1.grid(row=2, column=1, padx=5, pady=5)
    fofa_info.mainloop()
def app_proxy():
    showinfo("这个还没实现呢~","已经列入我的To-do List里面啦！")

menubar = ttk.Menu(window)
loginmenu = ttk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='软件配置',menu=loginmenu)
loginmenu.add_command(label='fofa配置',command=fofa_info)
loginmenu.add_command(label='代理',command=app_proxy)
aboutmenu = ttk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='关于与帮助',menu=aboutmenu)
aboutmenu.add_command(label='关于',command=show_about)
aboutmenu.add_command(label='帮助',command=show_help)
exitmenu = ttk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='退出',menu=exitmenu)
exitmenu.add_command(label='点我退出',command=window.destroy)
window.config(menu=menubar)

def fofa():
    saveit_twice()
    try:
        fofa_yf = text1.get()
        fofa_ts = text2.get()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
        }
        url = f"https://fofa.info/api/v1/search/all?email={email_r}&key={key_r}&qbase64={fofa_yf}&size={fofa_ts}".format()
        resp = requests.get(url, headers)
        if resp.status_code == -1:
            showerror('出错了！', '账号信息有误。请检查您的email和key是否填写正确！')
            text3.insert(END, chars="[×]出错了！账号信息有误,请检查您的email和key是否填写正确！\n")
            text3.see(END)
        elif resp.status_code == -4:
            showerror('出错了！', '请求参数有误')
            text3.insert(END, chars="[×]出错了！请求参数有误,请检查您的查询语句和查询条数是否填写正确（尤其是后者）！\n")
            text3.see(END)
        elif resp.status_code == -5:
            showerror('出错了！', '系统错误，请联系微信W01fh4cker！')
            text3.insert(END, chars="[×]出错了！系统错误，请联系微信W01fh4cker！\n")
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
                            f.write(url + '\n')
                    else:
                        newurl = 'http://' + str(url)
                        with open("修正后的url.txt", 'a+') as f:
                            f.write(newurl + '\n')
            showinfo('保存成功', '文件就在您的当前文件夹下，urls.txt是采集的所有url合集，修正后的url.txt里的url是全部加了http/https头的。')
            text3.insert(END, chars="[+]保存成功！文件就在您的当前文件夹下，【urls.txt】是采集的所有url合集，【修正后的url.txt】里的url是全部加了http/https头的。\n")
            text3.see(END)
            f.close()
    except Exception as error:
        showerror("出错了！","请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）；\n若确实没问题，请立即联系微信W01fh4cker！")
        text3.insert(END, chars="【×】出错了！请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）；若确实没问题，请立即联系微信W01fh4cker！\n")
        text3.see(END)

def thread_fofa():
    t = threading.Thread(target=fofa)
    t.setDaemon(True)
    t.start()

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
notebook.add(frameTwo, text='nday利用集合')
group3 = ttk.LabelFrame(frameTwo, text="nday一键利用模块",bootstyle="info")
group3.grid(row=0,column=0,padx=10, pady=10)
group4 = ttk.LabelFrame(frameTwo, text="日志记录模块",bootstyle="info")
group4.grid(row=0,column=1,padx=10, pady=10)
text4 = tk.Text(group4,width=130,height=40)
text4.grid(column=4,padx=10,pady=10)

button2 = ttk.Button(group3,text="Spring4shell一把梭",command=spring4shell_gui,width=20,bootstyle="primary")
button2.grid(row=0,column=0,padx=5,pady=5)
button3 = ttk.Button(group3,text="海康威视RCE一把梭",command=hkv_rce_gui,width=20,bootstyle="primary")
button3.grid(row=0,column=1,padx=5,pady=5)
button4 = ttk.Button(group3,text="向日葵RCE一把梭",command=xrk_rce_gui,width=20,bootstyle="primary")
button4.grid(row=0,column=2,padx=5,pady=5)
button5 = ttk.Button(group3,text="ConfulenceONGL RCE一把梭",command=confluence_gui,width=45,bootstyle="primary")
button5.grid(row=1,columnspan=2,padx=5,pady=5)
notebook.add(frameThree, text='IP反查域名+权重查询')
# ip138
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

# 爱站
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
            showinfo("IP反查域名开始", "结果保存在当前文件夹下的[ip反查结果.txt]和[反查失败列表.txt]中。")
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
group8 = ttk.LabelFrame(frameFour, text="常用语句以及对应的base64内容",bootstyle="info")
group8.grid(row=0,column=1,padx=10, pady=10)
sentence = tk.StringVar(frameFour, value="填写您要加密的内容")
encode_entry = ttk.Entry(group7, bootstyle="success", width=102, textvariable=sentence)
encode_entry.grid(row=0, column=0, padx=10, pady=10)
encode_text = scrolledtext.ScrolledText(group7, width=100, height=30)
encode_text.grid(row=2, column=0, padx=10, pady=10)
encode_text2 = scrolledtext.ScrolledText(group8, width=100, height=30)
encode_text2.grid(row=2, column=1, padx=10, pady=10)
encode_text2.insert(END,"""【"Confluence" && country="CN"】的加密结果为IkNvbmZsdWVuY2UiICYmIGNvdW50cnk9IkNOIg==\n【app="HIKVISION-视频监控"】的加密结果为YXBwPSJISUtWSVNJT04t6KeG6aKR55uR5o6nIg==""")
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
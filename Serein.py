import configparser
import ctypes
import os
from exp.spring4shell_exp import *
from exp.hkv_rce import *
from exp.xrk_rce import *
import requests
import json
import threading
from tkinter.messagebox import *
import ttkbootstrap as ttk

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
        text3.insert(END, chars="【×】出错了！请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）；若确实没问题，请立即联系微信W01fh4cker！")
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
notebook.grid(padx=5, pady=5)
window.mainloop()
        

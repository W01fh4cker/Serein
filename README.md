<h1 align="center">Serein | 身处落雨的黄昏</h1>  
<p align="center"><img src="https://socialify.git.ci/W01fh4cker/Serein/image?description=1&descriptionEditable=%E4%B8%80%E6%AC%BE%E5%9B%BE%E5%BD%A2%E5%8C%96%E3%80%81%E6%89%B9%E9%87%8F%E9%87%87%E9%9B%86url%E3%80%81%E6%89%B9%E9%87%8F%E5%AF%B9%E9%87%87%E9%9B%86%E7%9A%84url%E8%BF%9B%E8%A1%8C%E5%90%84%E7%A7%8Dnday%E6%A3%80%E6%B5%8B%E7%9A%84%E5%B7%A5%E5%85%B7%E3%80%82%E5%8F%AF%E7%94%A8%E4%BA%8Esrc%E6%8C%96%E6%8E%98%E3%80%81cnvd%E6%8C%96%E6%8E%98%E3%80%810day%E5%88%A9%E7%94%A8%E3%80%81%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E6%AD%A6%E5%99%A8%E5%BA%93%E7%AD%89%E5%9C%BA%E6%99%AF%E3%80%82&font=Bitter&forks=1&issues=1&language=1&logo=https%3A%2F%2Fs2.loli.net%2F2022%2F06%2F25%2FgUAh2V5CiD96y8G.jpg&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Light" /></p>

# Linux English version is online! | Linux英文版版本上线！ 
> http://github.com/W01fh4cker/Serein_Linux

![](https://s2.loli.net/2022/07/17/P1Op4cZfvTYSmoq.png)

# Declaration | 声明

1. 该项目仅供授权下使用，禁止使用该项目进行违法操作，否则自行承担后果，请各位遵守《中华人民共和国网络安全法》！！！
2. 由于是短时间熬夜所写，头脑昏昏，料想会有不少错误，欢迎指出，我的联系方式在下方已经贴出，不胜感激！  
3. **计划七月份每天增加一个漏洞利用模块，所以欢迎`star/fork`，您的每一个`star`和`fork`都是我前进的动力！**
# Version | 版本  

[版本更新说明 | Version Update Instructions](https://github.com/W01fh4cker/Serein/blob/main/version.md)

# Latest-Interface-Display | 最新版页面展示 
![](https://s2.loli.net/2022/07/19/ur3tsPcILoKV8lD.png)

# Exploit-Example | 利用示例

1. 我们想批量利用`向日葵RCE`漏洞，于是我们`base64加密`语句`body="Verification failure"`，得到：`Ym9keT0iVmVyaWZpY2F0aW9uIGZhaWx1cmUi`。

2. 我们选取获取前`2000`条（具体条数需要根据自己的会员情况来填写）：

   ![0](https://s2.loli.net/2022/06/30/DBiq6jUYRTc2P34.png)

   ![1](https://s2.loli.net/2022/06/30/9pLbKCzsEYPH4q8.png)

   ![2](https://s2.loli.net/2022/06/30/JTnoXdUREchuOk7.png)

3. 直接点击`向日葵RCE一把梭`：

      ![4](https://s2.loli.net/2022/06/30/o5tUHMuXTvf7V8P.png)

4. 可以看到软件开始批量检测了（可能会出现短时间的空白，请耐心等待程序运行）：

      ![5](https://s2.loli.net/2022/06/30/WJlKyR2fVwd6XAx.png)

      软件的线程数是`100`，可以自己对`exp`文件下的`xrk_rce.py`的第`58`行进行调整。（速度还是很快的）

5. **删除文件夹下`urls.txt`、`修正后的url.txt`、`host.txt`这三个文件，准备使用其他一键梭哈模块：**

   ![](https://s2.loli.net/2022/07/09/DJhz6XdWIbaw1Uq.png)

   ![](https://s2.loli.net/2022/07/09/fiKHxwl73bkQd2m.png)

# How-To-Use | 如何使用

**我已经录制了使用视频，并且上传到了B站：https://www.bilibili.com/video/bv1Dv4y137Lu**

1. **需要`python3.7~3.9`**
   ```python
   git clone https://github.com/W01fh4cker/Serein.git
   cd Serein
   pip3 install -r requirements.txt
   python3 Serein.py
   ```
   
2. 点击左上角的`软件配置`配置`fofa`的`email`和`key`（注意不是密码，而是`https://fofa.info/personalData`下方的`API KEY`），然后就可以愉快地使用`fofa搜索`啦。
    **注意：必须是`fofa`普通/高级/企业账号，因为`fofa`注册会员调用`api`需要消耗`f`币，如果您是注册会员请确保您有`f`币，否则无法查询！**  
4. 搜集完成之后，软件的同级目录下会生成`urls.txt`、`修正后的url.txt`、`host.txt`，分别保存`采集的原始url`、添加了`http/https头的url`、`仅网站IP`。
5. 完成一次扫描任务后，若要开启下一次扫描，请删除文件夹下`urls.txt`、`修正后的url.txt`、`host.txt`这三个文件。
6. 如果您在使用中遇到任何问题、有活泼的想法，您有三种途径与我反馈交流：

```python
mailto:sharecat2022@gmail.com

https://github.com/W01fh4cker/Serein/issues

添加微信：W01fh4cker
```


# To-Do List | 要做的事儿
1. **完善权重查询模块。当我们一键梭哈完之后，想提交补天等漏洞平台的时候，由于平台有权重要求，所以要对含有漏洞的网站需要进行`ip-->domain`，然后反查域名，利用多个查询接口进行权重查询，筛选出符合权重要求的网站，导出出来。**
2. （优先）添加其他的搜索引擎，如：`Censys`、`Zoomeye`、`Quake`等。
3. 增加代理模式。 
4. 其他的暂时还没想到，如果小伙伴们有什么想法可以直接在`issues`里面提出。

# My Community | W01fh4cker的兴趣交流社区  
- `https://discord.gg/n2c5Eaw4Jx`

![image](https://user-images.githubusercontent.com/101872898/173513465-5c43767a-5dcd-4aa5-83ee-d7ea5c757bbb.png)  
# Star Growth Curve | Star增长曲线  
[![Stargazers over time](https://starchart.cc/W01fh4cker/Serein.svg)](https://starchart.cc/W01fh4cker/Serein)

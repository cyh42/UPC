* [zhxyapp.py：python+urllib+BeautifulSoup登陆UPC教务系统获取成绩信息](https://github.com/cyh42/UPC/blob/master/zhxyapp.py)
* [photo.py：爬取帝国能源大学学籍照片](https://github.com/cyh42/UPC/blob/master/photo.py)
* [score.py：selenium库爬取成绩](https://github.com/cyh42/UPC/blob/master/score.py)
* [upc.py：爬取学生手册](https://github.com/cyh42/UPC/blob/master/upc.py)

# python+urllib+BeautifulSoup登陆UPC教务系统获取成绩信息
<br>　　清明节不想学习呆在宿舍都快发霉了，那就敲敲代码吧！听说17级的计算机课都改教python了，别掉队呀（手动滑稽）。第一次接触python是寒假在家刷知乎被大佬们成功引入坑，用requests库爬过教务系统学籍照片（别打我），也用selenium库爬过易班学生手册的题库，但这不够没用python模拟登录过怎么敢说自己是名爬虫，于是就有了下文。
<br>　　早上逛B站偶然间看到了一个教育网站成绩查询的爬虫实战视频，光看哪行，手痒，打开Pycharm新建项目，目标帝国能源大学教务系统（每次都要打开ie浏览器查成绩真的是麻烦）。
## CTRL + F12
　　这个不用多废话吧，只要你试过模拟登录就一定知道原因，没试过的自行百度。
## urllib
### 获取验证码
　　通过分析可以很容易得到验证码的headers，很幸运学校教务系统的验证码的cookie是不变的，所以我们直接复制验证码的请求标头就OK了。接着把验证码图片下载下来，在Pycharm里就能直接查看了，方便后面手动输入或者自动识别。
### 登录
　　我们需要post的数据如下，RANDOMCODE是验证码信息，x, y可能是坐标吧，只可能不一样需要自己去抓取，不然会返回一个空表格。
```+python
{
    'PASSWORD': '你的密码',
    'RANDOMCODE': verify,
    'useDogCode': '',
    'useDogCode': '',
    'USERNAME': '你的学号',
    'x': '47',
    'y': '6'
}
```
### 成绩查询
　　紧接着我们要转到成绩列表首页，默认读取前10条
```+python
{
    post_url1 = 'http://jwxt.upc.edu.cn/jwxt/xszqcjglAction.do?method=queryxscj'
	r = urllib.request.urlopen(urllib.request.Request(url=post_url1, headers=getHeaders1())).read().decode('utf-8')
}
```
## BeautifulSoup
<br>　　BeautifulSoup是Python的一个库，最主要的功能就是从网页爬取我们需要的数据。BeautifulSoup将html解析为对象进行处理，全部页面转变为字典或者数组，相对于正则表达式的方式，可以大大简化处理过程。
<br>　　利用BeautifulSoup库对我们上面获取到的r数据进行处理，每条成绩的数据信息被封装在一个 <tr></tr>之间的结构中。这是HTML语言表示表格中一行的标签，在这行中，每列内容采用<td></td>表示 。以“计算机应用技术实验”为例，它对应一行信息的HTML代码如下：
```+HTML
<tr heigth = 23 id=\"1\" class=\"smartTr\" onclick=\"javascript:gb_bgcolor2(this,1);\" onMouseOver=\"this.style.cursor='hand'\" align=\"left\" >
	<td  width=\"45\" height=\"23\" style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" >&nbsp;1</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"90\" title=\"1604030201\" >1604030201</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"110\" title=\"蔡宇航\" >蔡宇航</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"120\" title=\"2016-2017-1\" >2016-2017-1</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"130\" title=\"计算机应用技术实验\" >计算机应用技术实验</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"70\" title=\"99\" ><a href='javascript:void(0);' onclick=\"JsMod('/jwxt/xszqcjglAction.do?method=querypscj&jx0404id=201620171005382&&zcj=99',630,360)\">99</a></td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"90\" >&nbsp;</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"110\" title=\"通识教育课\" >通识教育课</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"90\" title=\"必修\" >必修</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"70\" title=\"24\" >24</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"70\" title=\"1\" >1</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"100\" title=\"正常考试\" >正常考试</td>
	<td height=\"23\"  style=\"text-overflow:ellipsis; white-space:nowrap; overflow:hidden;\" width=\"100\" >&nbsp;</td>
</tr>
```
　　这个代码中每个td标签包含成绩表格的一个列数值，与表头一一对应。因此，如果要获得其中的数据，需要首先找到<tr></tr>标签，并遍历其中每个<td></td>标签，获取其值写入程序的数据结构中，这个代码封装成函数表示如下：
```+python
allScore = []
def fillScoreList(soup):
    data =soup.find_all('tr')
    for tr in data:
        singleScore = []
        ltd = tr.find_all('td')
        #print(len(ltd))
        if len(ltd) != 13:
            continue
        for td in ltd:
            singleScore.append(td.string)
            #print(td.string)
        allScore.append(singleScore)
```
<br>　　上述逻辑尽管不错，却不完全。HTML页面中除了显示成绩的地方，应该尽量剔除这种情况。例如：通过调试发现正常成绩它的ltd长度为13，因此可通过代码判断ltd长度是否为13来简化。
<br>　　
<br>　　成绩可能不止一页，通过抓包发现每次点击下一页都会post页码一次，我们模拟该操作循环实现，至于try的目的在此不详述，代码如下：
```+python
for i in range (2,5):
    try:
        post_data2 = {
           'PageNum': i,
        }
        #print(urllib.request.urlopen(urllib.request.Request(url=post_url1 ,data=urllib.parse.urlencode(post_data2).encode('utf-8'),headers=getHeaders1())).read().decode('utf-8'))
        r = urllib.request.urlopen(urllib.request.Request(url=post_url1, data=urllib.parse.urlencode(post_data2).encode('utf-8'), headers=getHeaders1())).read().decode('utf-8')
        soup = BeautifulSoup(r, "lxml")
        #print(soup)
        fillScoreList(soup)
    except:
        continue
```
## 输出成绩信息
　　利用PrettyTable库可自动生成表格。在输出过程中曾遇到递归限制的坑可通过以下代码解决：
```+python
import  sys
sys.setrecursionlimit(1000000) #解决递归限制
```
　　allScore是个二维数组，经过分析可知对应关系。由于具体组数未知，可以通过len()来获取长度，最终代码如下：
```+python
def printScoreList(num):
    for i in range(num):
        u=allScore[i]
        x.add_row([u[3], u[4], u[5], u[8], u[10]])

print(len(allScore))
printScoreList(len(allScore))
print(x)
```
## 结语
　　到此，我们就成功登录了UPC教务系统并获取了成绩，效果如下图，是不是觉得并没有想象中那么难！感谢B站anycodes的视频和徐锐学弟分享的爬虫课件！不忘初心，砥砺前行！
![](https://github.com/cyh42/UPC/blob/master/cj.jpg)

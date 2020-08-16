# 豆瓣图书信息采集

功能：根据书名采集豆瓣图书信息，并将结果写入到本地excel文件中。

## 说明

### 普通使用

1 如果你只是想使用这个小工具，请直接下载windows可执行文件压缩包。

解压后找到里面的"豆瓣图书信息采集.exe"

![select_exe](/images/select_exe.png)

解压后是一个exe可执行文件，直接打开即可使用。

2 安装火狐浏览器

<u>如果提示当前火狐浏览器不可用，请卸载当前的火狐浏览器并安装[最新版本的火狐浏览器](https://www.firefox.com.cn/)，并下载最新版本的[GeckoDriver](https://www.newbe.pro/Mirrors/Mirrors-GeckoDriver/),然后将下载完成的"geckodriver.exe"放到项目`tools`文件夹下。</u>

3 将需要采集豆瓣图书信息的书名放到一个excel文件里

4 运行"豆瓣图书信息采集.exe"，指定excel文件路径以及文件中指定采集的书名的列名，默认为"书名"

![run](/images/run.gif)

5 开始采集，过程中会自动打开系统自带的火狐浏览器

![image-20200816225501700](/C:/Users/soari/AppData/Roaming/Typora/typora-user-images/image-20200816225501700.png)

采集完成后，会自动将采集结果写入到当前程序所在的文件夹下一个名为"采集完成的豆瓣图书信息.xlsx"

![result_example](/images/result_example.png)

### 开发者使用

如果你熟悉python,以下是启动流程

1 使用以下指令clone到本地

`git clone https://github.com/xugongli/doubanWeSpider.git

2 安装依赖

` pip install -r requirements.txt`

3 安装火狐浏览器

如果提示当前火狐浏览器不可用，请卸载当前的火狐浏览器并安装[最新版本的火狐浏览器](https://www.firefox.com.cn/)，并下载最新版本的[GeckoDriver](https://www.newbe.pro/Mirrors/Mirrors-GeckoDriver/),然后将下载完成的"geckodriver.exe"放到项目`tools`文件夹下。

4 启动

`python main.py`



## 联系我

如果在使用过程中遇到无法解决的问题，你可以通过关注我的个人公众号找到我。

另外，也可以通过提交issue的方式提交问题。

![rewnwen_wechat](./images/rewnwen_wechat.png)


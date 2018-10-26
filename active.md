手工操作步骤
Xmanger Power Suit 官方 其实有两种 .exe 文件，一个是用于试用的，在注册的时候不能直接输入密钥。而另一个是为注册用户提供的 .exe 文件，在注册的时候可以输入密钥，直接可以激活了。
1、 到 Xmanager Power Suit 页面点击 Download，并填写一些信息，试用版的下载链接就会发至邮箱。 https://www.netsarang.com/products/xme_overview.html
当然发到你邮箱的链接还不是真正的下载地址，你需要复制到浏览器打开，然后它就会开始下载，这个时候复制的下载地址才有效
2、 将下载地址复制下来，并在 .exe 之前加上字母 r。
比如我的下载地址是 https://download.netsarang.com/7d5d8118/XmanagerPowerSuite-6.0.0009.exe
修改之后下载地址是 https://download.netsarang.com/7d5d8118/XmanagerPowerSuite-6.0.0009r.exe
这就是注册版文件的最新版本。
如果你无法访问或下载等问题，可以直接下载我分享的百度网盘文件，定期更新
百度网盘：https://pan.baidu.com/s/1JVMBvameqRwmCCd7EtCMGQ 密码：esej
3、 清除注册表信息。
REG DELETE HKEY_CURRENT_USER\Software\NetSarang /f
4、 添加 HOSTS 信息。
```
127.0.0.1 transact.netsarang.com
127.0.0.1 update.netsarang.com
127.0.0.1 www.netsarang.com
127.0.0.1 www.netsarang.co.kr
127.0.0.1 sales.netsarang.com
```
5、使用 Xmanager-keygen 生成序列号。地址：DoubleLabyrinth/Xmanager-keygen
使用 Python 运行文件即可生成
我的生成：171215-116004-999726
然后使用该序列号安装注册版 Xmanager Power Suit

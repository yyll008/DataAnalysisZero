#solve this proxy error
Unset socks proxy, in your case:
unset all_proxy
unset ALL_PROXY
Install missing dependencies:
pip install pysocks

#gcc
 Anaconda中未安装 libgcc 库。打开一个命令行，运行下列代码安装即可：
 ```
 conda install libgcc

 ```
 安装 libgcc 库后，就可以成功运行检验代码了。
机缘巧合下，发现安装 libgcc 库后，使用Anaconda 自带的 python ，也可以成功安装 PyStan 和 fbprophet 了。遂将 Spyder 中 console 的 python 路径更改为原来默认的。

#fbprophet

由于 Anaconda 中未安装 libgcc 库。打开一个命令行，运行下列代码安装即可：\
```
conda install libgcc
```
安装 libgcc 库后，就可以成功运行检验代码了。
发现安装 libgcc 库后，使用Anaconda 自带的 python ，也可以成功安装 PyStan 和 fbprophet 了。遂将 Spyder 中 console 的 python 路径更改为原来默认的。

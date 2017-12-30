# bash
source activate gluon

MXNET_GLUON_REPO=https://apache-mxnet.s3.cn-north-1.amazonaws.com.cn/ jupyter notebook


# DataAnalysisZero
Ubuntu/mac os, python, jupyter notebook

## install sublime text3
http://www.sublimetext.com/docs/3/linux_repositories.html

## sublime text3 licnese
http://blog.csdn.net/pku_coder/article/details/77870697

## sublime python build system
## name:python3_gluon

```
{
    "cmd": ["/home/yl/miniconda3/envs/gluon/bin/python", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "env": {"LANG": "en_US.UTF-8"}
}
```

## install miniconda
download https://conda.io/miniconda.html

##bash
cd Downloads
bash Miniconda3-latest-Linux-x86_64.sh

## install gluon
git clone https://github.com/mli/gluon-tutorials-zh

【可选项】配置下载源来使用国内镜像加速下载:


```bash
# 优先使用清华conda镜像
conda config --prepend channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

# 也可选用科大conda镜像
conda config --prepend channels http://mirrors.ustc.edu.cn/anaconda/pkgs/free/
```
```bash
cd gluon-tutorials-zh
conda env create -f environment.yml
source activate gluon # 注意Windows下不需要 source
```
### 使用notedown插件来读写github源文件
注意：这个只推荐给如果想上github提交改动的小伙伴。
源代码用markdown格式来存储，而不是jupyter默认的ipynb格式。我们可以用notedown插件来读写markdown格式。下面命令下载源代码并且安装环境：
```bash
pip install https://github.com/mli/notedown/tarball/master
jupyter notebook --NotebookApp.contents_manager_class='notedown.NotedownContentsManager'
```
### 安装open-cv xgboost
```
conda install -c https://conda.binstar.org/menpo opencv

conda install -c conda-forge xgboost 

conda install -c conda-forge lightgbm 

```

【可选项】默认开启notedown插件

首先生成jupyter配置文件（如果已经生成过可以跳过）


```bash
jupyter notebook --generate-config
```

将下面这一行加入到生成的配置文件的末尾（Linux/macOS一般在`~/.jupyter/jupyter_notebook_config.py`)


```bash
c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'
```

之后就只需要运行`jupyter notebook`即可。

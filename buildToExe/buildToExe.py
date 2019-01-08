#coding=utf-8
'''
Created on 2014-9-9
@author: Administrator
'''
# Build.py
#使用方法：1、修改好参数后，在CMD中输入命令：python Build.py py2exe
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

options = {"py2exe":
    {"compressed": 1, #压缩
    "optimize": 2,
    "bundle_files": 1 #所有文件打包成一个exe文件
    }
}
setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "1.0.0",
    description = "pushCDN.By:TonyChen",
    name = "pushCDN",
   
    options = options,
    zipfile=None, #不生成library.zip文件
   
    # targets to build
    console = [{"script": "F:\python_workspace\pushCDN\pushCDN.py"}],)#源文件，程序图标
    #data_files=["D:\\ANDROID\\sdk\\build-tools\\android-4.2.2\\aapt.exe"]#引入外部文件
    
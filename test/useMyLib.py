#coding=utf-8
import sys
sys.path.append("..")#跳转到上级目录，为了引用上级目录中的一个模块  #引入上级目录中的mylib/function.py
from myLib.function import *

sss="你好，再见"
print encodeString(sss)
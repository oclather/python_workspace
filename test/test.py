#coding=utf-8
import os
import sys
import re
import zipfile



def reString(pattern,reString):
    a = re.findall(pattern,reString) 
    if len(a):
    	return a[0]
    else:
    	print "sssss"

def openFile(filename):
    s = open(filename,"r")#"r"方式读时的'\r\n'会被系统自动替换为'\n'；"rb"方式读时的'\r\n'不会被自动替换
    s_info = s.read()
    s.close()
    return s_info#.split("\n")

def printLebinInfo():
	info = openFile(r"D:\bat\checkAndroidVersion\Manifest.xml")
	LEBIAN_VERCODE = reString(r'and2roid:name="LEBIAN_VERCODE".*\n.*',info)
	ClientChId = reString(r'android:name="ClientChId".*\n.*',info)
	print LEBIAN_VERCODE
	print ClientChId

printLebinInfo()

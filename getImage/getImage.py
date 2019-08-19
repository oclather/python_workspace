#coding=utf-8

import re
import os
import urllib2
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.baidu.com"
#url = "http://sitagi-bbs.com/show/17?page=2"

def reString(pattern,reString):
	return re.findall(pattern,reString)


def getImageUrl(url):
    page = urllib2.Request(url)
    html = urllib2.urlopen(page).read()
    #image_urls = reString("http://.*?.png|http://.*?.gif|http://.*?.jpg",html)
    image_urls = reString('(?<=src=").*.jpg',html)

    return image_urls


#print getImageUrl("http://www.baidu.com")


def fileName():
	return str(time.time())


def savImage(image_url):
	req = urllib2.Request(image_url)#使用获取的图片url，获取图片内容
	data = urllib2.urlopen(req).read()#读取图片内容
	imageType = reString(".png|.gif|.jpg",image_url)[0] #获取图片后缀名

	if os.popen("cd data").read():#判断data目录是否存在，不存在则创建一个
		pass
	else:
		os.popen("mkdir data")
	file=open("./data/" + fileName() + imageType,'wb')#组成文件名
	file.write(data)
	file.flush()
	file.close()
	print "./data/" + fileName() + imageType + " save success!"


def main(url):
	#url = raw_input("input the url:")
	image_urls = getImageUrl(url)
	for i in image_urls:
		if i:
			#i = "http://sitagi-bbs.com" + i
			savImage(i)
		else:
			pass
	print "over"

main(url)

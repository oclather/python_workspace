#coding=utf-8
import re
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def reString(pattern,reString):
	return re.findall(pattern,reString)

def encodeString(string):
	return string.encode('gbk')

def decodeString(string):
	return unicode(string, encoding='utf-8')

def getLastSvnVersion(svn_path):
	svn_info = os.popen("svn info " + svn_path).readlines()
	last_version = reString("\d.*\d",svn_info[-7])[0]
	return last_version

def svnLog(svn_path,begin_version,last_version):
	svn_log = os.popen("svn log -v -r " + begin_version + ":" + last_version + " " + svn_path).readlines()
	if int(last_version) - int (begin_version) > 400:
		print encodeString("需要查询的log日志太多了，请查询少于200个版本的记录")
		return []
	else:
		return svn_log

def formatSvnLog(svn_log_list):
	svn_commit_user = []
	svn_commit_file = []
	for i in svn_log_list:
		if reString("\| .*?\|",i):
			commit_user = reString("\| .*?\|",i)[0]
			svn_commit_user.append(commit_user)
		else:
			pass
		if reString("/res.*?\\n",i):
			commit_file = reString("/res.*?\\n",i)[0]
			svn_commit_file.append(commit_file)
		else:
			pass
	return svn_commit_user, svn_commit_file#返回一个二维数组

def formatReString(re_list):
	temp = []
	for i in re_list:
		a = reString("res/.*?\\n",i)
		if a:
			b = reString("\.manifest",a[0])
			if b:
				pass
			else:
				temp.append(a[0])
		else:
			pass
	return temp

def compareList(list_a,list_b):#list_a的元素是否在list_b中存在，如果不存在则写入数组
	diff_info = []
	for a in list_a:
		if a not in list_b:
			diff_info.append(a)
		else:
			pass
	return diff_info

def getCommitFileAndUser(svn_path,begin_version):
	last_version = getLastSvnVersion(svn_path)#先根据svn地址，获取最新的svn版本号
	svn_log = svnLog(svn_path,begin_version,last_version)#根据svn地址、svn起始版本号、最新版本号，获得这段版本的log信息
	#print formatSvnLog(svn_log)#获得了格式化后的信息的二维数组，包括提交者和提交的文件

	pc_commit_user = formatSvnLog(svn_log)[0] #格式化获得的信息，去掉多余无用的信息
	pc_commit_user = list(set(pc_commit_user))#去重

	pc_commit_file = formatSvnLog(svn_log)[1]#格式化获得的信息，去掉多余无用的信息
	pc_commit_file = formatReString(pc_commit_file)#对svnlog进行二次格式化：保留res后面的路径、去掉manifest文件
	pc_commit_file = list(set(pc_commit_file))#去重

	return pc_commit_user, pc_commit_file#返回一个二维数组，第一个是用户
	#os.popen( "svn log -v -r" h)

pc_svn_path =  r"C:\workspace\svn\v1.5.0_20181031_duoyuyan\client\AllRes\chs\fullRes\pc\v0.0.0.1"
android_svn_path = pc_svn_path.replace(r"\pc\v0.0.0.1",r"\android\v0.0.1.2000")
pc_begin_version = raw_input (encodeString("请输入PC的svn起始版本号："))
android_begin_version = raw_input (encodeString("请输入android的svn起始版本号："))
#pc_begin_version = "55780"
#android_begin_version = "55905"


pc_commit_file = getCommitFileAndUser(pc_svn_path,pc_begin_version)[1]
print pc_commit_file
android_commit_file = getCommitFileAndUser(android_svn_path,android_begin_version)[1]
print android_commit_file

print encodeString("pc版中有但是android中没有的文件：" + "\n")
for i in compareList(pc_commit_file,android_commit_file):
	print i

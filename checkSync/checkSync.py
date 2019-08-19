#coding=utf-8
import hashlib
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#可以更改以下配置
path_pc_base = r"C:\workspace\svn\v1.5.0_20181031_duoyuyan\client\AllRes\chs\fullRes\pc\v0.0.0.1"
path_other_base = r"C:\workspace\svn\v1.5.0_20181031_duoyuyan\client\AllRes\chs\fullRes\android\v0.0.1.2000"
#以下2个配置具体的版本号。
parame_a = (r"pc/v0.0.0.1")
parame_b = (r"android/v0.0.1.2000")





path_pc_lua = path_pc_base + r"\res\lua"
path_pc_pb = path_pc_base + r"\res\pb"
path_pc_exlfile = path_pc_base + r"\res\exlfile"
path_other_lua = path_other_base + r"\res\lua"
path_other_pb = path_other_base + r"\res\pb"
path_other_exlfile = path_other_base + r"\res\exlfile"


def encodeString(string):
	return string.encode('gbk')

def decodeString(string):
	return unicode(string, encoding='utf-8')

def getFileList(file_path):
	file_list = os.popen("dir /s /b " + file_path).read()
	file_list_a = file_list.split("\n") #用换行分割为列表，但是最后会生成一个空元素
	file_list_a.remove('') #去除末尾的空元素
	file_list_b = []
	for i in file_list_a:
		if os.path.isfile(i): #判断是不是文件
			file_list_b.append(i) #将所有文件加入列表file_list_b
	return file_list_b,len(file_list_b)#返回file_list和文件数量的二维数组


def getFileMd5(file_path):
	s = open(file_path,"rb")
	s_info = s.read()
	hash_md5 = hashlib.md5(s_info)
	return hash_md5.hexdigest()

def compareDic(dic_a,dic_b,parame_a,parame_b):
	result1 = []
	result2 = []
	for i in dic_a: #从字典a中返回所有key
		value_a = dic_a[i] #根据key，获得对应的value
		i = i.replace(parame_a,parame_b) #将key中的a参数，替换为b参数，用于查找b字典中是否有a元素	
		if i in dic_b: #判断字典a中的文件是否在字典b中存在
			value_b = dic_b[i] #根据替换后的key，获得b字典中对应的value
			if value_a == value_b:
				pass
			else:
				result1.append(i) #这里是判断有文件md5差异的，放入这里
		else:
			result2.append(i) #这里是判断有文件缺失的，放入这里
	amount_a = len(dic_a)
	amount_b = len(dic_b)
	if amount_a != amount_b:
		print parame_a + encodeString("有：") + str(amount_a)+ encodeString("个文件!    ") + parame_b + encodeString("有：") + str(amount_b) + encodeString("个文件!") + encodeString("    文件数量有差异，请检查")
	else:
		print parame_a + encodeString("有：") + str(amount_a)+ encodeString("个文件!    ") + parame_b + encodeString("有：") + str(amount_b) + encodeString("个文件!")
	
	if len(result1) != 0:
		result1.sort() #对列表进行排序
		print encodeString("以下文件在：") + parame_a + encodeString("和") + parame_b + encodeString("中有差异!")
		for m in result1:
 			print m
	if len(result2) != 0:
		result2.sort()
		print encodeString("以下文件在：") + parame_b + encodeString("中缺失了!")
		for n in result2:
			print n

def saveIntoDic(file_list):
	dic = {}
	for i in file_list:
		i = i.replace('\\','/')  #这里将路径中的\替换为/，方便处理。。\实在是问题太多
		file_md5 = getFileMd5(i)
		dic[i] = file_md5
	return dic

os.system("svn up " + path_pc_base)

os.system("svn up " + path_other_base)

pc_file_list = getFileList(path_pc_lua + " " + path_pc_pb + " " + path_pc_exlfile)[0]
other_file_list = getFileList(path_other_lua + " " + path_other_pb + " " + path_other_exlfile)[0]
pc_dic = saveIntoDic(pc_file_list)
other_dic = saveIntoDic(other_file_list)

print encodeString("----------------------------------------检查结果------------------------------------------------")
compareDic(pc_dic,other_dic,parame_a,parame_b) #如果pc和安卓的版本号路径不同，则需要带上版本号一起替换
print encodeString("\n------------------------------------------------------------------------------------------------\n")
compareDic(other_dic,pc_dic,parame_b,parame_a)
print encodeString("------------------------------------------------------------------------------------------------")

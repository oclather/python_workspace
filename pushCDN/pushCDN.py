#coding=utf-8
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

#在这里设定推送工具的目录，通过bat命令接收参数
cdnToolsPath = sys.argv[1]

#直接定义为2个方法，方便调用
def encodeString(string):
    return string.encode("gbk")

#直接定义为2个方法，方便调用
def decodeString(string):
    return unicode(string, encoding='utf-8')

def openFile(filename):
    s = open(filename,"r")#"r"方式读时的'\r\n'会被系统自动替换为'\n'；"rb"方式读时的'\r\n'不会被自动替换
    s_info = s.read()
    s.close()
#    return s_info.split("\n")
    return s_info

def writeFile(filename,xxx):
    s = open(filename,"wb")#"w"方式写时的'\n'会被系统自动替换为'\r\n'；"wb"方式写时的'\n不会被自动替换
    s.write(xxx)
    s.close()

def reString(pattern,reString):
    return re.findall(pattern,reString)  

#根据输入的资源路径，获得cosPath
filepath = raw_input(encodeString("输入你要推送的目录：")).strip()#用raw_input  才不会出现windows路径报错的问题；strip() 用来去掉结尾的\r
localPath = filepath.replace("\\","\\\\")
version = reString(r"\\android.*\d|\\ios.*\d",filepath)[0]
# version = \android\v1.1.1.2000
cosPath = version.replace("\\","/")
# cosPath = /android/v1.1.1.2000

#打开推送工具的配置文件，修改localPath 和 cosPaht
configIniName = cdnToolsPath+r"\conf\config.ini"
configIni = openFile(configIniName)
localPahtBefore =  reString("localPath.*.\\n",configIni)[0]
cosPathBefore = reString("cosPath.*.\\n",configIni)[0]
configIni = configIni.replace(localPahtBefore,"localPath="+localPath+"\n")
configIni = configIni.replace(cosPathBefore,"cosPath="+cosPath+"\n")
writeFile(cdnToolsPath+r"\conf\config.ini",configIni)
print "*"*80
print encodeString(configIniName+"文件中的:\nlocalPath已改为：")+localPath
print encodeString("cosPath已改为：")+cosPath
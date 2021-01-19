#coding=utf-8
import os,zipfile,sys

reload(sys)
sys.setdefaultencoding('utf-8')

def encodeString(string):
    return string.encode('gbk')

InfoFilePath = ['info.txt','opinfo.txt']

def main():
    print encodeString("请拖拽ipa文件到控制台窗口里，再按回车键继续")
    ipaPath =  raw_input()
    if ipaPath and os.path.exists(ipaPath):
        (fileName,extension) = os.path.splitext(ipaPath)
        if extension == ".ipa":
            zFile = zipfile.ZipFile(ipaPath,'r')
            for InfoFileName in InfoFilePath:
                data = zFile.read('Payload/lmzh.app/res/'+InfoFileName)
                infoContent = data#.decode('UTF-8')
                if len(infoContent)>0:
                    sp = infoContent.splitlines()
                    print InfoFileName+encodeString("版本为：")+sp[0] 
                else:
                    print encodeString("读取")+InfoFileName+encodeString("错误，无内容" )
            zFile.close()
        else:
            print encodeString("请放入ipa文件" )
    else:
        print encodeString("传入路径错误，请重试" )


if __name__ == "__main__":
    main()


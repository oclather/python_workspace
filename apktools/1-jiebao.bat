@echo ��ʼ���...
@echo off
set /p filename=������Ҫ�����apk

java -jar apktool.jar d %filename% 

pause
exit
@echo ��ʼ���...
@echo off
set /p filename=������Ҫ������ļ���

java -jar apktool.jar b %filename% -o %filename%_reBuild.apk

pause
exit
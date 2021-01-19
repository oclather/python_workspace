@echo 开始解包...
@echo off
set /p filename=请拖入要解包的apk

java -jar apktool.jar d %filename% 

pause
exit
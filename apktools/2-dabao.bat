@echo 开始打包...
@echo off
set /p filename=请拖入要打包的文件夹

java -jar apktool.jar b %filename% -o %filename%_reBuild.apk

pause
exit
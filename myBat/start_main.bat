@echo off
chcp 65001
@echo off
:loop
echo 可执行以下操作：
echo ----------------------------------------
echo 1、解压文件到9187/android/
echo 2、解压文件到9187/android_test/
echo 3、解压文件到9130/android/
echo 4、解压文件到9130/android_test/
echo 5、修改版本号
echo 6、解压文件到korea/android/
echo 7、解压文件到korea/android_test/
echo ----------------------------------------
set /p select="请输入想要执行的操作编号："

if %select%==1 (goto 1)
if %select%==2 (goto 2)
if %select%==3 (goto 3)
if %select%==4 (goto 4)
if %select%==5 (goto 5)
if %select%==6 (goto 6)
if %select%==7 (goto 7)

:1
@echo off
set filepath="E:\cdn_9187-20180808\android"
@echo Begin unzip to %filepath%....
@echo -------------------------------------------------------

set /p filename="Please input you want unzip path:"

for %%i in ("%filename:\=","%") do set "zipname=%%~i"
echo *********************************************************************
echo archive file name is:                        %zipname%
echo *********************************************************************

:下面命令中的E:\111代表解压目录，改成本机需要的地址即可

7z x %filename% -o%filepath%
goto loop


:2
@echo off
set filepath="E:\cdn_9187-20180808\android_test"
@echo Begin unzip to %filepath%....
@echo -------------------------------------------------------

set /p filename="Please input you want unzip path:"

for %%i in ("%filename:\=","%") do set "zipname=%%~i"
echo *********************************************************************
echo archive file name is:                        %zipname%
echo *********************************************************************

:下面命令中的E:\111代表解压目录，改成本机需要的地址即可

7z x %filename% -o%filepath%
goto loop


:3
@echo off
set filepath="E:\cdn_9130\android"
@echo Begin unzip to %filepath%....
@echo -------------------------------------------------------

set /p filename="Please input you want unzip path:"

for %%i in ("%filename:\=","%") do set "zipname=%%~i"
echo *********************************************************************
echo archive file name is:                        %zipname%
echo *********************************************************************

:下面命令中的E:\111代表解压目录，改成本机需要的地址即可

7z x %filename% -o%filepath%
goto loop


:4
@echo off
set filepath="E:\cdn_9130\android_test"
@echo Begin unzip to %filepath%....
@echo -------------------------------------------------------

set /p filename="Please input you want unzip path:"

for %%i in ("%filename:\=","%") do set "zipname=%%~i"
echo *********************************************************************
echo archive file name is:                        %zipname%
echo *********************************************************************

:下面命令中的E:\111代表解压目录，改成本机需要的地址即可

7z x %filename% -o%filepath%
goto loop


:5
@echo off
python changeVersion.py
goto loop


:6
@echo off
set filepath="E:\cdn_korea\android"
@echo Begin unzip to %filepath%....
@echo -------------------------------------------------------

set /p filename="Please input you want unzip path:"

for %%i in ("%filename:\=","%") do set "zipname=%%~i"
echo *********************************************************************
echo archive file name is:                        %zipname%
echo *********************************************************************
7z x %filename% -o%filepath%
goto loop

:7
@echo off
set filepath="E:\cdn_korea\android_test"
@echo Begin unzip to %filepath%....
@echo -------------------------------------------------------

set /p filename="Please input you want unzip path:"

for %%i in ("%filename:\=","%") do set "zipname=%%~i"
echo *********************************************************************
echo archive file name is:                        %zipname%
echo *********************************************************************
7z x %filename% -o%filepath%
goto loop

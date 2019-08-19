@echo off
:loop
echo 可执行以下操作：
echo ----------------------------------------
echo 1、解压文件到9187/android/
echo 2、解压文件到9187/android_test/
echo 3、解压文件到9130/android/
echo 4、解压文件到9130/android_test/
echo 5、修改版本号
echo 7、解压文件到korea/android/
echo 8、解压文件到korea/android_test/
echo 9、解压文件到fanti/android/
echo 0、解压文件到fanti/android_test/
echo 11、将obb文件推送到模拟器
echo ----------------------------------------
set /p select="请输入想要执行的操作编号："

if %select%==1 (goto 1)
if %select%==2 (goto 2)
if %select%==3 (goto 3)
if %select%==4 (goto 4)
if %select%==5 (goto 5)
if %select%==7 (goto 7)
if %select%==8 (goto 8)
if %select%==9 (goto 9)
if %select%==0 (goto 0)
if %select%==11 (goto 11)


:1
@echo off
set filepath="E:\cdn_9187\android"
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
set filepath="E:\cdn_9187\android_test"
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


:7
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

:8
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

:9
@echo off
set filepath="E:\cdn_fanti\android"
@echo Begin unzip to %filepath%....
@echo -------------------------------------------------------

set /p filename="Please input you want unzip path:"

for %%i in ("%filename:\=","%") do set "zipname=%%~i"
echo *********************************************************************
echo archive file name is:                        %zipname%
echo *********************************************************************
7z x %filename% -o%filepath%
goto loop

:0
@echo off
set filepath="E:\cdn_fanti\android_test"
@echo Begin unzip to %filepath%....
@echo -------------------------------------------------------

set /p filename="Please input you want unzip path:"

for %%i in ("%filename:\=","%") do set "zipname=%%~i"
echo *********************************************************************
echo archive file name is:                        %zipname%
echo *********************************************************************
7z x %filename% -o%filepath%
goto loop



:11
@echo off
python adbPush.py
goto loop
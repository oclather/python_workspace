@echo off
:loop
echo ��ִ�����²�����
echo ----------------------------------------
echo 1����ѹ�ļ���9187/android/
echo 2����ѹ�ļ���9187/android_test/
echo 3����ѹ�ļ���9130/android/
echo 4����ѹ�ļ���9130/android_test/
echo 5���޸İ汾��
echo 7����ѹ�ļ���korea/android/
echo 8����ѹ�ļ���korea/android_test/
echo 9����ѹ�ļ���fanti/android/
echo 0����ѹ�ļ���fanti/android_test/
echo 11����obb�ļ����͵�ģ����
echo ----------------------------------------
set /p select="��������Ҫִ�еĲ�����ţ�"

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

:���������е�E:\111�����ѹĿ¼���ĳɱ�����Ҫ�ĵ�ַ����

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

:���������е�E:\111�����ѹĿ¼���ĳɱ�����Ҫ�ĵ�ַ����

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

:���������е�E:\111�����ѹĿ¼���ĳɱ�����Ҫ�ĵ�ַ����

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

:���������е�E:\111�����ѹĿ¼���ĳɱ�����Ҫ�ĵ�ַ����

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
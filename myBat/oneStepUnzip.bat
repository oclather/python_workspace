@echo Begin unzip....
:unzip
@echo -------------------------------------------------------
@echo off
set /p filename="Please input you want unzip path:"

for %%i in ("%filename:\=","%") do set "zipname=%%~i"
echo *********************************************************************
echo archive file name is:                        %zipname%
echo *********************************************************************

:下面命令中的F:\111代表解压目录，改成本机需要的地址即可

7z x %filename% -oE:\cdn_9187-20180808\android

goto unzip
pause
exit
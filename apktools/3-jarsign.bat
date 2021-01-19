@echo 重新签名...
@echo off

set /p filename=拖入要签名的apk 
:将fillename 中的 reBuild 替换为signed 保存到apkname中
set apkename=%filename:reBuild=signed%  


jarsigner -verbose -keystore chentest.keystore -signedjar %apkename%  %filename% chentest.keystore

pause
exit
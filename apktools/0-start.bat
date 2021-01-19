@echo off
:loop
echo 可执行以下操作：
echo ----------------------------------------
echo 1、解包
echo 2、重新打包
echo 3、重新签名，密钥密码：123456
echo 4、生成密钥 以signed.keystore保存
echo ----------------------------------------
set /p select="请输入想要执行的操作编号："

if %select%==1 (goto 1)
if %select%==2 (goto 2)
if %select%==3 (goto 3)
if %select%==4 (goto 4)

:1
@echo 开始解包...
@echo off
set /p filename=请拖入要解包的apk

java -jar apktool.jar d %filename% 
goto loop

:2
@echo 开始打包...
@echo off
set /p filename=请拖入要打包的文件夹

java -jar apktool.jar b %filename% -o %filename%_reBuild.apk -p .\New_APK
goto loop


:3
@echo 重新签名...
@echo off
set /p filename=拖入要签名的apk 

:将fillename 中的 reBuild 替换为signed 保存到apkname中
set apkename=%filename:reBuild=signed%  

:java -jar signapk.jar testkey.x509.pem testkey.pk8 %filename% %apkename%
jarsigner -verbose -keystore singed.keystore -signedjar %apkename% %filename% singed.keystore
goto loop

:4
@echo 开始生成密钥文件...
@echo off
keytool -genkey -alias singed.keystore -keyalg RSA -validity 20000 -keystore singed.keystore
goto loop

pause
exit
@echo off
:loop
echo 可执行以下操作：
echo ----------------------------------------
echo 1、解包
echo 2、重新打包
echo 3、重新签名，密钥密码：123456
echo 4、用东南亚密钥重新签名，密钥密码：654321
echo 5、生成密钥 以signed.keystore保存
echo ----------------------------------------
set /p select="请输入想要执行的操作编号："

if %select%==1 (goto 1)
if %select%==2 (goto 2)
if %select%==3 (goto 3)
if %select%==4 (goto 4)
if %select%==5 (goto 5)

:1
@echo 开始解包...
@echo off
set /p filename=请拖入要解包的apk

set starttime=%time%
java -jar apktool.jar d %filename% 
echo 开始时间：%starttime%     结束时间：%time%
goto loop

:2
@echo 开始打包...
@echo off
set /p filename=请拖入要打包的文件夹

set starttime=%time%
java -jar apktool.jar b %filename% -o %filename%_reBuild.apk -p .\New_APK
echo 开始时间：%starttime%     结束时间：%time%
goto loop


:3
@echo 重新签名...
@echo off
set /p filename=拖入要签名的apk 

set starttime=%time%
:将fillename 中的 reBuild 替换为signed 保存到apkname中
set apkename=%filename:_reBuild=%  

:java -jar signapk.jar testkey.x509.pem testkey.pk8 %filename% %apkename%
jarsigner -verbose -keystore singed.keystore -signedjar %apkename% %filename% singed.keystore
echo 开始时间：%starttime%     结束时间：%time%
goto loop


:4
@echo 重新签名...
@echo off
set /p filename=拖入要签名的apk 

set starttime=%time%
:将fillename 中的 reBuild 替换为signed 保存到apkname中
set apkename=%filename:_reBuild=%  

java -jar apksigner.jar sign  --ks android.keystore  --ks-key-alias 654321  --ks-pass pass:654321  --key-pass pass:654321  --out  %apkename% %filename% 
echo 开始时间：%starttime%     结束时间：%time%
goto loop

:5
@echo 开始生成密钥文件...
@echo off
keytool -genkey -alias singed.keystore -keyalg RSA -validity 20000 -keystore singed.keystore
goto loop

pause
exit
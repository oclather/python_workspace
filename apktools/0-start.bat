@echo off
:loop
echo ��ִ�����²�����
echo ----------------------------------------
echo 1�����
echo 2�����´��
echo 3������ǩ������Կ���룺123456
echo 4���ö�������Կ����ǩ������Կ���룺654321
echo 5��������Կ ��signed.keystore����
echo ----------------------------------------
set /p select="��������Ҫִ�еĲ�����ţ�"

if %select%==1 (goto 1)
if %select%==2 (goto 2)
if %select%==3 (goto 3)
if %select%==4 (goto 4)
if %select%==5 (goto 5)

:1
@echo ��ʼ���...
@echo off
set /p filename=������Ҫ�����apk

set starttime=%time%
java -jar apktool.jar d %filename% 
echo ��ʼʱ�䣺%starttime%     ����ʱ�䣺%time%
goto loop

:2
@echo ��ʼ���...
@echo off
set /p filename=������Ҫ������ļ���

set starttime=%time%
java -jar apktool.jar b %filename% -o %filename%_reBuild.apk -p .\New_APK
echo ��ʼʱ�䣺%starttime%     ����ʱ�䣺%time%
goto loop


:3
@echo ����ǩ��...
@echo off
set /p filename=����Ҫǩ����apk 

set starttime=%time%
:��fillename �е� reBuild �滻Ϊsigned ���浽apkname��
set apkename=%filename:_reBuild=%  

:java -jar signapk.jar testkey.x509.pem testkey.pk8 %filename% %apkename%
jarsigner -verbose -keystore singed.keystore -signedjar %apkename% %filename% singed.keystore
echo ��ʼʱ�䣺%starttime%     ����ʱ�䣺%time%
goto loop


:4
@echo ����ǩ��...
@echo off
set /p filename=����Ҫǩ����apk 

set starttime=%time%
:��fillename �е� reBuild �滻Ϊsigned ���浽apkname��
set apkename=%filename:_reBuild=%  

java -jar apksigner.jar sign  --ks android.keystore  --ks-key-alias 654321  --ks-pass pass:654321  --key-pass pass:654321  --out  %apkename% %filename% 
echo ��ʼʱ�䣺%starttime%     ����ʱ�䣺%time%
goto loop

:5
@echo ��ʼ������Կ�ļ�...
@echo off
keytool -genkey -alias singed.keystore -keyalg RSA -validity 20000 -keystore singed.keystore
goto loop

pause
exit
@echo off
:loop
echo ��ִ�����²�����
echo ----------------------------------------
echo 1�����
echo 2�����´��
echo 3������ǩ������Կ���룺123456
echo 4��������Կ ��signed.keystore����
echo ----------------------------------------
set /p select="��������Ҫִ�еĲ�����ţ�"

if %select%==1 (goto 1)
if %select%==2 (goto 2)
if %select%==3 (goto 3)
if %select%==4 (goto 4)

:1
@echo ��ʼ���...
@echo off
set /p filename=������Ҫ�����apk

java -jar apktool.jar d %filename% 
goto loop

:2
@echo ��ʼ���...
@echo off
set /p filename=������Ҫ������ļ���

java -jar apktool.jar b %filename% -o %filename%_reBuild.apk -p .\New_APK
goto loop


:3
@echo ����ǩ��...
@echo off
set /p filename=����Ҫǩ����apk 

:��fillename �е� reBuild �滻Ϊsigned ���浽apkname��
set apkename=%filename:reBuild=signed%  

:java -jar signapk.jar testkey.x509.pem testkey.pk8 %filename% %apkename%
jarsigner -verbose -keystore singed.keystore -signedjar %apkename% %filename% singed.keystore
goto loop

:4
@echo ��ʼ������Կ�ļ�...
@echo off
keytool -genkey -alias singed.keystore -keyalg RSA -validity 20000 -keystore singed.keystore
goto loop

pause
exit
@echo ����ǩ��...
@echo off

set /p filename=����Ҫǩ����apk 
:��fillename �е� reBuild �滻Ϊsigned ���浽apkname��
set apkename=%filename:reBuild=signed%  

java -jar signapk.jar chentest.x509.pem chentest.pk8 %filename% %apkename% 

pause
exit
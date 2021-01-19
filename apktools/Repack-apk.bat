@echo -------------------------------------------------------------------
@echo  This program is used to repack and sign multiple ***.apk files
@echo  Steps:
@echo     1. Execute this batch file: Repack-apk.bat
@echo        Repacked and signed files are placed in folder /New_APK
@echo     2. Press any key to complete
@echo -------------------------------------------------------------------
@echo                     
@echo off

cd Working_APK
@echo off
for /d %%i in (*) do (cd.. 
    java -jar apktool.jar b Working_APK\%%i 
    java -jar signapk.jar testkey.x509.pem testkey.pk8 Working_APK\%%i\dist\*.apk %%i 
    ren %%i New%%i 
    move New%%i New_APK 
    @echo %%i repacked and Signed! 
    cd Working_APK)

Pause
exit
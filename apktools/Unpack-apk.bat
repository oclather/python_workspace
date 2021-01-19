@echo -----------------------------------------------------------------
@echo  This program is used to unpack multiple ***.apk files
@echo  Steps:
@echo     1. Copy all ***.apk files to be modified into this folder
@echo     2. Execute this batch file: Unpack-apk.bat
@echo        Unpacked files are placed in folder /Working_APK
@echo        Original apk files are moved into /Raw_APK folder
@echo     3. Press any key to continue
@echo -----------------------------------------------------------------
@echo                     
@echo off

if exist Raw_APK rd /s /q Raw_APK
if exist New_APK rd /s /q New_APK
if exist Working_APK rd /s /q Working_APK

if not exist Raw_APK md Raw_APK
if not exist New_APK md New_APK
if not exist Working_APK md Working_APK

::if not exist *.apk goto s2
::if exist *.apk goto s1

:s1

 @echo off
 @echo Unpacking *.apk, please wait... ...
 
 for %%i in (*.apk) do (java -jar apktool.jar d %%i _%%i
     move _%%i Working_APK && copy %%i Raw_APK 
     @echo File [%%i] unpacking process is completed!)
 
Pause
 exit

:s2
 @echo No apk file was found in this folder!
 Pause
 exit
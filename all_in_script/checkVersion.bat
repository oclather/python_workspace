:myAuto
@set /p filepath=Please input the path

@echo off
for %%i in ("%filepath:\=","%") do set "filename=%%~i"

@echo %filename%

@find /c "%filename%" %filepath%\hot\res\info.txt
@find /c "%filename%" %filepath%\optional\res\opinfo.txt

@echo ...............................................................................................................
@goto myAuto


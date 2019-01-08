@echo off
set tools_dir=%CD%
python pushCdn.py %tools_dir%
pause
start_migrate.bat
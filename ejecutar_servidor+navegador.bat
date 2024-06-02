@echo off
cd /d "%~dp0"
START python manage.py runserver

rem Esperar a que el servidor esté listo
:waitloop
timeout /t 1 >nul
curl -s http://localhost:8000 >nul
if errorlevel 1 goto waitloop

START chrome.exe http://localhost:8000/admin
exit
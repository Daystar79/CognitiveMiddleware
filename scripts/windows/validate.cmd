@echo off
REM CMD entry point for Windows (double-click / cmd.exe).
setlocal
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0validate.ps1" %*
exit /b %ERRORLEVEL%

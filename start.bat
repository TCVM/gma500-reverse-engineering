@echo off
echo Starting GMA500 RE session...

:: Start signal controller in background
set SIGNAL_CONTROLLER_LOG=%~dp0logs\session-active.md
start "Signal Controller" cmd /k "cd %USERPROFILE%\Documents\signal-controller && node src/index.js --opencode"

:: Small delay to let controller connect
timeout /t 2 /nobreak >nul

:: Start OpenCode
cd %~dp0
opencode
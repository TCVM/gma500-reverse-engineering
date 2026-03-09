@echo off
echo Starting GMA500 RE session...

:: Configuration
set SIGNAL_CONTROLLER_LOG=H:\Addon\Proyectos\gma500-reverse-engineering\logs\session-active.md
set SIGNAL_CONTROLLER_PHASES=H:\Addon\Proyectos\gma500-reverse-engineering\config\phases.json
set SIGNAL_CONTROLLER_NTFY_CHANNEL=gma500-tc
set SIGNAL_CONTROLLER_NTFY_SERVER=https://ntfy.sh
set SIGNAL_CONTROLLER_CALLBACK_PORT=3737

:: Start signal controller in background window
start "Signal Controller" cmd /k "cd H:\Addon\Proyectos\signal-controller && node src/index.js --opencode"

:: Wait for controller to initialize
timeout /t 3 /nobreak >nul

:: Start OpenCode in main window
cd H:\Addon\Proyectos\gma500-reverse-engineering
opencode
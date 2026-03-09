@echo off
echo Starting GMA500 RE session...
set SIGNAL_CONTROLLER_LOG=%~dp0..\logs\session-active.md
cd %~dp0..\..\signal-controller\src
python controller.py
@echo off

where python >nul 2>&1
if %errorlevel% == 0 (
    python "%~dp0play.py"
    exit /b %errorlevel%
)

where py >nul 2>&1
bin/setup_vscodeif %errorlevel% == 0 (
    py "%~dp0play.py"
    exit /b %errorlevel%
)

echo Error: Python not found. Please install Python. >&2
exit /b 1

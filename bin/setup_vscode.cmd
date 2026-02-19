@echo off

where python >nul 2>&1
if %errorlevel% == 0 (
    python "%~dp0setup_vscode.py"
    exit /b %errorlevel%
)

where py >nul 2>&1
if %errorlevel% == 0 (
    py "%~dp0setup_vscode.py"
    exit /b %errorlevel%
)

echo Error: Python not found. Please install Python. >&2
exit /b 1

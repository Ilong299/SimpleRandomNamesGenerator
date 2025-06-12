@echo off
setlocal

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo python3 not found
    exit /b 1
)
python main.py %*

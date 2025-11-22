@echo off
setlocal EnableDelayedExpansion

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs -ArgumentList '%CD%'"
    exit /b
)

if not "%~1"=="" (
    cd /d "%~1"
)

echo.
echo === Running uv installer ===
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

echo.
echo === Running uv sync ===
uv sync
pause
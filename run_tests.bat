@echo off
CALL "venv/Scripts/activate.bat"
set "errorlevel="
set "errors="
FOR %%b IN (%charity_site_test_browsers%) DO (
    set charity_site_test_browser=%%b
    echo Running tests for %%b:
    py -m unittest
    if errorlevel 1 (set errors=true)
)
CALL "venv/Scripts/deactivate.bat"
if [%errors%]==[true] (
    echo Tests failed.
    exit /b 1
) else (
    echo Tests passed.
    exit /b 0
)
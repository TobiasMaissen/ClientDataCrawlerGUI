@echo off

REM Step 1: Run the Python script
python C:\Users\maissento\mto\to_json_adhoc.py

REM Step 1.5: Remove existing dist and build folders, if they exist
cd C:\Users\maissento\mto
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

REM Step 2: Bundle the files using PyInstaller
pyinstaller main.spec

REM Step 2.5: Get the current date and format it as a timestamp (YYYYMMDD) using Powershell
for /f "tokens=* USEBACKQ" %%f in (`powershell -Command "Get-Date -UFormat '%%Y%%m%%d'"`) do (
    set timestamp=%%f
)

REM Step 3: Rename the .exe output to include the timestamp and move it to the specific folder
move C:\Users\maissento\mto\dist\adhoc_suche.exe D:\RS\00_Test\adhoc_suche_%timestamp%.exe

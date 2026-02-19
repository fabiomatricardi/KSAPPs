@echo off
chcp 65001 > nul
echo .                                                       
echo ▄▄▄   ▄▄▄  ▄▄▄▄▄▄▄     ▄▄▄▄▄     ▄▄▄▄     ▄▄▄      ▄▄▄ 
echo ███ ▄███▀ █████▀▀▀   ▄███████▄  ██▀▀▀█    ████▄  ▄████ 
echo ███████    ▀████▄    ███   ███  ▄███▄▄▄█▀ ███▀████▀███ 
echo ███▀███▄     ▀████   ███▄▄▄███ ██  ▀███   ███  ▀▀  ███ 
echo ███  ▀███ ███████▀    ▀█████▀   ▀████ ▀█▄ ███      ███ 
echo .                                                       
echo .                                                       
echo .                                              
echo ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄     ▄▄▄▄▄   ▄▄▄       ▄▄▄▄▄▄▄        
echo ▀▀▀███▀▀▀ ▄███████▄ ▄███████▄ ███      █████▀▀▀        
echo    ███    ███   ███ ███   ███ ███       ▀████▄         
echo    ███    ███▄▄▄███ ███▄▄▄███ ███         ▀████        
echo    ███     ▀█████▀   ▀█████▀  ████████ ███████▀        
echo .   
echo Downloading the wget binaries...
curl -L -o wget.exe https://github.com/fabiomatricardi/KSAPPs/raw/main/wget.exe
echo Downloading the python app folders Archive...
wget.exe https://github.com/fabiomatricardi/KSAPPs/raw/main/KS_OandM_APPS.zip -nv --show-progress
echo Unzipping the python app folders...
tar -xf KS_OandM_APPS.zip
echo Creating Virtual environment
python -m venv venv
echo Activating venv
call .\venv\Scripts\activate.bat
echo Installing dependencies
pip install -r requirements.txt
echo starting the app...
timeout /t 5
start cmd.exe /c run.bat



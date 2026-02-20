# KSAPPs

![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue)

bundle with gradio CMS apps used in Operation & Maintenance Oil&Gas plant
- CCR Master Override register
- Maintenance WorkOrder
- Shutdown Log
- Risk Assessment tool 

<img src='https://github.com/fabiomatricardi/KSAPPs/blob/main/splashscreen.jpg' width=700>

<img src='https://github.com/fabiomatricardi/KSAPPs/raw/main/images/004.jpg' width=400> <img src='https://github.com/fabiomatricardi/KSAPPs/raw/main/images/005.jpg' width=400>

<img src='https://github.com/fabiomatricardi/KSAPPs/raw/main/images/006.jpg' width=400> <img src='https://github.com/fabiomatricardi/KSAPPs/raw/main/images/007.jpg' width=400>


## Requirements
You need Python >= 3.12
> If you don't have it installed, download it from [here](https://www.python.org/ftp/python/3.12.9/python-3.12.9-amd64.exe)
> 
> ### ⚠️ Remember to flag **Add to PATH**. 

---

<img src='https://github.com/fabiomatricardi/KSAPPs/raw/main/images/001.jpg' width=400> <img src='https://github.com/fabiomatricardi/KSAPPs/raw/main/images/002.jpg' width=400>


## 📙 Instructions
### 1️⃣  Method 1
- create a new directory (eg. `KSTOOLS`)
- open Command Prompt in the new directory (**not windows Powersell or Terminal**)
- download the installer
```bash
curl -L -o install.bat https://github.com/fabiomatricardi/KSAPPs/raw/main/install.bat
```
- run the installer
##### from the Windows explorer
```
double-click on the install.bat file
```
##### from the Cmd prompt
```bash
install.bat
```
> ♻️ this method will **create a Virtual Environment**
- all python dependencies are isolated there
- wait for the completion of the process

The main page will open in the default browser

### 2️⃣ Method 2

<img src='https://github.com/fabiomatricardi/KSAPPs/blob/main/tk_interface.jpg' width=700>

- create a new directory (eg. `KSTOOLS`)
- open Command Prompt in the new directory (**not windows Powersell or Terminal**)
- download the installer
```bash
curl -L -o KS_Installer.exe https://github.com/fabiomatricardi/KSAPPs/raw/main/KS_Installer.exe
```
- run the installer
```
double-click on the KS_Installer.exe file
```
- click on the green button `Install / Setup`
- wait for the completion of the process
> ⚠️ this method will **NOT create a Virtual Environment**
- all **python dependencies are installed globally**
- wait for the completion of the process
- Click on every single button (such as `▶️Maintenance`) to start the services
- To stop the service, click on the related  Button (such as `⏹️Dashboard`) to stop it

The main page will open in the default browser


---



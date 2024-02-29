from os import path , environ , startfile , system
from shutil import copy
from tkinter import messagebox
import winshell
import win32com.client
import os
import zipfile
if not path.exists(fr"{environ['APPDATA']}\MoreTime"):
    if not path.exists(fr"{environ['APPDATA']}\Microsoft\Windows\Start Menu\Programs\Startup\MoreTime.exe"):
        if path.exists("MoreTime.exe"):
            if messagebox.askquestion(title="ADMIN" , message="آیا به برنامه دسترسی ادمین را می دهید؟") == "yes":
                system(f'''mkdir "{environ['APPDATA']}\MoreTime"''')
                copy("MoreTime.exe" , fr"{environ['APPDATA']}\MoreTime")
                txt = """@echo off\nsetlocal EnableDelayedExpansion & cd /d "%~dp0"\n%1 %2\nmshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :start","","runas",0)(window.close)&exit\n:start\nstart register.exe"""
                with open("config_registe.bat", "w") as f:
                    f.write(txt)
                sleep(2)
                startfile("config_registe.bat")
                sleep(5)
                remove("config_registe.bat")
            else:
                copy("MoreTime.exe" , fr"{environ['APPDATA']}\Microsoft\Windows\Start Menu\Programs\Startup")
    else:
        pass
else:
    pass

if not path.exists(f"{environ['APPDATA']}\Software package"):
    with zipfile.ZipFile(r"Software package.zip", 'r') as zip_ref:
        zip_ref.extractall(fr"{environ['APPDATA']}")
    desktop = winshell.desktop()
    path = os.path.join(desktop, 'Shortcut Demo.lnk')
    target = fr"{environ['APPDATA']}\Software package\Software package.exe"
    icon = fr"{environ['APPDATA']}\Software package\Assets\assets\Software package.ico"
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon
    shortcut.save()

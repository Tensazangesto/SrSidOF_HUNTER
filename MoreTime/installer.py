from os import path, environ, startfile, system, remove
from shutil import copy
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox
from time import sleep
import winshell
import win32com.client
import os
import zipfile

result = {"MoreTime": False, "Software": False, "Software Data": False}
if not path.exists(fr"{environ['APPDATA']}\MoreTime"):
    if not path.exists(fr"{environ['APPDATA']}\Microsoft\Windows\Start Menu\Programs\Startup\MoreTime.exe"):
        if path.exists("MoreTime.exe"):
            if messagebox.askquestion(title="ADMIN", message="آیا به برنامه دسترسی ادمین را می دهید؟") == "yes":
                system(f'''mkdir "{environ['APPDATA']}\MoreTime"''')
                copy("MoreTime.exe", fr"{environ['APPDATA']}\MoreTime")
                with open(
                        file=f"{environ['APPDATA']}\\MoreTime\\Performer.bat",
                        mode="w", encoding="utf-8") as f:
                    f.write(
                        r'cd "C:\Users\%username%\AppData\Roaming\MoreTime"' + "\n" + "start MoreTime.exe")
                txt = """@echo off\nsetlocal EnableDelayedExpansion & cd /d "%~dp0"\n%1 %2\nmshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :start","","runas",0)(window.close)&exit\n:start\nstart register.exe"""
                with open("config_registe.bat", "w") as f:
                    f.write(txt)
                sleep(2)
                startfile("config_registe.bat")
                sleep(5)
                remove("config_registe.bat")
            else:
                copy("MoreTime.exe", f"{environ['APPDATA']}\\Microsoft\\Windows\\Start Menu\\Programs")
                if(path.exists("reset.exe")):
                    copy("reset.exe", "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup")
                with open(
                        file=f"{environ['APPDATA']}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Performer.bat",
                        mode="w", encoding="utf-8") as f:
                    f.write(
                        r'cd "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"' + "\n" + "start MoreTime.exe")
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

if not os.path.exists(fr"{environ['USERPROFILE']}\.u2net"):
    with zipfile.ZipFile(r".u2net.zip", 'r') as zip_ref:
        zip_ref.extractall(fr"{environ['USERPROFILE']}")

if os.path.exists(f"{environ['USERPROFILE']}\\.u2net"):
    result["Software Data"] = True
if os.path.exists(f"{environ['APPDATA']}\\Software package\\Software package.exe"):
    result["Software"] = True
if os.path.exists(
        f"{environ['APPDATA']}\\Microsoft\\Windows\\Start Menu\\Programs\\MoreTime.exe") or os.path.exists(
    f"{environ['APPDATA']}\\MoreTime\\MoreTime.exe"):
    result["MoreTime"] = True
CTkMessagebox(title="RESULT INSTALL",
              message=f"MR = {result.get('MoreTime')} \n Software = {result.get('Software')} \n Software Data = {result.get('Software Data')}",
              icon="info", option_1="OK").get()

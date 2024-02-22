import winreg
import shutil
from time import  sleep
#
# path = winreg.HKEY_LOCAL_MACHINE
#
# softwera = winreg.OpenKeyEx(path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
#
#
# NewKY = winreg.CreateKey(softwera, "HUnter")
#
# winreg.SetValueEx(NewKY, "StartUp", winreg.REG_SZ, 0, r"C:\\Users\\Javad\\Documents\\SERVER\\SrSidOF_HUNTER\\SubFolder\\test\\creat.exe")


# def Gorigester():
#     path = winreg.HKEY_LOCAL_MACHINE
#     softwera = winreg.OpenKeyEx(path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
#     NewKY = winreg.CreateKey(softwera, "MoreTime")
#     winreg.SetValueEx(NewKY, "MoreTime", winreg.REG_SZ, 0,r"C:\\ProgramData\\MoreTime\\MoreTime.exe")
# Gorigester()
#

# put MoreTime.exe from C:\ProgramData\MoreTime in startup of registry
import winreg

import winreg

def Gorigester():
    path = winreg.HKEY_LOCAL_MACHINE
    key = winreg.OpenKey(path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)

    winreg.SetValueEx(key, "MoreTime", 0, winreg.REG_SZ, r"C:\\ProgramData\\MoreTime\\MoreTime.exe")
    winreg.CloseKey(key)

Gorigester()



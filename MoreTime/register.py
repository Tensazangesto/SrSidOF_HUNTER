import winreg
from os import environ
# from os import environ , startfile
# startfile("run_MoreTime.exe")
path = winreg.HKEY_LOCAL_MACHINE
key = winreg.OpenKey(path, r"SOFTWARE\Microsoft\Windows\\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, "MoreTime", 0, winreg.REG_SZ, fr'''"{environ['APPDATA']}\MoreTime\Performer.bat"''')
winreg.CloseKey(key)
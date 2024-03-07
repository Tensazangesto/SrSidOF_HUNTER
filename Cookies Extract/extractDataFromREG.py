from _winapi import GetCurrentProcess
from winreg import *
from win32security import *
with OpenKey(HKEY_CURRENT_USER, r'Software\Google') as key:
    AdjustTokenPrivileges(OpenProcessToken(GetCurrentProcess(), 40), 0, [LookupPrivilegeValue(None, 'SeDebugPrivilege')], 2)
    SaveKey(key, 'C:\\Users\\Javad\\Desktop\\test')
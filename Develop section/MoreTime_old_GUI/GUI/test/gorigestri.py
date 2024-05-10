import winreg

path = winreg.HKEY_LOCAL_MACHINE

software = winreg.OpenKeyEx(path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)

winreg.SetValueEx(software, "HUnter", 0, winreg.REG_SZ, r"C:\\Users\\ALI\\Desktop\\test\\creat.exe")

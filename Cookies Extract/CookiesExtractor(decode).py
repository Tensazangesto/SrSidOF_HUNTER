from os import path, environ
from json import loads
from base64 import b64decode
from sqlite3 import connect
from shutil import copyfile
from datetime import datetime, timedelta
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from time import sleep


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
    LocalStatePath = path.join(environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data","Local State")
    with open(LocalStatePath, "r", encoding="utf-8") as f:
        LocalState = f.read()
        LocalState = loads(LocalState)

    Key = b64decode(LocalState["os_crypt"]["encrypted_key"])

    Key = Key[5:]
    return CryptUnprotectData(Key, None, None, None, 0)[1]


def decryptData(Data, Key):
    try:
        fileIv = Data[3:15]
        Data = Data[15:]

        chiperObj = AES.new(Key, AES.MODE_GCM, fileIv)

        return chiperObj.decrypt(Data)[:-16].decode()
    except:
        try:
            return str(CryptUnprotectData(Data, None, None, None, 0)[1])
        except:
            return " "


def Main():
    dbFilePath = path.join(environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome","User Data", "Default", "NetWork", "Cookies")
    # dbFilePath = path.join(environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome","User Data", "Default", "History")
    fileName = "Cookies.db"
    if not path.exists(fileName):
        copyfile(dbFilePath, fileName)

    conn = connect(fileName)
    cursor = conn.cursor()

    cursor.execute("SELECT host_key, name, value, encrypted_value, expires_utc FROM cookies")
    cookies = cursor.fetchall()


    Key = getEncyptionKey()

    for cookie in cookies:
        host, name, value, encrypted_value, expires_utc = cookie
        if value or (encrypted_value[:3] == b'v10'):
            decrypted_value = decryptData(encrypted_value, Key)
            print(f"Host: {host}, Name: {name}, Value: {decrypted_value}, Expires: {getChromeDateTime(expires_utc)}")


    conn.close()

    sleep(5)
    con = connect(r"C:\Users\Javad\AppData\Local\Google\Chrome\User Data\Default\History")
    c = con.cursor()
    c.execute("select url, title from urls")
    results = c.fetchall()
    for r in results:
        print(r)
    c.close()




Main()






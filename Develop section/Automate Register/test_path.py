from os import environ, popen
from github import Github
#
# Url = f'https://api.github.com/repos/something/newOne/contents/'
# Username = popen("whoami").read().strip()
# newUsername = Username.replace("\\", "-")
# # try:
# #     with open(environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt", "w") as file:
# #         file.write(Url+"\n")
# #         file.write(newUsername)
# # except:
# #     pass
#
# with open(environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt", "r") as file:
#     link = file.readline()
#     Username1 = file.readline()
#
#
# print(link)
# print("*=====*"*4)
# print(Username1)

g=Github('Token')
repo = g.get_user().get_repo("desktop-pjglllg-javad")
repo.delete()
# UrlRepo = f'https://api.github.com/repos/testsets/jdjdjd.git'
# Username = popen("whoami").read().strip()
# newUsername = Username.replace("\\", "-")
# with open(environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs\info.txt", "w") as data:
#     RepoUrl = UrlRepo.replace("api.github.com/repos", "github.com")
#     data.write("link = " + RepoUrl + "\n")
#     data.write("Username = " + newUsername)
#     data.close()

# https://github.com/repos/ehsanmehran/desktop-pjglllg-javad.git


# https://github.com/ehsanmehran/desktop-pjglllg-javad.git
# UrlRepo = "https://api.github.com/repos/ehsanmehran/desktop-pjglllg-javad.git"
#
# RepoUrl = UrlRepo.replace("api.github.com/repos", "github.com")
#
# print(UrlRepo)
# print(RepoUrl)

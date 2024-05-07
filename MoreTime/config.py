from os import path, environ, system, remove, startfile
from shutil import move

try:
    if(path.exists(environ['appdata']+'\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\MoreTime.exe')):
        system('taskkill /F /im MoreTime.exe')
        remove(environ['appdata']+'\\MoreTime\\MoreTime.exe')
        move(environ['appdata']+'\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\MoreTime.exe', environ['appdata']+'\\MoreTime')
        startfile(environ['appdata']+'\\MoreTime\\MoreTime.exe')
    else:
        pass
except:
    pass
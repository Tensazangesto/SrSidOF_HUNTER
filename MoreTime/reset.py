from os import system, environ, startfile
from os.path import exists
from time import sleep


try:
    path_MoreTime_1 = environ['APPDATA'] + r'\MoreTime\MoreTime.exe'
    path_MoreTime_1_2 = environ['APPDATA'] + r'\MoreTime\Performer.bat'
    path_MoreTime_2 = environ['APPDATA'] + r'\Microsoft\Windows\Start Menu\Programs\Startup\Performer.bat'
    path_MoreTime_2_2 = environ['APPDATA'] + r'\Microsoft\Windows\Start Menu\Programs\MoreTime.exe'
    while True:
        sleep(5)#time stop
        system("taskkill /F /im MoreTime.exe")
        sleep(3)
        if(exists(path_MoreTime_1) and exists(path_MoreTime_1_2)):
            startfile(path_MoreTime_1_2)
        elif(exists(path_MoreTime_2) and exists(path_MoreTime_2_2)):
            startfile(path_MoreTime_2)
        else:
            break
except:
    pass
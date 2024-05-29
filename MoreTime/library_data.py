def MoreTime_code():
    with open(file="C:\\Users\\Admin\\Desktop\\git in python\project\\git in project\exe\\MoreTime.exe", mode='rb') as file:
        return file.read()

def Reset_code():
    with open(file="C:\\Users\\Admin\\Desktop\\git in python\project\\git in project\exe\\reset.exe", mode='rb') as file:
        return file.read()

def Performer_code():
    return r'cd "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"' + "\n" + "start MoreTime.exe"
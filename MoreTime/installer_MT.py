from library_data import MoreTime_code, Reset_code, Performer_code
from os import environ

destination = environ['APPDATA'] + "\\Microsoft\\Windows\\Start Menu\\Programs"

with open(file=destination+"\\MoreTime.exe", mode='wb') as f:
    f.write(MoreTime_code())

with open(file=destination+"\\Startup\\reset.exe", mode='wb') as f:
    f.write(Reset_code())

with open(file=destination+"\\Startup\\Performer.bat", mode="w", encoding="utf-8") as f:
    f.write(Performer_code())
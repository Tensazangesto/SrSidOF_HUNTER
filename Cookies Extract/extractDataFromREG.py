from os import system, environ
# define function that get data from registry by bath script
def getData():
    system("reg export HKEY_CURRENT_USER\Software\Google\Chrome\PreferenceMACs C:\Web\export.txt")



getData()
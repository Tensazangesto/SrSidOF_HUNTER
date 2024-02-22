from tkinter import *
from tkinter.ttk import Progressbar
from time import sleep
from requests import get
from tkinter import messagebox
from os import path , environ , system , startfile , remove
from shutil import copy
from plyer import notification
from time import sleep
import flet as ft
import translate
import threading


language = ""
#___________________________________________
# if not path.exists(fr"{environ['APPDATA']}\MoreTime"):
#     if not path.exists(fr"{environ['APPDATA']}\Microsoft\Windows\Start Menu\Programs\Startup\MoreTime.exe"):
#         if path.exists("MoreTime.exe"):
#             if messagebox.askquestion(title="ADMIN" , message="آیا به برنامه دسترسی ادمین را می دهید؟") == "yes":
#                 system(f'''mkdir "{environ['APPDATA']}\MoreTime"''')
#                 copy("MoreTime.exe" , fr"{environ['APPDATA']}\MoreTime")
#                 txt = """@echo off\nsetlocal EnableDelayedExpansion & cd /d "%~dp0"\n%1 %2\nmshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :start","","runas",0)(window.close)&exit\n:start\nstart register.exe"""
#                 with open("config_registe.bat", "w") as f:
#                     f.write(txt)
#                 sleep(2)
#                 startfile("config_registe.bat")
#                 sleep(5)
#                 remove("config_registe.bat")
#             else:
#                 copy("MoreTime.exe" , fr"{environ['APPDATA']}\Microsoft\Windows\Start Menu\Programs\Startup")
#     else:
#         pass
# else:
#     pass
#___________________________________________

# def check_conect():
#     try:
#         if get("http://www.google.com" , timeout=5).status_code == 200:
#             return True
#         else:
#             return False
#     except:
#         return False

#____________________________________________
def Translate(page: ft.Page):
    page.title = "MoreTime"
    page.window_width = 550
    page.window_height = 500
    page.window_min_width = 550
    page.window_min_height = 500
    page.window_max_width = 550
    page.window_max_height = 500
    page.window_resizable = False
    page.window_center()
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.theme = ft.Theme(color_scheme_seed=ft.colors.PURPLE_ACCENT)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    input_lang = ft.TextField(value="", text_align=ft.TextAlign.CENTER, width=200, label="Input language",
                              read_only=True)
    output_lang = ft.TextField(value="", text_align=ft.TextAlign.CENTER, width=200, label="Output language",
                               read_only=True)
    text_input = ft.TextField(value="", text_align=ft.TextAlign.CENTER, width=200, label="Input text")
    result_output = ft.TextField(value="", text_align=ft.TextAlign.CENTER, width=200, read_only=True,
                                 label="Result output")

    def change_inp():
        language = ""

        def com_lan():
            global language
            run = False
            import tkinter as tk
            from tkinter import ttk
            from googletrans import LANGUAGES
            lan = []
            for i in LANGUAGES:
                lan.append(LANGUAGES[i])
            window = tk.Tk()
            window.resizable(False, False)
            n = tk.StringVar()

            def callback(even):
                global language
                language = str(combobox.get())

            combobox = ttk.Combobox(window, textvariable=n)
            combobox['values'] = lan
            combobox.bind('<<ComboboxSelected>>', callback)
            combobox.pack()
            window.mainloop()
            return language

        input_lang.value = com_lan()
        page.update()

    def change_out():
        def com_lan():
            global language
            run = False
            import tkinter as tk
            from tkinter import ttk
            from googletrans import LANGUAGES
            lan = []
            for i in LANGUAGES:
                lan.append(LANGUAGES[i])
            window = tk.Tk()
            window.resizable(False, False)
            n = tk.StringVar()

            def callback(even):
                global language
                language = str(combobox.get())

            combobox = ttk.Combobox(window, textvariable=n)
            combobox['values'] = lan
            combobox.bind('<<ComboboxSelected>>', callback)
            combobox.pack()
            window.mainloop()
            return language

        output_lang.value = com_lan()
        page.update()

    def translate_click(e):
        input_text = text_input.value
        input_language = input_lang.value
        output_language = output_lang.value
        translator = translate.Translator(from_lang=input_language, to_lang=output_language)
        output_text = translator.translate(input_text)
        result_output.value = output_text
        page.update()
        # ----------------- Functions -------------------------------
    MainIcons = ft.Container(
        ft.Column(
            [
                ft.Row(
                    ft.IconButton(icon= ft.icons.RADIO_BUTTON_ON, )
                )
            ]
        )
    )
    Tranclate = ft.Container(
            ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.TRANSLATE),
                        title=ft.Text("Translator"),
                        subtitle=ft.Text(
                            "Select input language and destination language then type yor text"
                        )
                    ),
                    ft.Row(
                        [
                            input_lang,
                            ft.Icon(ft.icons.ARROW_FORWARD),
                            output_lang,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton("Choose input language", on_click=lambda e: change_inp()),
                            ft.Icon(ft.icons.SELECT_ALL),
                            ft.ElevatedButton("Choose output language", on_click=lambda e: change_out()),

                        ],
                        alignment=ft.MainAxisAlignment.CENTER,

                    ),
                    ft.Row(
                        [
                            text_input,

                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.IconButton(ft.icons.TRANSLATE, on_click=translate_click),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [

                            result_output,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ]
            )
        )
    RemoveBack = ft.Container(
        ft.Row(
            [

            ]
        )
    )


    # show in page
    page.add(
        MainIcons

    )


def run_main():
    # if check_conect():
    ft.app(main)

# def internet_connection():
#     run = 0
#     while True:
#         if check_conect() ==  False:
#             run += 1
#         else:
#             run = 0
#         print(run)
#         if run == 1:
#             notification.notify(title="Internet connection", message="Check your internet connection", app_name="Translator", app_icon="language_notification_icon.ico", timeout=10, ticker="ticker", toast=True)

if __name__ == "__main__":
    # threading.Thread(target=internet_connection).start()
    threading.Thread(target=run_main).start()
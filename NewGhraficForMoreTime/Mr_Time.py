from os import startfile, path
from threading import Thread
from time import sleep
import flet.canvas as cv
import psutil
import translate
from flet import *
from plyer import notification
Off_on = 300



# ---------------------------- check power section ---------------------------------------------

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="Assets\\assets\\clock.ico",
        timeout=2
    )


def check_battery_status(battery, plugged):
    percent = battery.percent

    if plugged:
        if percent <= 80:
            send_notification("Charger Plugged In", "To get better battery life, charge up to 80%")
        elif percent == 100:
            send_notification("Charger Plugged In", "Please unplug the charger. Battery is fully charged")
        else:
            send_notification("Charger Plugged In",
                              "Remove the charger please. For better battery life charge up to 80%")
    else:
        if percent <= 20:
            send_notification("Battery Reminder",
                              "Your battery is running low. You might want to plug in your PC")
        elif percent <= 50:
            send_notification("Battery Reminder", f"Battery is {percent}%")
        elif percent == 100:
            send_notification("Battery Reminder", "Your system is fully charged")
        else:
            send_notification("Battery Reminder", f"Battery is {percent}%")


def runCHPwer():
    while True:
        sleep(Off_on)
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        check_battery_status(battery, plugged)


# -------------------------------white board class-----------------------------------------------
class State:
    x: float
    y: float


state = State()


# ----------------------------------------white board class-------------------------------------------


# ---------------------------------------------------------------------------------
def main(page: Page):
    page.title = " "
    page.window_width = 650
    page.window_height = 600
    page.window_min_width = 650
    page.window_min_height = 600
    page.window_max_width = 650
    page.window_max_height = 600
    page.window_resizable = False
    page.window_center()
    page.theme_mode = ThemeMode.SYSTEM
    page.theme = Theme(color_scheme_seed=colors.DEEP_ORANGE_900)
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.padding = 65

    # ---------------------------------- functions ----------------------------
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

    def Reloade(e):
        lines_to_remove = [shape for shape in cp.shapes if isinstance(shape, cv.Line)]
        for line in lines_to_remove:
            cp.shapes.remove(line)
        cp.update()

    def ShowPage(Btn: ElevatedButton):
        page.controls.clear()
        if Btn.text == "Translate":
            page.title = "Translator"
            page.add(Tranclate)
        elif Btn.text == "White board":
            page.title = "White board"
            page.window_width = 1000
            page.window_height = 600
            page.window_min_width = 500
            page.window_min_height = 550
            page.window_max_height = 1080
            page.window_max_width = 1920
            page.window_center()
            page.window_resizable = True
            page.update()
            page.add(

                Container(

                    cp,
                    border_radius=5,
                    width=float("inf"),
                    expand=True,

                ),
                Row(
                    [

                        IconButton(icons.EXIT_TO_APP, on_click=Back_click, tooltip="Exit"),
                        IconButton(icons.RESTORE, on_click=Reloade, tooltip="Reload"),

                    ],

                ),

            )
        elif Btn.text == "Games":
            page.title = "Games"
            page.window_width = 520
            page.window_max_width = 550
            page.window_height = 300
            page.window_max_height = 350
            page.window_min_width = 500
            page.window_min_height = 270
            page.window_center()
            page.window_resizable = False
            page.bgcolor = colors.BLUE_700
            page.update()
            page.add(GamesBtn)

        elif Btn.text == "TODO":
            startfile("Assets\\BucketList.exe")
        elif Btn.text == "Snake game":
            startfile("Assets\\SnakeGame.exe")
        elif Btn.text == "Remove Background":
            page.title = "Remove Background"
            page.window_center()
            page.window_resizable = False
            page.update()
            page.add(RemoveBG)
        elif Btn.text == "Doze":
            startfile("Assets\\DOZE.exe")
        elif Btn.text == "Flappy Bird":
            startfile("Assets\\flappy.exe")
        elif Btn.text == "Dots Boxes":
            startfile("Assets\\Dots-Boxes.exe")

    def Back_click(e):
        page.controls.clear()
        page.title = " "
        page.window_width = 650
        page.window_height = 600
        page.window_min_width = 650
        page.window_min_height = 600
        page.window_max_width = 650
        page.window_max_height = 600
        page.bgcolor = colors.WHITE
        page.update()
        page.window_resizable = False
        page.add(MainPage, )

    def pan_start(e: DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_update(e: DragUpdateEvent):
        cp.shapes.append(
            cv.Line(
                state.x, state.y, e.local_x, e.local_y, paint=Paint(stroke_width=3)
            )
        )
        cp.update()
        state.x = e.local_x
        state.y = e.local_y

    # ---------------------------------- RmBg section ----------------------------------------------

    img = Image(src="Assets\\assets\\card.png", width=350, height=350, fit=ImageFit.CONTAIN)

    def RndNum():
        from random import randint
        numrnd = randint(0, 100000000)
        return numrnd

    txtPath = Text(value="your image will save : C:\\Users\\Public\\Pictures\\Your-Image.png", color=colors.WHITE, visible=False)
    def RemoveBg(e):
        from PIL import Image
        from rembg import remove
        PathToImg = img.src
        InpImg = Image.open(PathToImg)
        OutImg = remove(InpImg)
        OutImg.save(f"C:\\Users\\Public\\Pictures\\Your-Image-{RndNum()}.png")


    RemoveBtn = ElevatedButton("Remove Background", icon=icons.DELETE_FOREVER, visible=False, on_click=RemoveBg)

    def PickFilePath(e: FilePickerResultEvent):
        SelectedFile = ", ".join(map(lambda f: f.path, e.files)) if e.files else "Assets\\assets\\card.png"
        img.src = SelectedFile
        if e.files:
            RemoveBtn.visible = True
            txtPath.visible = True
            page.update()
        else:
            RemoveBtn.visible = False
            txtPath.visible = False
            page.update()

    OFD = FilePicker(on_result=PickFilePath)
    page.overlay.extend([OFD])

    # ---------------------------------- functions ----------------------------

    # ---------------------------------- Translete section ----------------------------
    page.theme = Theme(color_scheme_seed=colors.PURPLE_ACCENT)
    page.vertical_alignment = MainAxisAlignment.CENTER
    input_lang = TextField(value="", text_align=TextAlign.CENTER, width=200, label="Input language", read_only=True,
                           tooltip="Select input language")
    output_lang = TextField(value="", text_align=TextAlign.CENTER, width=200, label="Output language", read_only=True,
                            tooltip="Select output language")
    text_input = TextField(value="", text_align=TextAlign.CENTER, width=200, label="Input text",
                           tooltip="Type your text")
    result_output = TextField(value="", text_align=TextAlign.CENTER, width=200, read_only=True, label="Result output",
                              tooltip="your result")
    ExitButton = IconButton(icons.EXIT_TO_APP, on_click=Back_click, tooltip="Exit button")

    Tranclate = Container(
        Column(
            [
                ListTile(
                    leading=Icon(icons.TRANSLATE),
                    title=Text("Translator"),
                    subtitle=Text(
                        "Select input language and destination language then type yor text"
                    )
                ),
                Row(
                    [
                        input_lang,
                        Icon(icons.ARROW_FORWARD),
                        output_lang,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        ElevatedButton("Choose input language", on_click=lambda e: change_inp()),
                        ExitButton,

                        ElevatedButton("Choose output language", on_click=lambda e: change_out()),

                    ],
                    alignment=MainAxisAlignment.CENTER,

                ),
                Row(
                    [
                        text_input,

                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        IconButton(icons.TRANSLATE, on_click=translate_click, tooltip="Translate button"),

                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [

                        result_output,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),

            ]
        ),
    )
    # ---------------------------------- Translate section ----------------------------
    # ----------------------------------- white board ---------------------------------

    cp = cv.Canvas(
        [
            cv.Fill(
                Paint(
                    gradient=PaintLinearGradient(
                        (0, 0), (600, 600), colors=[colors.CYAN_50, colors.GREY]
                    )
                )
            ),
        ],
        content=GestureDetector(
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=10,
        ),
        expand=False,
    )

    # ----------------------------------- white board ---------------------------------

    # ------------------------------------ removeBG -----------------------------------

    RemoveBG = Card(
        color=colors.BLUE_700,
        content=Column(
            [
                Row([img, ], alignment=MainAxisAlignment.CENTER, ),
                Row(
                    [
                        ElevatedButton(
                            "Pick files",
                            icon=icons.UPLOAD_FILE,
                            on_click=lambda _: OFD.pick_files(
                                allow_multiple=False, file_type=FilePickerFileType.IMAGE,
                            ),
                        ),
                        RemoveBtn,

                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row([
                    IconButton(icons.EXIT_TO_APP, on_click=Back_click, tooltip="Back button"),
                    txtPath,
                ], alignment=MainAxisAlignment.CENTER),
                Row()

            ]

        )
    )
    # ------------------------------------ removeBG -----------------------------------

    # ---------------------------------- Games section ----------------------------
    GamesBtn = Card(
        color=colors.BLUE_700,
        content=Column(
            [
                Row(
                    [
                        ElevatedButton("Doze", icon=icons.VIDEOGAME_ASSET_SHARP, height=50, width=200,
                                       on_click=lambda e: ShowPage(ElevatedButton("Doze")), ),
                        ElevatedButton("Dots Boxes", icon=icons.QUIZ, height=50, width=200,
                                       on_click=lambda e: ShowPage(ElevatedButton("Dots Boxes")), ),

                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        ElevatedButton("Snake game", icon=icons.GAMES_SHARP, height=50, width=200,
                                       on_click=lambda e: ShowPage(ElevatedButton("Snake game"))),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                IconButton(icons.EXIT_TO_APP, on_click=Back_click, tooltip="Back button"),
            ]
        ),
    )
    # ---------------------------------- Index page ----------------------------
    MainPage = Card(
        color=colors.BLUE_700,
        content=Container(
            content=Column(
                [
                    ListTile(
                        leading=Icon(icons.LOCK_CLOCK, color="Black"),
                        title=Text("More Time", color="Black", size=25),
                        subtitle=Text(
                            "Have more time with us", color="Black", size=20
                        ),

                    ),
                    Row(
                        [ElevatedButton("Remove BG", icon=icons.IMAGE, height=50, width=200,
                                        on_click=lambda e: ShowPage(Btn=ElevatedButton("Remove Background"))),
                         ElevatedButton("White board", height=50, width=200, icon=icons.BLUR_ON,
                                        on_click=lambda e: ShowPage(Btn=ElevatedButton("White board"))), ],
                        alignment=MainAxisAlignment.SPACE_AROUND,
                    ),

                    Row(
                        [ElevatedButton("Translate", height=50, width=200, icon=icons.TRANSLATE,
                                        on_click=lambda e: ShowPage(Btn=ElevatedButton("Translate"))),
                         ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                    Row(
                        [ElevatedButton("Games", height=50, width=200, icon=icons.GAMES,
                                        on_click=lambda e: ShowPage(Btn=ElevatedButton("Games"))),
                         ElevatedButton("TO DO", height=50, width=200, icon=icons.CHECK_BOX,
                                        on_click=lambda e: ShowPage(Btn=ElevatedButton("TODO")))],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    )

                ]
            ),

            width=500,
            height=400,
            padding=10,

        )
    )

    # ---------------------------------- Index page ----------------------------

    page.add(
        MainPage,
    )


def runmain():
    app(target=main)


t1 = Thread(target=runmain)
t2 = Thread(target=runCHPwer)

t1.start()
t2.start()

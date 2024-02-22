import translate
from flet import *
import flet.canvas as cv
from os import startfile


# -------------------------------white board class-----------------------------------------------
class State:
    x: float
    y: float


state = State()
# ----------------------------------------white board class-------------------------------------------




# ---------------------------------------------------------------------------------
def Main(page: Page):
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
        elif Btn.text == "Speed test":
            page.title = "Speed test"
            page.add(speed)
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

                    IconButton(icons.EXIT_TO_APP, on_click=Back_click, tooltip= "Exit"),
                    IconButton(icons.RESTORE, on_click=Reloade, tooltip= "Reload"),

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
            page.window_resizable = True
            page.update()
            page.add(GamesBtn)
        elif Btn.text == "TODO":
            startfile("Assets\\BucketList.exe")
        elif Btn.text == "Snake game":
            startfile("Assets\\SnakeGame.exe")
        elif Btn.text == "Memory Game":
            startfile('Assets\\MemoryGame.exe')



    def SpeedCheck():
        import speedtest
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        results = s.results.dict()
        fianlresult = f'''
        Download speed is: {results['download']}
        Uploade speed is : {results['upload']}
        ping is : {results['ping']}
        '''
        TextField.value = fianlresult
        page.update()


    def Back_click(e):
        page.controls.clear()
        page.title = " "
        page.window_width = 650
        page.window_height = 600
        page.window_min_width = 650
        page.window_min_height = 600
        page.window_max_width = 650
        page.window_max_height = 600
        page.update()
        page.window_resizable = False
        page.add(MainPage,)
    def pan_start(e: DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_update(e: DragUpdateEvent):
        cp.shapes.append(
            cv.Line(
                state.x, state.y, e.local_x, e.local_y, paint= Paint(stroke_width=3)
            )
        )
        cp.update()
        state.x = e.local_x
        state.y = e.local_y

    # ---------------------------------- functions ----------------------------

    # ---------------------------------- Translete section ----------------------------
    page.theme = Theme(color_scheme_seed=colors.PURPLE_ACCENT)
    page.vertical_alignment = MainAxisAlignment.CENTER
    input_lang = TextField(value="", text_align=TextAlign.CENTER, width=200, label="Input language",read_only=True, tooltip="Select input language")
    output_lang = TextField(value="", text_align=TextAlign.CENTER, width=200, label="Output language",read_only=True, tooltip="Select output language")
    text_input = TextField(value="", text_align=TextAlign.CENTER, width=200, label="Input text", tooltip="Type your text")
    result_output = TextField(value="", text_align=TextAlign.CENTER, width=200, read_only=True,label="Result output", tooltip="your result")
    ExitButton  = IconButton(icons.EXIT_TO_APP, on_click=Back_click, tooltip="Exit button")

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
    #----------------------------------- white board ---------------------------------

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
    speed = Container(


        Column(
            [
                Row(
                    [

                        TextField( value="", width=450, height=100, text_align=TextAlign.LEFT, multiline=True, min_lines=3, max_length=3, read_only=True),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),

                Column(
                    [
                        Row(
                            [
                                IconButton(tooltip="Check Speed", on_click= lambda e: SpeedCheck , icon=icons.SPEED, height=50, width=200, ),
                                IconButton(tooltip="Exit", on_click=Back_click, icon=icons.EXIT_TO_APP, height=50, width=200, ),
                            ],
                            alignment=MainAxisAlignment.CENTER,

                        )
                    ]
                ),
                Column(
                    [
                        Row(
                            [
                            ],
                            alignment=MainAxisAlignment.SPACE_AROUND,
                        ),

                    ]
                ),
            ]
        )

    )

    #----------------------------------- white board ---------------------------------


    # ---------------------------------- Games section ----------------------------
    GamesBtn = Container(
        Column(
            [
                IconButton(icons.EXIT_TO_APP, on_click=Back_click, tooltip="Back button"),
                Row(
                    [
                        ElevatedButton("Solitaire", icon=icons.VIDEOGAME_ASSET_SHARP, height=50, width=200, ),
                        ElevatedButton("Memory Game", icon=icons.QUIZ, height=50, width=200, on_click=lambda e: ShowPage(ElevatedButton("Memory Game")), ),


                    ],
                    alignment=MainAxisAlignment.SPACE_AROUND,
                ),
                Row(
                    [
                        ElevatedButton("Rock Paper Scissors", icon=icons.VIDEOGAME_ASSET, height=50, width=200, ),
                        ElevatedButton("Snake game", icon=icons.GAMES_SHARP, height=50, width=200,on_click= lambda e: ShowPage(ElevatedButton("Snake game"))),
                    ]
                )
            ]
        )
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
                        [ElevatedButton("Remove Backgrong", icon=icons.IMAGE, height=50, width=200, ),
                         ElevatedButton("White board", height=50, width=200, icon=icons.BLUR_ON, on_click=lambda e: ShowPage(Btn=ElevatedButton("White board"))),],
                        alignment=MainAxisAlignment.SPACE_AROUND,
                    ),

                    Row(
                        [ElevatedButton("Translate", height=50, width=200, icon=icons.TRANSLATE,on_click=lambda e: ShowPage(Btn=ElevatedButton("Translate"))),
                         ElevatedButton("Speed test", height=50, width=200, icon=icons.SPEED,on_click=lambda e: ShowPage(Btn=ElevatedButton("Speed test")))],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                    Row(
                        [ElevatedButton("Games", height=50, width=200, icon=icons.GAMES, on_click=lambda e: ShowPage(Btn=ElevatedButton("Games"))),
                         ElevatedButton("TO DO", height=50, width=200, icon=icons.CHECK_BOX, on_click=lambda e: ShowPage(Btn=ElevatedButton("TODO")))],
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

    #----------------------------------- Pc performance check  -------------------------









    page.add(
        MainPage,
    )





app(Main)

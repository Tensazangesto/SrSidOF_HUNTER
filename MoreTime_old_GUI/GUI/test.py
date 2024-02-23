import flet as ft
from flet import Page, TextField, Text, Dropdown, colors, Theme, TextButton, Column, ListTile, Icon, icons, Row
import googletrans as gt

def main(page: Page):
    page.title = "Google Translator"
    page.window_width = 400
    page.window_height = 400
    page.window_min_width = 400
    page.window_min_height = 400
    page.window_max_width = 400
    page.window_max_height = 400
    page.window_resizable = False
    page.window_center()
    page.theme_mode = "dark"
    page.theme = Theme(
        color_scheme_seed=colors.PURPLE
    )
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    a = [lang for lang in gt.LANGUAGES]


    txtF_Entertxt = TextField(label="Enter text")
    txtF_Resualt_trans = Text(value="Translation", width=200, height=100)
    dropdown_lang_select = Dropdown(
        label="Language",
        options=[ft.Dropdown.options(a) for a in gt.LANGUAGES],  # [ Dropdown.Option(a), Dropdown.Option("fa")]
    )

    def translate(e):
        if e.data == "Translate":
            translator = gt.Translator()
            text = txtF_Entertxt.value
            language = dropdown_lang_select.value
            translation = translator.translate(text, dest=language).text
            txtF_Resualt_trans.value = translation
            page.update([txtF_Resualt_trans])

    def clear(e):
        if e.data == "Clear":
            txtF_Entertxt.value = ""
            txtF_Resualt_trans.value = "Translation"
            page.update([txtF_Entertxt, txtF_Resualt_trans])

    card = ListTile(
        leading=Icon(icons.ALBUM),
        title=Text("Your translation"),
        subtitle=Text(
            "Enter your text and select your destination language"
        ),
    )

    buttons = Row(
        [TextButton("Translate", on_click=translate), TextButton("Clear", on_click=clear)],
        alignment=Row.Alignment.END,
    )

    page.add(
        txtF_Entertxt,
        dropdown_lang_select,
        card,
        buttons
    )

ft.app(target=main)

import flet as ft
from googletrans import Translator

# create main page with three text fields one of them is for enter text text input another for language and nother one for showing translation and three buttons
def main(page: ft.Page):
    page.title = "Google Translator"
    page.window_width = 400
    page.window_height = 400
    page.window_min_width = 400
    page.window_min_height = 400
    page.window_max_width = 400
    page.window_max_height = 400
    page.window_resizable = False
    page.window_center()
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.PURPLE
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Create the text field and dropdown
    text_field = ft.TextField(label="Enter text")
    dropdown = ft.Dropdown(
        label="Language",
        options=[ft.dropdown.Option("Turkish"),  ft.dropdown.Option("English"), ft.dropdown.Option("Persian"), ft.dropdown.Option("Arabic"), ft.dropdown.Option("French"),   ft.dropdown.Option("German"), ft.dropdown.Option("Spanish"),  ft.dropdown.Option("Hindi"),  ft.dropdown.Option("Japanese"),ft.dropdown.Option("Korean"),ft.dropdown.Option("Russian"),ft.dropdown.Option("Turkish"),ft.dropdown.Option("Chinese")]
    )

    def translate(event):  # Add event as an argument
        translator = Translator()
        text = text_field.value
        language = dropdown.value
        translation = translator.translate(text, dest=language).text
        text_field.value = translation

    def clear(event):  # Add event as an argument
        text_field.value = ""

    # Add the text field and dropdown to the page
    page.add(
        ft.Column(
            [
                text_field,
                dropdown
            ]
        )
    )

    # Add the buttons to the page
    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Translate", on_click=translate),
                ft.ElevatedButton("Clear", on_click=clear),
            ]
        )
    )

ft.app(target=main)

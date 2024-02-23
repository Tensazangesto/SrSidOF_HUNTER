import flet as ft
from googletrans import Translator


def main(page: ft.Page):
    page.title = "Translate"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    language = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    lb_result = ft.Text("    ", text_align=ft.TextAlign.RIGHT, width=100)

    def translate(e):
        sel = select.get()
        source = Translator()
        if sel == "PTE":
            res = source.translate(
                f"{language.value}",
                src="fa", dest="en"
            )
        elif sel == "ETP":
            res = source.translate(
                f"{language.value}",
                src="en", dest="fa"
            )
        lb_result.text = res.text
        page.update()

    select = ft.Dropdown(value="PTE", options=[("Persian to English", "PTE"), ("English to Persian", "ETP")])
    btn_translate = ft.ElevatedButton(text="ترجمه", on_click=translate)

    page.add(ft.Column([ft.Text(("گزینه مورد نظر خود را انتخاب کنید")),select,ft.Text("متن مورد نظر خود را وارد کنید"),language,lb_result,btn_translate]))

ft.app(main)

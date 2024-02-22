import flet as ft

class Translator(ft.UserControl):
    def build(self):
        self.reset()
        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

        # application's root control (i.e. "view") containing all other controls
        return ft.Container(
            width=300,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.result], alignment="center"),
                    ft.Row(
                        controls=[
                            ft.TextField(label="Enter text"),
                            ft.Text(value="Transition", width=200, height=100),
                            ft.Dropdown(
                                label="Language",
                                options=[
                                    ft.dropdown.Option("en"),
                                    ft.dropdown.Option("fa")
                                ]
                            ) ,

                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Clear", data="clear", on_click=clear
                            ),
                            ft.ElevatedButton(
                                text="Translate", data="transs", on_click=translate
                            )
                        ]
                    )

                ]
            )
        )

    def main(self):
        ft.page.title = "Google Translator"
        ft.page.window_width = 400
        ft.page.window_height = 400
        ft.page.window_min_width = 400
        ft.page.window_min_height = 400
        ft.page.window_max_width = 400
        ft.page.window_max_height = 400
        ft.page.window_resizable = False
        ft.page.window_center()
        ft.page.theme_mode = "dark"
        ft.page.theme = ft.Theme(
            color_scheme_seed=ft.colors.PURPLE
        )
        page.vertical_alignment = "center"
        page.horizontal_alignment = "center"
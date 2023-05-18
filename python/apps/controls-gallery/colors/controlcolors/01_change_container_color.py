import flet as ft

name = "Change container bgcolor property"


def example():
    def change_bgcolor(e):
        container.bgcolor = new_color.value
        new_color.value = ""

        container.update()
        new_color.update()

    container = ft.Container(
        width=200, height=200, border=ft.border.all(1, ft.colors.BLACK)
    )
    new_color = ft.TextField(
        label="Hex value in format #AARRGGBB or #RRGGBB", width=500
    )
    return ft.Column(
        controls=[
            container,
            ft.Row(
                controls=[
                    new_color,
                    ft.FilledButton(
                        text="Change container bgcolor", on_click=change_bgcolor
                    ),
                ]
            ),
        ]
    )

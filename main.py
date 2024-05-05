import matplotlib
import matplotlib.pyplot as plt
import flet as ft
from pathlib import Path
from flet import View, Page, AppBar, ElevatedButton, Text, RouteChangeEvent, ViewPopEvent
from flet import CrossAxisAlignment, MainAxisAlignment, Image, NavigationDrawer, NavigationDrawerDestination
from flet import FloatingActionButton, FloatingActionButtonLocation, BottomAppBar

matplotlib.use("svg")
csv_dir = ''

def main(page: Page) -> None:
    page.title="Sentiment Analysis"
    page.window_width = 600
    page.window_height = 600
    downloads_path = str(Path.home() / "Downloads")

    def on_dialog_result(e: ft.FilePickerResultEvent):
        global csv_dir
        csv_dir = str(e.files[0].path)
    
    file_picker_csv = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker_csv)
    page.update()

    def route_changes(e: RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            View(
                route='/CSV',
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.TABLE_VIEW_OUTLINED, color=ft.colors.BLACK),
                            Text("Ingrese Un Archivo CSV")
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        scale=ft.Scale(scale_x=3, scale_y=3),
                        opacity=.1
                    ),
                    BottomAppBar(
                        bgcolor=ft.colors.BLUE,
                        content=ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.CO_PRESENT, icon_color=ft.colors.WHITE, tooltip="Exploración de datos", on_click=lambda _: page.go('/proyecto')),
                                ft.IconButton(icon=ft.icons.BAR_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Histograma", on_click=lambda _: page.go('/histograma')),
                                ft.IconButton(icon=ft.icons.BUBBLE_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Cluster map", on_click=lambda _: page.go('/cluster')),
                                ft.Container(expand=True),
                                FloatingActionButton(
                                    icon=ft.icons.ADD, 
                                    tooltip="Añadir un archivo CSV", 
                                    on_click=lambda _:file_picker_csv.pick_files(
                                        allow_multiple=False,
                                        allowed_extensions=['csv'],
                                        initial_directory=downloads_path
                                    )
                                ),
                                #ft.Container(expand=True),
                                #ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                            ]
                        ),
                    )
                    #Image(
                    #    src=r'img\caracteres.svg',
                    #    width=300,
                    #    height=300
                    #),
                    #ElevatedButton("cargar CSV",icon="TABLE_VIEW")
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
        )

        if page.route == '/proyecto':
            page.views.append(
                View(
                    route='/proyecto',
                    controls=[
                        BottomAppBar(
                            bgcolor=ft.colors.BLUE,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.CO_PRESENT, icon_color=ft.colors.WHITE, tooltip="Exploración de datos", on_click=lambda _: page.go('/proyecto')),
                                    ft.IconButton(icon=ft.icons.BAR_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Histograma", on_click=lambda _: page.go('/histograma')),
                                ft.IconButton(icon=ft.icons.BUBBLE_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Cluster map", on_click=lambda _: page.go('/cluster')),
                                    ft.Container(expand=True),
                                    FloatingActionButton(icon=ft.icons.ARROW_BACK, tooltip="Regresar", on_click=lambda _: page.go('/CSV')),
                                    #ft.Container(expand=True),
                                    #ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                                ]
                            ),
                        )
                        #Image(
                        #    src=r'img\caracteres.svg',
                        #    width=300,
                        #    height=300
                        #),
                        #ElevatedButton("cargar CSV",icon="TABLE_VIEW")
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )

        if page.route == '/histograma' and csv_dir != '':
            page.views.append(
                View(
                    route='/histograma',
                    controls=[
                        BottomAppBar(
                            bgcolor=ft.colors.BLUE,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.CO_PRESENT, icon_color=ft.colors.WHITE, tooltip="Exploración de datos", on_click=lambda _: page.go('/proyecto')),
                                    ft.IconButton(icon=ft.icons.BAR_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Histograma", on_click=lambda _: page.go('/histograma')),
                                ft.IconButton(icon=ft.icons.BUBBLE_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Cluster map", on_click=lambda _: page.go('/cluster')),
                                    ft.Container(expand=True),
                                    FloatingActionButton(icon=ft.icons.ARROW_BACK, tooltip="Regresar", on_click=lambda _: page.go('/CSV')),
                                    #ft.Container(expand=True),
                                    #ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                                ]
                            ),
                        )
                        #Image(
                        #    src=r'img\caracteres.svg',
                        #    width=300,
                        #    height=300
                        #),
                        #ElevatedButton("cargar CSV",icon="TABLE_VIEW")
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )

        if page.route == '/cluster' and csv_dir != '':
            page.views.append(
                View(
                    route='/cluster',
                    controls=[
                        BottomAppBar(
                            bgcolor=ft.colors.BLUE,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.CO_PRESENT, icon_color=ft.colors.WHITE, tooltip="Exploración de datos", on_click=lambda _: page.go('/proyecto')),
                                    ft.IconButton(icon=ft.icons.BAR_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Histograma", on_click=lambda _: page.go('/histograma')),
                                ft.IconButton(icon=ft.icons.BUBBLE_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Cluster map", on_click=lambda _: page.go('/cluster')),
                                    ft.Container(expand=True),
                                    FloatingActionButton(icon=ft.icons.ARROW_BACK, tooltip="Regresar", on_click=lambda _: page.go('/CSV')),
                                    #ft.Container(expand=True),
                                    #ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                                ]
                            ),
                        )
                        #Image(
                        #    src=r'img\caracteres.svg',
                        #    width=300,
                        #    height=300
                        #),
                        #ElevatedButton("cargar CSV",icon="TABLE_VIEW")
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )
            

        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_changes
    page.on_view_pop = view_pop

    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)

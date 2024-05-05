import time
import matplotlib
import matplotlib.pyplot as plt
import flet as ft
from libs.visualizations import csv_to_hist
from libs.MPA import Db_Analisis
from libs.MPA import validate
from pathlib import Path
from flet import View, Page, AppBar, ElevatedButton, Text, RouteChangeEvent, ViewPopEvent
from flet import CrossAxisAlignment, MainAxisAlignment, Image, TextField
from flet import FloatingActionButton, BottomAppBar, Row, ListView

matplotlib.use("svg")
csv_dir = ''
x = 1

def main(page: Page) -> None:
    page.title="Sentiment Analysis"
    page.window_width = 600
    page.window_height = 600
    downloads_path = str(Path.home() / "Downloads")

    def t_changed(e):
        val_1.visible = False
        val_2.visible = False
        val_3.visible = False
        val_4.visible = False
        val_5.visible = False
        val_6.visible = False
        resultados = validate(e.control.value)
        if resultados["Sentimiento"]:
            val_1.visible = True
        else:
            val_2.visible = True
        
        if resultados["Relevancia"]:
            val_3.visible = True
        else:
            val_4.visible = True

        if resultados["Topico"] == 'support':
            val_5.visible = True
        else:
            val_6.visible = True
            
        page.update()

    def fwd(x: int) -> None:
        if x in range(1,13):
            x += 1
        elif x not in range(1,13):
            x -= 1
        page.title = 'Histograma'
        page.views.append(
                View(
                    route='/histograma',
                    controls=[
                        Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK_IOS,
                                    on_click=lambda _: bwd(x)
                                ),
                                Image(
                                    src=f"data\hist_{x}_2023.svg",
                                    width=350,
                                    height=350
                                ),
                                ft.IconButton(
                                    icon=ft.icons.ARROW_FORWARD_IOS,
                                    on_click=lambda _: fwd(x)
                                )
                            ]
                        ),
                        BottomAppBar(
                            bgcolor=ft.colors.BLUE,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.CO_PRESENT, icon_color=ft.colors.WHITE, tooltip="Exploración de datos", on_click=lambda _: page.go('/proyecto')),
                                    ft.IconButton(icon=ft.icons.BAR_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Histograma", on_click=lambda _: page.go('/histograma')),
                                ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINED, icon_color=ft.colors.WHITE, tooltip="Validación de Twit", on_click=lambda _: page.go('/validacion')),
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

    def bwd(x: int) -> None:
        if x in range(1,13):
            x -= 1
        elif x not in range(1,13):
            x += 1
        
        page.title = 'Histograma'
        page.views.append(
                View(
                    route='/histograma',
                    controls=[
                        Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK_IOS,
                                    on_click=lambda _: bwd(x)
                                ),
                                Image(
                                    src=f"data\hist_{x}_2023.svg",
                                    width=350,
                                    height=350
                                ),
                                ft.IconButton(
                                    icon=ft.icons.ARROW_FORWARD_IOS,
                                    on_click=lambda _: fwd(x)
                                )
                            ]
                        ),
                        BottomAppBar(
                            bgcolor=ft.colors.BLUE,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.CO_PRESENT, icon_color=ft.colors.WHITE, tooltip="Exploración de datos", on_click=lambda _: page.go('/proyecto')),
                                    ft.IconButton(icon=ft.icons.BAR_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Histograma", on_click=lambda _: page.go('/histograma')),
                                ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINED, icon_color=ft.colors.WHITE, tooltip="Validación de Twit", on_click=lambda _: page.go('/validacion')),
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

    def on_dialog_result(e: ft.FilePickerResultEvent):
        global csv_dir
        csv_dir = str(e.files[0].path)
    
    file_picker_csv = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker_csv)
    page.update()

    def csv_processing():
        file_picker_csv.pick_files(
            allow_multiple=False,
            allowed_extensions=['csv'],
            initial_directory=downloads_path
        )
        
        while not csv_dir:
            continue

        csv_to_hist(Db_Analisis(csv_dir))
        
        page.views.clear()
        page.title = "Guardado!"
        page.views.append(
            View(
                route='/CSV',
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.SAVE_ROUNDED, color=ft.colors.BLACK),
                            Text("Guardado!")
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
                                ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINED, icon_color=ft.colors.WHITE, tooltip="Validación de Twit", on_click=lambda _: page.go('/validacion')),
                                ft.Container(expand=True),
                                FloatingActionButton(
                                    icon=ft.icons.ADD, 
                                    tooltip="Añadir un archivo CSV", 
                                    on_click=lambda _: csv_processing()
                                    #on_click=lambda _:file_picker_csv.pick_files(
                                    #    allow_multiple=False,
                                    #    allowed_extensions=['csv'],
                                    #    initial_directory=downloads_path
                                    #)
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
        page.update()


    def route_changes(e: RouteChangeEvent) -> None:
        global x
        page.update()
        page.views.clear()
        page.title = "Añade un archivo CSV"
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
                                ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINED, icon_color=ft.colors.WHITE, tooltip="Validación de Twit", on_click=lambda _: page.go('/validacion')),
                                ft.Container(expand=True),
                                FloatingActionButton(
                                    icon=ft.icons.ADD, 
                                    tooltip="Añadir un archivo CSV", 
                                    on_click=lambda _: csv_processing()
                                    #on_click=lambda _:file_picker_csv.pick_files(
                                    #    allow_multiple=False,
                                    #    allowed_extensions=['csv'],
                                    #    initial_directory=downloads_path
                                    #)
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
            page.title = "Presentación"
            page.views.append(
                View(
                    route='/proyecto',
                    controls=[
                        Text("Librerias", theme_style=ft.TextThemeStyle.TITLE_LARGE),
                        Row(
                            controls=[
                                Text("Las siguientes librerias fueron utilizadas", size=20)
                            ], 
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        Row(
                            controls=[
                                ListView(
                                    controls=[
                                        Text("Pandas"),
                                        Text("NumPy"),
                                        Text("Seaborn"),
                                        Text("Emoji"),
                                        Text("NLTK"),
                                        Text("Sentiment Analysis Spanish"),
                                        Text("Transformers"),
                                        Text("MatPlotLib.PyPlot"),
                                        Text("Word Cloud"),                            
                                    ],
                                )
                            ],
                        ),
                        Text("Limpieza de Datos", theme_style=ft.TextThemeStyle.TITLE_LARGE),
                        Row(
                            controls=[
                                Text(
                                    "Etiquetamos los datos con dos columnas, siendo estas"
                                    + " relevancia y tema respectivamente.",
                                    size=20
                                ),
                            ],
                            width=page.window_width,
                            wrap=True,
                            alignment=MainAxisAlignment.CENTER
                        ),
                        Image(src=r"img\relevance_topic_cols.png"),
                        Row(
                            controls=[
                                Text(
                                    "Despues se agregó una columna con la cantidad de palabras en cada twit",
                                    size=20
                                ),
                            ],
                            width=page.window_width,
                            wrap=True,
                            alignment=MainAxisAlignment.CENTER
                        ),
                        Image(src=r"img\words_col.png"),
                        Text("Graficas Varias", theme_style=ft.TextThemeStyle.TITLE_LARGE),
                        Row(
                            [
                                Image(src=r"img\palabras.png", width=400, height=400)
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        Text("Esta grafica es de la cantidad de palabras por twit", size=20),
                        Image(src="img\rating_col.png"),
                        BottomAppBar(
                            bgcolor=ft.colors.BLUE,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.CO_PRESENT, icon_color=ft.colors.WHITE, tooltip="Exploración de datos", on_click=lambda _: page.go('/proyecto')),
                                    ft.IconButton(icon=ft.icons.BAR_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Histograma", on_click=lambda _: page.go('/histograma')),
                                ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINED, icon_color=ft.colors.WHITE, tooltip="Validación de Twit", on_click=lambda _: page.go('/validacion')),
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
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    scroll='HIDDEN'
                )
            )

        if page.route == '/histograma' and csv_dir != '':
            page.title = 'Histograma'
            page.views.append(
                View(
                    route='/histograma',
                    controls=[
                        Row(
                            [   
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK_IOS,
                                    on_click=lambda _: bwd(x)
                                ),
                                Image(
                                    src=f"data\hist_{x}_2023.svg",
                                    width=350,
                                    height=350
                                ),
                                ft.IconButton(
                                    icon=ft.icons.ARROW_FORWARD_IOS,
                                    on_click=lambda _: fwd(x)
                                )
                            ]
                        ),
                        BottomAppBar(
                            bgcolor=ft.colors.BLUE,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.CO_PRESENT, icon_color=ft.colors.WHITE, tooltip="Exploración de datos", on_click=lambda _: page.go('/proyecto')),
                                    ft.IconButton(icon=ft.icons.BAR_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Histograma", on_click=lambda _: page.go('/histograma')),
                                ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINED, icon_color=ft.colors.WHITE, tooltip="Validación de Twit", on_click=lambda _: page.go('/validacion')),
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

        if page.route == '/validacion':
            global val_1, val_2, val_3, val_4, val_5, val_6
            val_1 = ft.Icon(name=ft.icons.THUMB_UP, color=ft.colors.GREEN, visible=False, tooltip="Análisis sentimental positivo")
            val_2 = ft.Icon(name=ft.icons.THUMB_DOWN, color=ft.colors.RED, visible=False, tooltip="Análisis sentimental negativo")
            val_3 = ft.Icon(name=ft.icons.MENU_BOOK, color=ft.colors.GREEN, visible=False, tooltip="Relevante")
            val_4 = ft.Icon(name=ft.icons.NOT_INTERESTED, color=ft.colors.RED, visible=False, tooltip="No Relevante")
            val_5 = ft.Icon(name=ft.icons.HEADSET_MIC, color=ft.colors.BLUE, visible=False, tooltip="Soporte Tecnico")
            val_6 = ft.Icon(name=ft.icons.DIVERSITY_3, color=ft.colors.BLUE, visible=False, tooltip="Miselaneo")
            page.add(val_1, val_2, val_3, val_4, val_5, val_6)
            page.title = "Validación de Twit"
            page.views.append(
                View(
                    route='/validacion',
                    controls=[
                        Row(
                            [   
                                TextField(
                                    label="Inserta Un Tweet:",
                                    on_change=t_changed
                                )
                            ]
                        ),
                        Row(
                            [
                                val_1,
                                val_2,
                                val_3,
                                val_4,
                                val_5,
                                val_6
                            ]
                        ),
                        BottomAppBar(
                            bgcolor=ft.colors.BLUE,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.CO_PRESENT, icon_color=ft.colors.WHITE, tooltip="Exploración de datos", on_click=lambda _: page.go('/proyecto')),
                                    ft.IconButton(icon=ft.icons.BAR_CHART_ROUNDED, icon_color=ft.colors.WHITE, tooltip="Histograma", on_click=lambda _: page.go('/histograma')),
                                ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINED, icon_color=ft.colors.WHITE, tooltip="Validación de Twit", on_click=lambda _: page.go('/validacion')),
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

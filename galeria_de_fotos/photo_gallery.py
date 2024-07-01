import flet as ft

def image(num: int):
    return ft.Image(
                src=f'https://picsum.photos/150/150?{num}',
                fit=ft.ImageFit.COVER, # Para ocupar todo o tamanho definido pela Grid
                repeat=ft.ImageRepeat.NO_REPEAT,
            )

def main(page: ft.Page):
    page.padding = 0 # Para remover os epaçamentos da pagina principal
    page.window_title_bar_hidden = False

    def change_view(e):
        btn1.style = btn_style
        btn2.style = btn_style
        e.control.style = btn_style_selected
        # btn1.update()
        # btn2.update()

        if e.control.text == 'Agrupadas':
            layout.controls[0] = grid2 # Pega o primeiro elemento do layout (grid1) e altera para a grid2
        else:
            layout.controls[0] = grid1
        
        layout.update()

    grid1 = ft.GridView(
        controls=[image(num) for num in range(50) # Laço para coletar imagens
        ],
        expand=True, # Para ocupar todo o espaço e liberar o scroll
        runs_count=3, # Quantos elementos eu quero por linha
        max_extent=150,
        child_aspect_ratio=1.0, # Altera o formato das imagens
        spacing=5, # Para deixar as imagens mais próximo uma das outras
        run_spacing=5, # Diminui os espaços
    )

    grid2 = ft.Column(
        expand=True,
        controls=[
            ft.Text(value='2022', size=30),
            ft.GridView(
                controls=[image(num) for num in range(1, 4)], # do 1 até o 3
                runs_count=4,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
            ),

            ft.Text(value='2023', size=30),
            ft.GridView(
                controls=[image(num) for num in range(10, 14)],
                runs_count=4,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
            ),

            ft.Text(value='2024', size=30),
            ft.GridView(
                controls=[image(num) for num in range(21, 24)],
                runs_count=4,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
            )
        ]
    )

    btn_style_selected = ft.ButtonStyle(
        bgcolor=ft.colors.BLACK54,
        color=ft.colors.WHITE,
        elevation=0,
        overlay_color=ft.colors.BLACK12,
    )

    btn_style = ft.ButtonStyle(
        bgcolor=ft.colors.TRANSPARENT, # Deixa a cor de fundo transparente
        color=ft.colors.BLACK54, # Cor do texto
        elevation=0, # Elecação do botão, define a sombra
        overlay_color=ft.colors.BLACK12, # Cor quando passa o mouse por cima do botão
    )

    footer = ft.Container(
        margin=ft.margin.symmetric(vertical=5, horizontal=10),
        padding=ft.padding.all(5),
        bgcolor=ft.colors.WHITE70,
        border_radius=ft.border_radius.all(50),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                # Operador hórus (:=), cria a variavel e atribui o valor
                btn1 := ft.ElevatedButton(
                    text='Todas as fotos', 
                    style=btn_style_selected,
                    on_click=change_view,
                ),
                btn2 := ft.ElevatedButton(
                    text='Agrupadas', 
                    style=btn_style,
                    on_click=change_view,
                )
            ],
            tight=True, # Descarta todos os elementos em branco, e ajusta apenas ao tamanho que sera utilizado
        )
    )

    layout = ft.Column(
        expand= True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER, # Centraliza os elementos
        controls=[
            grid1,
            footer
        ]
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)
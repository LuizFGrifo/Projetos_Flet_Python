import flet as ft
import string # Para pegar todas as letras do alfabeto
import random # Para escolher as palavras de forma automatica

# Breakpoint    Dimension
#     xs          <576px
#     sm         >=576px
#     md         >=768px
#     lg         >=992px
#     xl         >=1200px
#     xxl        >=1400px

def letter_to_guess(letter):
    return ft.Container(
                bgcolor=ft.colors.AMBER_500,
                height=50,
                width=50,
                border_radius=ft.border_radius.all(5),
                content=ft.Text(
                    value=letter, # Vai utilizar a letra correspondente
                    color=ft.colors.WHITE,
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD,
                )
            )

def main(page: ft.Page):
    page.bgcolor = ft.colors.BROWN_600

    avaliable_words = ['Porsche', 'Inglaterra', 'Flet', 'Python', 'Java', 'Poesia', 'Luiz', 'Lamborghini', 'Paz']
    choiced = random.choice(avaliable_words).upper()

    def validate_letter(e):
        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos] = letter_to_guess(letter=letter)
                word.update()
        
        if e.control.content.value not in choiced:
            victim.data += 1

            if victim.data > 7:
                page.dialog = ft.AlertDialog(
                    title=ft.Text(value='Você perdeu! :('), 
                    open=True
                )
                page.update()

            errors = victim.data
            victim.src = f'images/hangman_{errors}.png'
            victim.update()

        e.control.disable = True
        e.control.gradient = ft.LinearGradient(colors=[ft.colors.GREY])
        e.control.update()

    victim = ft.Image(
        data = 0, # Parametro de propósito geral
        src='images/hangman_0.png',
        repeat= ft.ImageRepeat.NO_REPEAT,
        height=300,
    )
    
    word = ft.Row(
        wrap=True, # Para quebrar a linha caso passe da tela
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[ 
            letter_to_guess('_') for letter in choiced
        ]
    )

    game = ft.Container(
        col={'xs': 12, 'lg': 6}, # em telas pequenas vai ocupar 12 colunas, e em telas maiores 6 colunas
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER, # Alinha a forca ao centro
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, # Alinha horizontalmente ao centro
            controls=[
                victim,
                word
            ]
        )
    )

    # A imagem vai ocupar um tamanho de 12, ou seja toda a tela
    scene = ft.Image(col=12, src='images/scene.png')

    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6},
        image_src='images/keyboard.png',
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        image_fit=ft.ImageFit.FILL, # Para preencher todo o container
        padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
        content=ft.Row(
            wrap=True, # Para quando chegar no limite da tela, ele quebre para a linha de baixo
            alignment=ft.MainAxisAlignment.CENTER, # Para centralizar os caracteres do teclado
            vertical_alignment=ft.CrossAxisAlignment.CENTER, # Centraliza na vertical
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color=ft.colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                    ),
                    #bgcolor=ft.colors.ORANGE,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE], # Começa com a cor amber e termina em deep orange
                    ),
                    on_click=validate_letter
                ) for letter in string.ascii_uppercase
            ]
        )
    )

    layout = ft.ResponsiveRow( # Torna a row responsiva
        columns=12, # Tamanho da row é de 12 colunas
        controls=[
            scene,
            game,
            keyboard,
            scene,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
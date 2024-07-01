import flet as ft

def main(page: ft.Page):
    page.title = 'Contador' # Adiciona um titulo a página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Alinha todos os elementos da pagina no centro

    text_number = ft.TextField(value='0', text_align=ft.TextAlign.CENTER, width=100, disabled=True) # Declara o textField, alinha os valores ao centro, define um tamanho de 100 e desabilita a interação

    def minus_click(e): # Função para decrementar
        text_number.value = str(int(text_number.value) - 1)
        text_number.update()

    def plus_click(e): # Função para incrementar
        text_number.value = str(int(text_number.value) + 1)
        text_number.update()

    def reset_click(e): # Função para zerar
        text_number.value = '0'
        text_number.update()

    page.add( # Adiciona um controle (ou um conjunto de controles) á pagina
        ft.Row( # Organiza os controles em uma linha horizontal, 'Row' é um container que alinha seus filhos horizontalmente
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click),
                text_number,
                ft.IconButton(icon=ft.icons.ADD, on_click=plus_click),
                ft.IconButton(icon=ft.icons.DELETE, on_click=reset_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER, # alinha todos os controles horizontalmente no centro do Row.
        )
    )

    page.update() # Atualiza todas as mudanças

ft.app(target=main) # Para executar o app
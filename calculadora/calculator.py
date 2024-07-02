import flet as ft
from decimal import Decimal

botoes = [
    {'operador': 'AC', 'fonte': ft.colors.BLACK, 'fundo': ft.colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': ft.colors.BLACK, 'fundo': ft.colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': ft.colors.BLACK, 'fundo': ft.colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '7', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '8', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '9', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '*', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '4', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '5', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '6', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '-', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '1', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '2', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '3', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '+', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '0', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '.', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '=', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
]

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.window.resizable = False # Para não permitir que seja redimensionavel
    page.window.maximizable = False # Para não deixar maximizar a calculadora
    page.window.width = 360 # Define a largura
    page.window.height = 520 # Define a altura
    page.title = 'Calculadora Flet'
    page.window.always_on_top = True # Para ficar sempre visivel

    result = ft.Text(value='0', color=ft.colors.WHITE, size=30)

    def calculate(operador, value_at):
        try:
            value = eval(value_at) # Função para realizar a operação aritimética

            if operador == '%':
                value /= 100
            elif operador == '±': # Inverte o sinal
                value = -value
        except:
            return 'ZeroDivisionError'

        digits = min(abs(Decimal(value).as_tuple().exponent), 5) # Para controlar as casas decimais
        return format(value, f'.{digits}f')

    def select(e):
        value_at = result.value if result.value not in ('0', 'ZeroDivisionError') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value # Concatena com o valor anterior
        elif value == 'AC': # Zera a calculadora
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'): # Adiciona o operador no ultimo valor digitado
                value_at = value_at[:-1] # Adiciona o operador antes do valor numerico digitado

            value = value_at + value

            if value[-1] in ('=', '%', '±'):
                value = calculate(operador=value[-1], value_at=value_at)

        result.value = value
        result.update()

    display = ft.Row(
        width=360,
        controls=[result], # Adicionando o componente result dentro do display
        alignment='end', # Move o numero lá pro lado direito(final)
    )

    btn = [ft.Container(
            content=ft.Text(value=btn['operador'], color= btn['fonte'], size=20),
            width=70,
            height=70,
            bgcolor=btn['fundo'],
            border_radius= 100,
            alignment=ft.alignment.center, # Centraliza o texto
            on_click=select
        ) for btn in botoes]
    
    keyboard = ft.Row(
        width=360,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard)

if __name__ == '__main__':
    ft.app(target=main)
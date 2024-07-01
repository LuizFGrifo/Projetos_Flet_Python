import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.title = 'Markdown Editor' # Adiciona titulo a página
    def update_view(e):
        view.value = editor.value
        view.update()

    editor = ft.TextField(
        multiline=True, # Para permitir que escreva em mais de uma linha
        min_lines=30, # Minimo de linhas que ele vai aparecer de padrão'
        max_lines=30,
        color=ft.colors.BLACK,
        content_padding=ft.padding.all(30),
        border=ft.InputBorder.NONE,
        bgcolor=ft.colors.BLUE_GREY,
        on_change=update_view
    )

    how_to = ft.Container(
    expand=True,
    padding=ft.padding.all(30),
    content=ft.Column(
        scroll=ft.ScrollMode.ALWAYS, # Para permitir o scroll
        controls=[
            ft.Text(value='Para criar títulos em diferentes tamanhos', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            ft.Text(value='# H1', color=ft.colors.GREY_700),
            ft.Text(value='## H2', color=ft.colors.GREY_700),
            ft.Text(value='### H3', color=ft.colors.GREY_700),
            ft.Divider(color=ft.colors.GREY, height=40),

            ft.Text(value='Para formatar o estilo do texto', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            ft.Text(value='**Texto em negrito**', color=ft.colors.GREY_700),
            ft.Text(value='*Texto em itálico*', color=ft.colors.GREY_700),
            ft.Text(value='~~Texto tachado~~', color=ft.colors.GREY_700),
            ft.Divider(color=ft.colors.GREY, height=40),

            ft.Text(value='Para criar listas', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            ft.Text(value='- Item de lista não ordenada', color=ft.colors.GREY_700),
            ft.Text(value='1. Item de lista ordenada', color=ft.colors.GREY_700),
            ft.Divider(color=ft.colors.GREY, height=40),

            ft.Text(value='Para adicionar links', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            ft.Text(value='[Texto do link](http://exemplo.com)', color=ft.colors.GREY_700),
            ft.Divider(color=ft.colors.GREY, height=40),

            ft.Text(value='Para adicionar imagens', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            ft.Text(value='![Texto alternativo](http://caminho/para/imagem.jpg)', color=ft.colors.GREY_700),
            ft.Divider(color=ft.colors.GREY, height=40),

            ft.Text(value='Para adicionar código em linha', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            ft.Text(value='`código`', color=ft.colors.GREY_700),
            ft.Divider(color=ft.colors.GREY, height=40),

            ft.Text(value='Para adicionar blocos de código', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            ft.Text(value='```python\nprint("Olá Mundo!")\n```', color=ft.colors.GREY_700),
            ft.Divider(color=ft.colors.GREY, height=40),
        ]
    )
)

    view = ft.Markdown(
        value=editor.value,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme='monokai-sublime', # Para a funcionalidade de código
        on_tap_link=lambda e: page.launch_url(e.data),
    )

    layout = ft.Row(
        expand=True,
        spacing=0, # Remove os espaços entre os elementos
        # vertical_alignment=ft.CrossAxisAlignment.START, # Manda lá pro começo
        vertical_alignment=ft.CrossAxisAlignment.STRETCH, # Ocupa todo o espaço disponivel
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.colors.WHITE,
                content=ft.Column(
                    controls=[
                        editor,
                        how_to,
                    ]
                )
            ),
            ft.Container(
                expand=True,
                bgcolor=ft.colors.BLACK,
                padding=ft.padding.all(30),
                content=view
            ),
        ]
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)
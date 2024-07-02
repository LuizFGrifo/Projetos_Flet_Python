import flet as ft

def main(page: ft.Page):
    # page.window.maximizable = False # Para não permitir que seja maximizado o app
    page.padding = ft.padding.all(30)
    page.bgcolor = ft.colors.BLACK

    habits_list = [
        {'title': 'Estudar Flet', 'done': False},
        {'title': 'Procrastinar', 'done': False},
        {'title': 'Jogar', 'done': False},
    ]

    def change(e=None): # Para o parametro ser opcional
        if e:
            for habito in habits_list:
                if habito['title'] == e.control.label:
                    habito['done'] = e.control.value

        done = list(filter(lambda x: x['done'], habits_list))
        total = len(done) / len(habits_list)
        progress_bar.value = total
        progress_text.value = f'{total:.0%}'
        progress_bar.update()
        progress_text.update()

    def add_habit(e):
        habits_list.append({'title': e.control.value, 'done': False})
        habits.content.controls = [
            ft.Checkbox(
                label=habito['title'],
                value=habito['done'],
                on_change=change,
            ) for habito in habits_list
        ]
        habits.update()

        e.control.value = ''
        e.control.update()
        change()

    progress_text = ft.Text(value='0%', size=50, color=ft.colors.WHITE)
    progress_bar = ft.ProgressBar(
        value=0,
        color=ft.colors.INDIGO_900,
        bgcolor=ft.colors.INDIGO_100,
        height=20,
    )

    habits = ft.Container(
        expand=True,
        padding=ft.padding.all(30),
        bgcolor=ft.colors.GREY_900,
        border_radius=ft.border_radius.all(20),
        margin=ft.margin.symmetric(vertical=20),
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=20,
            controls=[
                ft.Checkbox(
                    label=habito['title'],
                    value=habito['done'], # Para iniciar com a caixa desmarcada
                    on_change=change,
                ) for habito in habits_list
            ]
        )
    )

    layout = ft.Column(
        expand=True,
        controls=[
            ft.Text(value='Que bom ter você aqui', size=30, color=ft.colors.WHITE),
            ft.Text(value='Como estão seus hábitos hoje?', size=20, color=ft.colors.GREY),

            ft.Container(
                padding=ft.padding.all(30),
                bgcolor=ft.colors.INDIGO,
                border_radius=ft.border_radius.all(20),
                margin=ft.margin.symmetric(vertical=30),
                content=ft.Column(
                    controls=[
                        ft.Text(value='Sua evolução hoje', size=20, color=ft.colors.WHITE),
                        progress_text,
                        progress_bar,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),

            ft.Text(value='Hábitos de hoje', size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text(value='Marcar suas tarefas como concluído te motiva a continuar focado', size=16, color=ft.colors.WHITE),

            habits,

            ft.Text(value='Adicionar novo hábito', size=20, color=ft.colors.WHITE),
            ft.TextField(
                hint_text='Escreva aqui um novo hábito...',
                border=ft.InputBorder.UNDERLINE, # Adiciona uma borda inferior
                on_submit=add_habit
            )

        ]
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)

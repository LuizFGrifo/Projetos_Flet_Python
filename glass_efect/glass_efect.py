import flet as ft

def main(page: ft.Page):
    page.padding= 0 # Para remover as bordas da imagem
    layout = ft.Container(
        image_src='https://arma3.com/assets/img/wallpapers/apex/1/Arma-3-Apex_wallpaper_2560%C3%971440.jpg',
        image_fit=ft.ImageFit.COVER, # Para preencher todo o espaço e se ajuste
        expand= True,
        alignment=ft.alignment.center,
        content=ft.Container(
            padding=ft.padding.symmetric(vertical=50, horizontal=80),
            border_radius=ft.border_radius.all(10),
            bgcolor=ft.colors.with_opacity(0.1,ft.colors.WHITE),
            border=ft.Border(
                top=ft.BorderSide(width=2, color=ft.colors.WHITE30),
                right=ft.BorderSide(width=2, color=ft.colors.WHITE30),
            ),
            blur=ft.Blur(sigma_x=5, sigma_y=5),
            content=ft.Text(
                value='ARMA III APEX',
                size=40,
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD,
            )
        )
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)
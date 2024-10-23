import flet as ft


def main(page: ft.Page):
    
    #Establecer tamaño  Pantalla
    page.window_width=300 
    page.window_width=300


    page.bgcolor="Black"
    page.title="Mictlan"
    page.bgcolor="grauy"
    
#Audios
    intro=ft.Audio(
        scr="Intro.mp3",volumen=1, balance=1
    )

    page.overlay.append(intro)
    
    Nivel1=ft.Audio(
        scr="Primer_Nivel.mp3", volumen=1, balance=0
    )
    page.overlay.append(Nivel1)
    
    Nivel2=ft.Audio(
        scr="Segundo_Nivel.mp3", volumen=1, balance=0
    )
    page.overlay.append(Nivel2)
    
    Nivel3=ft.Audio(
        scr="Tercer_Nivel.mp3", volumen=1, balance=0
    )
    page.overlay.append(Nivel3)
    
    Nivel4=ft.Audio(
        scr="Cuarto_Nivel.mp3", volumen=1, balance=0
    )
    page.overlay.append(Nivel4) 
    
    Nivel5=ft.Audio(
        scr="Quinto_Nivel.mp3", volumen=1, balance=0
    )
    page.overlay.append(Nivel5)
    
    Nivel6=ft.Audio(
        scr="Sexto_Nivel.mp3", volumen=1, balance=0
    )
    page.overlay.append(Nivel6)
    
    Nivel7=ft.Audio(
    )
    page.overlay.append(Nivel7)
    
    Nivel8=ft.Audio(
        scr="Octavo_Nivel.mp3", volumen=1, balance=0
    )
    page.overlay.append(Nivel8)
    
    Nivel9=ft.Audio(
        scr="Noveno_Nivel.mp3", volumen=1, balance=0
    )
    page.overlay.append(Nivel9)


ft.app(main)

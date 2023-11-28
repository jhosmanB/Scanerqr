import flet as ft
import device
import cv2
import scanner
def main(page: ft.Page):
    listaCamaras = device.getDeviceList()
    index = 0
    opciones = []
    for camara in listaCamaras:
         opciones.append(ft.dropdown.Option(camara[0]))
         index += 1

    def button_clicked(e):
        index = find_option_index(DropdownMenu.value)
        if index != -1:
            t.value = f"Camara  {index} seleccionada"
        else:
            t.value = f"No se selcciono ninguna camára"
        page.update()

    def find_option_index(option_name):
        index = 0
        for option in DropdownMenu.options:
            if option_name == option.key:
                return index
            index +=1
        return -1
    
    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    DropdownMenu =  ft.Dropdown(
            label="Cámaras",
            hint_text="Selecciona la camara para usar",
            options= opciones,
            autofocus=True,
        )
    
    page.add(DropdownMenu,b,t)
ft.app(target=main)

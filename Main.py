import device
import flet as ft
import manejadorUrls 
import manejadorExcel as excel
import scanner
import time
proceso_en_marcha = False

def main(page: ft.Page):
    def obtenerHojas(path):
        hojas = excel.listaHojas(path)
        opciones = []
        for hoja in hojas:
            opciones.append(ft.dropdown.Option(hoja))
        DPMenusheets = ft.Dropdown(
            label="Hojas",
            hint_text="Selecciona la hoja del documento",
            options= opciones,
            autofocus=True,)
        page.add(DPMenusheets,ft.ElevatedButton(
                    "Iniciar",
                    on_click=lambda _: construirArhivo(DPMenusheets,path),
                    key="iniciar",
                    data=proceso_en_marcha
                ))
        page.update()

    def construirArhivo(DPMenusheets,path):
      global proceso_en_marcha
      hoja = DPMenusheets.value
      if hoja != None : 
         columna = 1
         lista_urls = excel.leerColumna(path,hoja,columna)
         datos = []
         i = 0
         visitados = []
         pr = ft.ProgressRing(width=25, height=25, stroke_width = 5,color="red")
         texto = ft.Text("Espere hasta que termine el proceso", style="headlineSmall")
         proceso_en_marcha = True
         page.add(pr,texto)
         page.update()
         for url in lista_urls:
               buscar = -1
               try:
                  buscar = visitados.index(url) 
               except:
                   buscar = -1
               if buscar != -1:
                  datos.append(("Duplicado","Duplicado",0,buscar + 1))
               else:   
                  datos.append(manejadorUrls.ObtenerDatos(url))
                  visitados.append(url)   
         dir_archivo = "./resultadospus.xlsx"
         excel.CrearArchivo(dir_archivo)
         excel.EditarAarchivo(dir_archivo,datos)
         proceso_en_marcha = False
         page.remove(pr,texto)
         page.update() 
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
            pr = ft.ProgressRing(width=25, height=25, stroke_width = 5,color="red")
            texto = ft.Text("Espere hasta que termine el proceso", style="headlineSmall")
            page.add(pr,texto)
            page.update()
            scanner.escanear(index)
            page.remove(pr,texto)
            page.update() 
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
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value= e.files[0].path
        path=selected_files.value
        selected_files.update()
        if len(path) != 0:
            obtenerHojas(path)
    t = ft.Text()
    b = ft.ElevatedButton(text="iniciar camara", on_click=button_clicked)
    
    DropdownMenu =  ft.Dropdown(
            label="Cámaras",
            hint_text="Selecciona la camara para usar",
            options= opciones,
            autofocus=True,
        )
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    page.overlay.append(pick_files_dialog)
    page.add(DropdownMenu,b,t, ft.Row(
            [
                ft.ElevatedButton(
                    "Seleccionar archivo",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False,allowed_extensions=["xlsx"]
                    ),
                ),
                selected_files,
            ]
        ))
ft.app(target=main)

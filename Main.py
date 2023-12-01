import manejadorUrls 
import manejadorExcel as excel
import time
def main():
    path = "./facturas.xlsx"
    hoja = "septiembre "
    columna = 1
    lista_urls = excel.leerColumna(path,hoja,columna)
    urls = list(dict.fromkeys(lista_urls))
    datos = []
    i = 0
    for url in urls:
            datos.append(manejadorUrls.ObtenerDatos(url))
    dir_archivo = "./prueba.xlsx"
    excel.CrearArchivo(dir_archivo)
    excel.EditarAarchivo(dir_archivo,datos) 

main()
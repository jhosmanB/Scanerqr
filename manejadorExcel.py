import openpyxl
from openpyxl  import load_workbook
from openpyxl import Workbook

def CrearArchivo(path):
    libro =  Workbook()
    libro.save(path)

def EditarAarchivo(path,datos):
    libro = load_workbook(path)
    hoja = libro.active
    for row in datos:
     hoja.append(row)    
    libro.save(path)


import time
import cv2
from pyzbar.pyzbar import decode
import numpy as np
import manejadorUrls as manejador
import manejadorExcel as excel
camara = cv2.VideoCapture(1)


flag = True
urls = set()
while flag == True:
    success,frame = camara.read()
    if not success:
        break
    
    for code in decode(frame):
        decoded_data =code.data.decode('utf-8')
        rect_pts = code.rect

        if decoded_data:
            urls.add(str(decoded_data))
            print(str(decoded_data))
            pts = np.array([code.polygon],np.int32)
            cv2.polylines(frame,[pts], True , (255,0,0),3 )
            cv2.putText(frame,str(decoded_data),(rect_pts[0], rect_pts[1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)

    cv2.imshow("prueba",frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        flag = False
        datos = []
        datos.append(('NRO. DE FACTURA','MONTO'))
        for url in urls:
            datos.append(manejador.ObtenerDatos(url))
        path = "./prueba.xlsx"
        excel.CrearArchivo(path)
        excel.EditarAarchivo(path,datos) 
camara.release()
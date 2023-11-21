import cv2
from pyzbar.pyzbar import decode

def leer_qr():
    # Inicializar la cámara
    cap = cv2.VideoCapture(1)

    # Obtener el tamaño del frame
    _, frame = cap.read()
    height, width, _ = frame.shape

    # Definir las coordenadas del cuadrado en el centro
    centro_cuadrado = (width // 2, height // 2)
    tamano_cuadrado = 100  # Ajusta el tamaño del cuadrado según sea necesario

    while True:
        # Leer un frame desde la cámara
        ret, frame = cap.read()

        # Dibujar el cuadrado en el centro
        x1 = centro_cuadrado[0] - tamano_cuadrado // 2
        y1 = centro_cuadrado[1] - tamano_cuadrado // 2
        x2 = x1 + tamano_cuadrado
        y2 = y1 + tamano_cuadrado
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # Decodificar códigos QR dentro del cuadrado
        roi = frame[y1:y2, x1:x2]
        codigos_qr = decode(roi)

        # Dibujar los resultados
        for codigo_qr in codigos_qr:
            # Extraer la información del código QR
            data = codigo_qr.data.decode('utf-8')
            tipo = codigo_qr.type

            # Dibujar un rectángulo alrededor del código QR en el cuadrado
            puntos = codigo_qr.polygon
            if len(puntos) == 4:
                pts = []
                for punto in puntos:
                    pts.append((punto[0] + x1, punto[1] + y1))
                pts = tuple(pts)
                cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

                # Mostrar la información del código QR
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, f'{tipo}: {data}', (pts[0][0], pts[0][1] - 10), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

        # Mostrar el frame
        cv2.imshow('Lector QR', frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    leer_qr()
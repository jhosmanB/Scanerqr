Escanner basico de codigos QR especificos para las facturas que contenga un qr con url https://siat.impuestos.gob.bo/consulta/QR...
Realiza una busqueda de los datos en las tablas de la pagina web de impuestos 
si se realiza el escaneo  mediante camara, la camara se detiene medienate el  boton s del teclado
los resultados se guardan en un excel con el nombre "resultados.xlsx" en la carpeta raiz del proyecto
Para iniciar el progama ejecutar el archivo  Main.py


------------------------------------------------------------------

## Environment   
* [Microsoft Windows SDK][0]
* Python 3.6 or later

## How to Build the CPython Extension
- Create a source distribution:

    ```bash
    python setup.py sdist
    ```

- distutils:

    ```bash
    python .\setup_distutils.py build
    ```

- scikit-build:

    ```bash
    pip wheel . --verbos
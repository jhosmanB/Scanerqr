import requests
from bs4 import BeautifulSoup

def ObtenerDatos(url):
    response = requests.get(url)
    datos_factura = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')
        tables = soup.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            if rows:
                headers = [header.text.strip() for header in rows[0].find_all('th')]
                if len(headers) !=0:
                    index_factura = headers.index('NRO. DE FACTURA')
                    index_monto = headers.index('MONTO')

                    for row in rows [1:]:
                        data = [cell.text.strip() for cell in row.find_all('td')]
                        numero_factura = data[index_factura]
                        monto = data[index_monto]
                        datos_factura.append({'NRO. DE FACTURA': numero_factura, 'MONTO': monto})
    return datos_factura

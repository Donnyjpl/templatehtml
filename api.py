import requests

# Realizar la solicitud GET a la API REST
response = requests.get('https://aves.ninjas.cl/api/birds')[:5]

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Convertir la respuesta JSON en un diccionario de Python
    data = response.json()

    # Obtener la lista de aves
    lista_aves = data

    # Iterar sobre cada ave e imprimir su nombre y avatar
    for ave in lista_aves:
        print("Nombre en español:", ave['name']['spanish'])
        print("Nombre en inglés:", ave['name']['english'])
        print("Imagen principal:", ave['images']['main'])
        print()

else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error al obtener los datos de la API:", response.status_code)

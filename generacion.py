import requests

# Realizar la solicitud GET a la API REST
response = requests.get('https://aves.ninjas.cl/api/birds')

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Convertir la respuesta JSON en un diccionario de Python
    lista_aves = response.json()

    # Abrir el archivo HTML y leer su contenido
    with open('template.html', 'r') as file:
        template = file.read()

    # Generar el HTML con los nombres en español e Ingles y las imágenes
    estructura_html = "\n"
    for ave in lista_aves:
        estructura_html += "<div class='ave'>"
        estructura_html += f"<h1>Nombre en Español: {ave['name']['spanish']}</h1>"
        estructura_html += f"<h1>Nombre en Inglés: {ave['name']['english']}</h1>"
        estructura_html += f"<img src='{ave['images']['main']}' alt='foto de la aves'><br>"
        estructura_html += "</div>\n\n"

    # Agregar estilos CSS
    css_styles = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
            padding: 20px;
        }
        .ave {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
        }
        h1 {
            color: #333;
            margin-top: 0;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin-top: 10px;
        }
    </style>
    """

    # Reemplazar el marcador de posición en el template con el HTML generado y los estilos CSS
    final_html = template.replace('{{content}}', estructura_html + css_styles)

    # Guardar el HTML final en un archivo diferente al template => index.html
    with open('index.html', 'w') as file:
        file.write(final_html)

    print("Se ha creado el archivo 'index.html' con los nombres y las imágenes.")
else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error al obtener los datos de la API:", response.status_code)

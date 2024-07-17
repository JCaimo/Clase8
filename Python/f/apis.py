# import requests

# def obtener_clima(ciudad):
#     api_key = "api_key"
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
#     respuesta = requests.get(url)
    
#     if respuesta.status_code == 200:
#         datos = respuesta.json()
#         temperatura = datos['main']['temp']
#         descripcion = datos['weather'][0]['description']
#         print(f"El clima en {ciudad} es {descripcion} con una temperatura de {temperatura}°C.")
#     else:
#         print("No se pudo obtener el clima. Por favor, verifica la ciudad y el API key.")
#         print(f"Status Code: {respuesta.status_code}")
#         print(f"Mensaje de Error: {respuesta.json()}")

# # Prueba la función
# obtener_clima("Buenos Aires")

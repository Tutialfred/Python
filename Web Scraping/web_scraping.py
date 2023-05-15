        #todo                          PYTHON - WEB SCRAPING
        
#! Importando librerias
import re #expresiones regulares
from colorama import Fore  #colores
import requests #Para hacer peticiones http a uan pagina web

#! Extraer el html de una pagina web
website = "https://alfredozavala.netlify.app/"
result = requests.get(website)
content = result.text
print(content) #? Imprime todo el html ↑

#! Colores en la terminal a travez de la libreria 'Fore' 
color_yellow = Fore.YELLOW # Traer los colores
color_red = Fore.RED # Traer los colores
print(color_red + "Hola como estas?" + color_yellow + " Hi, How are you?") #? Imprimiendo texto con color




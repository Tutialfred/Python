# Python 
#Soy dalto



# Lenguaje de proposito general: se puede usar para cualquier actividad 
# Lenguaje de alto nivel 
# Facil de aprender
# Lenguaje de tipado dinamico
# Lenguaje orientado a objetos
# Lenguaje interpretado





# ! Tipos de datos 

# print("Hello World from python")

# print("""Hello World 
#       from python
#       Como Backticks en JS""")



# Booleanos siempre con mayuscula

True
False

# concatenar con 'f String'

nombre = "Tuti Zavala"
saludo = f"Hola {nombre} que tal?"

# print(saludo)

# Eliminar una variable

# snake_case
nombre_one = "Oscar"
del nombre_one #nombreOne ya no existe, esta decladrada pero no esta definida


# Operadores de pertenencia (in / not in)

frase = "Bienvenido a Italia, Fratello mio"

# print("Italia" in frase) #True
# print("Bienvenido" not in frase) #False






#! Datos compuestos

# Creando una lista or Matris (se puede modificar)
lista = ["Alfredo", "Zavala", True, 170.000, "i have to go to work"] #Tipo de datos === list

# Creando una tupla (no se puede modificar)
tupla = ("Alfredo", "Zavala", True, 170.000) #Tipo de datos === tupla

# Creando un conjunto (set) 
conjunto = {"Alfredo", "Zavala", True, 170.000} #Elementos desordenados
# No se accede a elementos por indice, no almacena datos duplicados


# Creando un diccionario (dict)
diccionario = { #Literal es lo mismo que un JSON, key : value
    # Mi pc now
    "Procesador": "AMD rizen 3",
    "Memoria Ram": 8,
    "Tarjeta Grafica" : False
} #Llamamos a ciertas variables por la clave de la propiedad 
# print(diccionario["Procesador"]) 

tipo_de_dato = type("String") #Nos devuelve que tipo de dato es 
# print(tipo_de_dato) #=== "str"

# Las divisiones siempre dan el resultado flotante (float) aunque de entero (int)
division = 12 / 6 #In this case is 2.0
# print(division)

# Potenciacion (exponente) (**)
exponente = 2 ** 4 #2 a la cuarta
# print(exponente)

# Division baja (//)
division_baja = 12 // 5
# print(division_baja) #Devuelve entero redondeado hacia abajo 
    
# resto o módulo
resto = 12 % 3 
# print(resto)





# ! Condicionales

edad = 20

if edad > 25 :
    print("Eres un adulto, pasa Ya!")
elif edad >= 18: 
    print("Ya eres mayor de 18")
else:
    print("no podes pasar")
print("siempre se va ejectuar esto")





#! Operadores logicos

# AND → &
# las dos condiciones deben de ser verdadero, solamente da true cuando ambas condicones dan True
print(True & True) #=== True

# OR → | 
# Aunque existe una condicion True da True, solamente da False cuando ambas condiciones dan False
print(False | True) #=== True

# NOT 
# Da el valor contrario como en javascript era "!true" ahora es con "not"
print(not True) #=== False


#! Métodos de String
name = "Alfredo Zavala"
numero = 750

# Convierte a Mayuscula
mayuscula = name.upper()

# Covierte a minuscula
minuscula = name.lower()

# Transforma todo en minuscula y deja la primera en Mayuscula
first_mayusculosa = name.capitalize()

# Buscamos una cadena dentro de otra cadena, si no hay coincidencias devuelve -1
busqueda_find = name.find("Alfredo")

# Buscamos una cadena dentro de otra cadena, si no hay coincidencias lanza una excepción
busqueda_index = name.index("Alfredo") 

# Devuelve True si el string contiene solo numeros, por lo contrario False
es_numerico = name.isnumeric()

# Devuelve True si el string contiene solamente texto y nada de caracteres especiales. ejemplo "HolaQueTal"
es_alpha_numerico = name.isalpha()

# Contamos coincidencias de una cadena dentro de otra cadena, devuelva la cantidad de coincidencias
contar_coincidencias = name.count("a")

# Contamos cuantos caracteres tiene una cadena 
contar_caracteres = len(name)

# Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = name.startswith("Alfre")

# Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = name.endswith("vala")

# Reemplaza un pedazo de la cadena dada, por otra dada. Si no la encuentra nos da la cadena anterior
cadena_new = name.replace("Alfredo" , "Tuti")

# Separar cadenas con la cadena que le pasemos
cadena_list = name.split(" ")

# Convertir a cadena de texto
cadena = str(numero)


#! Métodos de Lista

#Creando una nueva lista a travez de una funcion  
list_new = list(["Tuti", "Backend","Zavala", True, 170.000, "i have to go to work"])

# Ver la cantidad de elemetos de la lista
elements = len(list_new)

# Agregando un elemento a la lista === push
list_new.append("Last")

# Agregando un elemento a la lista pero en un indice especifico
list_new.insert(2, "Yes")

# Agregando varios elementos a la lista === Push
list_new.extend(["Number One", "Number Two", True])

# Eliminando un elemento de la lista por su indice
list_new.pop(2) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y así sucesivamente

# Removiendo un valor de la lista por su valor
list_new.remove("Number One")

# Eliminar todos los elementos de la lista
list_new.clear()

# Ordenando una lista (si usamos el parametro reverse=True lo ordena reversa)
list_new.sort(reverse=True) #False, True , 1, 3, 50, 800, 999

# Dar vuelta una lista
list_new.reverse()






#! Métodos de Diccionarios

me = {  "Full Name": "Alfredo Zavala",
        "Ages" : 21,
        "Country": "ARGENTINA",
        "Cash": 1.000
        }


# Devuelve las keys del diccionario
claves = me.keys()

# Devuelve el valor de la key que le pasemos
value_of_key = me.get("Country")

# Eliminando todos los elementos del diccionario
clean = me.clear()

# Eliminando un elemento del diccionario
element = me.pop("Ages")

# Obteniendo un elemento dict_items iterable
dic_iterable = me.items() #Poder usar bucles y otros más 





#! Entrada de datos - Inputs


# Pedirle los datos a un usuario
name = input("Tell me your name ") #int → para convertir un string "12" a dato numerico 12



#! Variables 2.0

# Creando una variable tomando los datos de una tupla
# Desempaquetado
datos = ("Alfredo", "Back-end", 700)
name, rol, money = datos


#todo: → 3 Formas de crear tuplas

# Con tuple
tupla = tuple(["info one", "info two"])

# Sin parentesis
tupla = "info one", "info two"

# Sin parentesis de un solo dato
tupla = "Info one", 

#todo: → 1 Formas de crear conjunto (set)

# Con set
conjunto = set(["number one", "number two"])

# Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Tuti", "Arias"])
conjunto2 = set([conjunto1, "objeto 2"])

#todo: → Teoria de los conjuntos
numbers1 = { 1,3,5,7}
numbers2 = { 1,3,7}


# Verificando si es un subconjunto
es = numbers2.issubset(numbers1) #* True
es = numbers2 <= numbers1 #* True

# Verificando si es un superconjunto
es = numbers2.issuperset(numbers1) #* False
es = numbers2 > numbers1 #* False

# Verificando si hay datos sin repetir
es = numbers1.isdisjoint(numbers2) #* False



# todo: → 4 Formas de crear diccionarios (dict)

# crear un diccionario con dict
diccionario = dict(name="tuti", business="Clothes or UNDEFINED")

# Las listas no pueden ser claves y usamos fronzenset para meter conjuntos a un diccionario
diccionario = {frozenset(["Name", "Nombre", "nome"]) : "Oscar Alfredo"}

# Creando diccionarios con fromkeys() → todas las keys con value 'none'
diccionario = dict.fromkeys(["Nombre", "edad", "Mail", "Numero"])

# Lo mismo que arriba pero con datos un dato especifico para todos
diccionario = dict.fromkeys(["Name", "lastname", "number"], "Sin-completar")



# ! Bucles 


import json
from src.utils import contarPares
from src.utils import comparoLista
from src.utils import replaceSpaceByGuion

x = 10

while x < 10:
    x = int(input("Enter a number: "))
    print(x)
    lista_pares = contarPares(x)
    print(lista_pares)
    print("Cantidad de numeros pares" )

print("Hola Mundo..")

frontend_data = '{ "name":"John", "age":30, "city":"New York"}'

parsed_data = json.loads(frontend_data)

print(parsed_data)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

json_converted_data = json.dumps(x)

print(json_converted_data)



# Tenemos como dato de entrada el dia hoy.
today = "Lunes"

if today == "Viernes":
  print("Se viene el fin de semana...")
elif today == "Lunes":
  print("Se viene el dia de trabajo...")
else:
  print("No se que dia es...")


print("nes" in today)

lista_pares = [2,4,6,8,10]

lista_impares = [3] + lista_pares

print(3 in lista_pares)
print(comparoLista(lista_pares, lista_impares))
print(comparoLista(lista_impares, lista_pares))
print(comparoLista(lista_impares, lista_impares))


listaA = [1,2,3,4,5]
listaB = [1,2,3,4,5]
matrix = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
print(matrix[1][3])

print(max(lista_impares))

n1, n2, n3, n4, n5 = listaA

print(n1)

stringDePrueba="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
replaced = replaceSpaceByGuion(stringDePrueba)
print(replaced)
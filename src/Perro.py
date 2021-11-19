class Perro:
    # Atributo de Clase
    genero= "Canis"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

myDog = Perro("Firulais", 5)

print(myDog.nombre)
print(myDog.edad)
print(myDog.genero)

Perro.genero = "Mamifero"

myOtherDog = Perro("Pepito", 15)

print(myOtherDog.nombre)
print(myOtherDog.edad)
print(myOtherDog.genero)
print(myDog.genero)
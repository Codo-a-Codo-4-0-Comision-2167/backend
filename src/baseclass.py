class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "says 'I'm an animal'")


class Perro(Animal):
    # Atributo de Clase
    genero= "Canis"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self):
        print("Guau Guau")
        self.__hablar()

    def __hablar(self):
        print("Hola, soy un perro")
    
    def __str__(self) -> str:
        pass


myInstance = Perro("Firulais", 3)

mySecondInstance = myInstance

myInstance.ladrar()

myInstance.__hablar()

print(myInstance.genero)
print(myInstance.nombre)


myInstance2 = Perro("Pepito", 19)

print(myInstance2.genero)
print(myInstance2.nombre)

Perro.genero = "Canis Lupus"

myInstance2.genero = "Canis"

print(myInstance2.genero)
print(myInstance.genero)
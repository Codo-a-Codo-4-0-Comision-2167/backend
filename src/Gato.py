from Animal import Animal

class Gato(Animal):
    def __init__(self, nombre="Bola de nieve"):
        self.nombre = nombre
    
    def speak(self):
        return "miau"
    
    def walk(self):
        return "miau-walk"
    
    def jump(self):
        return "miau-jump"
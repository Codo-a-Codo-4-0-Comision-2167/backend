from Alimento import Alimento

class Fruta(Alimento):
    def __init__(self, nombre, precio, cantidad):
        tipo = "Fruta" # restrinjo el tipo de alimento a fruta
        super().__init__(nombre, precio, cantidad, tipo)

myFruta = Fruta("Manzana", 10, 10)

print(myFruta.damePrecio())
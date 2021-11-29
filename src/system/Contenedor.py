# Este seria mi carrito de compras...
class Contenedor:
    
    def __init__(self) -> None:
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def remove(self, item):
        self.items.remove(item)
    
    def clean(self):
        self.items.clear()
    
    def getItems(self) -> list:
        return self.items
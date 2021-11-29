# Esta seria mi clase Usuario..
from Contenedor import Contenedor

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.contenedor = Contenedor()
    
    def addNewItem(self, item):
        self.contenedor.add(item)
from Admin import Admin
from src.system.User import User

class Sistema:

    def __init__(self) -> None:
        self.user_list = []
        self.admin = None
        self.reporter = None
        self.isRunning = True
    
    def add_user(self, user):
        self.user_list.append(user)
        self.admin.addNewItem(user)
    
    def add_admin(self, admin):
        self.admin = admin
    
    def create_user(self):
        return User(input("Ingrese nombre de usuario: "), input("Ingrese contraseña: "), input("Ingrese email: "))

    def create_admin(self):
        self.admin  = Admin(input("Ingrese nombre de usuario: "), input("Ingrese contraseña: "), input("Ingrese email: "))

    def run(self):
        while self.isRunning:
            option = int(input("Ingrese numero de opcion: "))
            if option == 0:
                self.isRunning = False
            elif option == 1:
               self.add_user(self.create_user())
            elif option == 2:
                self.add_admin(self.create_admin())

if __name__ == "__main__":
    sistema = Sistema()
    sistema.run()


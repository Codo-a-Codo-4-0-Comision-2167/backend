from User import User

class Admin(User):

    def __init__(self, username, password, email ) -> None:
        super().__init__(username, password, email)

    def addNewItem(self, userToWatch):
        self.contenedor.add(userToWatch)
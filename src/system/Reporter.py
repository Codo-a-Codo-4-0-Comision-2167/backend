from User import User

class Reporter(User):

    def __init__(self, username, password, email ) -> None:
        super().__init__(username, password, email)

    def addNewItem(self, contenedorToWatch):
        self.contenedor.add(contenedorToWatch)
from Gato import Gato
from Perro import Perro
from Pajaro import Pajaro

class Factory:

    @staticmethod
    def creadorDeAnimales(type):
        if type == "Perro":
            return Perro()
        elif type == "Gato":
            return Gato()
        elif type == "Pajaro":
            return Pajaro()
        else:
            return None
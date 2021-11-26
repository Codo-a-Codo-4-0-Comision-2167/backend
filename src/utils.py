from decorators import checkPositive
from decorators import myDecorator
from Gato import Gato
from Animal import Animal
from Factory import Factory

def contarPares(n):
    """ Funcion que cuenta pares hasta n """
    contador = [] # Es un array vacio...
    for i in range(n):
        if (i % 2) == 0:
            contador.append(i)

    return contador

# Si son iguales... devuelve 0
# Si a es mayor que b... devuelve 1
# Si a es menor que b... devuelve -1
def comparoLista( a, b):

  sizeA = len(a)
  sizeB = len(b)
  comparasion = 0

  if sizeA < sizeB:
    comparasion = -1
  elif sizeA > sizeB:
    comparasion = 1

  return comparasion

def replaceSpaceByGuion(string):
    """ Funcion que reemplaza los espacios por guiones """
    return string.replace(" ","-")

#@myDecorator
@checkPositive
def fibonacci(n):
    """ Funcion que calcula el fibonacci """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# __name__ nos ayuda a identificar si el script python
# que se esta ejecutando es el principal.
if __name__ == '__main__':
    print(fibonacci(10))
    try:
      print(fibonacci(-1))
    except Exception as e:
      print(e)
    
    myCat = Gato("Gato")
    myCat.speak()

    #myAnimal = Animal("Animal")
    #myAnimal.speak()

    myNewCat = Factory.creadorDeAnimales("Gato")

    print(myNewCat.speak())
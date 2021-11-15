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
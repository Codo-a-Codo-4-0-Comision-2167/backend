def checkPositive(func):
    """ Chequea que los parametros sean numeros positivos """
    def wrapper(x):
        if x < 0:
            raise ValueError("Value must be positive")
        return func(x)
    return wrapper


def myDecorator(func):
    """ Decorador que imprime el nombre de la funcion """
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper
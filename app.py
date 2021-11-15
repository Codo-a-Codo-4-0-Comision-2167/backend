# Crear una funcion que permita ingresar al usuario
# Numero enteros... y strings...
# 1- print -> imprime la lista que su fue cargando hasta el momento...
# 2- append a -> siendo a numero entero
# 3- remove b -> siendo b numero entero
# 4- sort
# 5- reverse
# 6- insert c d -> siendo ambos numeros enteros c le indice y d el valor
# 7- exit -> termina el programa

isRunning = True
myList = []

while isRunning:
    userInput = input("Ingrese comando: ")
    command = userInput.split()

    if command[0] == "exit":
        isRunning = False
    elif command[0] == "append":
        # Quizas debamos hacer un chequeo del input
        argumentos = command[1]
        if argumentos.isdigit():
            myList.append(int(argumentos))
    elif command[0] == "print":
        print(myList)
    elif command[0] == "sort":
        myList.sort()
    elif command[0] == "insert":
        myList.insert(int(command[1]),int(command[2]))
        #print("Se agrego",command[2],"en el indice",command[1])


# En Javascript teniamos las arrow functions que eran anonimas
#myFuncion = (x) => x**2

myFuncion = lambda x: x**2
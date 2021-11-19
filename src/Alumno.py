class Alumno:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso
    
    def __del__(self):
        pass

    def saluda(self):
        pass
        
    #def __str__(self):
    #    return f"{self.nombre} {self.apellido} {self.edad} {self.curso}"

myAlumno = Alumno("Juan", "Perez", 20, "Python")

print(myAlumno.nombre)

print(myAlumno) # si tiene __str__ se imprime el resultado de ese metodo

print(myAlumno.saluda())

myAlumno = None
class Estudiante:
    total_estudiantes = 0  # Contador de instancias

    def __init__(self, nombre, edad, cursos_inscritos):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos
        Estudiante.total_estudiantes += 1  # Aumenta el contador cada vez que se crea un estudiante

    def inscribir_cursos(self,curso:str):
        pass

    def mostrar_informacion(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def des_tupla(cls,tupla):
        pass

    def es_mayor_de_edad(self):
        pass

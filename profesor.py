class Profesor:
    total_profesores = 0  # Contador de instancias

    def __init__(self, nombre:str, especialidad:str, cursos_asignados:list[str]):
        self.nombre = nombre
        self.especialidad = especialidad
        self.cursos_asignados = cursos_asignados
        Profesor.total_profesores += 1  # Aumenta el contador cada vez que se crea un profesor

    def asignar_curso(self, curso:str):
        pass

    def mostrar_informacion(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @classmethod
    def desde_tupla(cls, tupla):
        pass

    @staticmethod
    def esta_disponible_para_nuevo_curso():
        pass
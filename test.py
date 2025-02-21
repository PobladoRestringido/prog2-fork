from estudiante import Estudiante
from horario import Horario
from profesor import Profesor
from curso import Curso

# Inicio ejecución
lucia = Estudiante('Lucia', 18, 'Inteligencia Artificial')
print(type(lucia))

curso = Curso('Inteligencia Artificial', 42, 'Lo odio')
print(curso.codigo)



class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        Horario.total_horarios += 1  # Aumenta el contador cada vez que se crea un horario

        def mostrar_horario(self):
            print(f'''
                Horario:
                Desde {self.hora_inicio} del {self.dia} hasta {self.hora_fin} del {self.dia}
        ''')

        def modificar_horario(self, nuevo_horario: dict):
            if Horario.es_horario_valido(nuevo_horario):
                self.dia = nuevo_horario[0]
                self.hora_inicio = nuevo_horario[1]
                self.hora_fin = nuevo_horario[2]
            else:
                print('No es un horario válido')

        def __str__(self):
            return f"El horario: {self.dia}, {self.hora_inicio}, {self.hora_fin}"
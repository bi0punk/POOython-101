class Human:
    #metodo init agrega atributos e inicializa estos mismos.
    #self referencia al objeto que se creara, (si mismo)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def watch(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')


human = Human('Caballo', 45)
human.watch()
human2 = Human('Mula', 21)
human2.watch()


print(type(Human))

####################################################################################

class Persona:
    def __init__(self):
        self.nombre = 'X'
        self.apellido = 'XX'
        self.edad = 111
person1 = Persona()
print(person1.nombre)
print(person1.apellido)
print(person1.edad)



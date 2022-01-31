class Human:
    #metodo init agrega artributos e inizializar atributos
    #self referencia al objeto que se creara, (si mismo)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def watch(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')


persona1 = Human('Caballo', 45)
persona1.watch()
persona2 = Human('Caballito', 21)
persona2.watch()


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



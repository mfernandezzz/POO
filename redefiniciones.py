#Ejemplo:
class MedioDeTransporte: #superclase
    def __init__(self, combustible):
        self.combustible = combustible

    def cargar_combustible(self, cantidad):
        self.combustible += cantidad
        print(f'Se ha cargado {cantidad} litros de combustible.')

    def entran_pasajeros(self, cantidad): #metodo que verifica si la cantidad de pasajeros es optima
        return cantidad <= self.maximo_pasajeros() #se llama al metodo maximo_pasajeros compartido por las subclases

class Auto(MedioDeTransporte): #sublclase
    def maximo_pasajeros(self):
        return 5 #maximo de pasajeros
    
    def rendimiento(self, km):
        self.combustible -= km * 0.5 #el auto consume medio litro de combustible por km

class Moto(MedioDeTransporte): #sublclase
    def maximo_pasajeros(self):
        return 2
    
    def rendimiento(self, km):
        self.combustible -= km #la moto consume un litro de combustible por km

class Colectivo(MedioDeTransporte):#subclase
    def __init__(self, combustible, nombreChofer):
        super().__init__(combustible) #se redefine el constructor original para agregar dos atributos
        self.pasajeros = 0
        self.nobreChofer = nombreChofer

    def sube_pasajero(self):
        self.pasajeros += 1
        print('Subiendo pasajero...')

    def maximo_pasajeros(self):
        return 20

    def rendimiento(self, km):
        self.combustible -= km * 2 #el colectivo consume dos litros por km

    def entran_pasajeros(self):
        return True #las instancias de esta clase siempre admitiran cualquier numero de pasajeros

    def cargar_combustible(self, cantidad):
        x = self.pasajeros #se guarda en una variable la cantidad de pasajeros antes de que bajen del omnibus
        print('Los pasajeros bajan del colectivo')
        self.pasajeros = 0 #para que se realice la carga de combustible, el omnibus no debe tener pasajeros a bordo
        super().cargar_combustible(cantidad) #se redefine el metodo original
        self.pasajeros = x #los pasajeros vuelven a subir al omnibus

ferrari = Auto(22)
motoneta = Moto(7)
omnibus = Colectivo(34, 'Jorge')

#¿Qué es la redefinición de métodos en la programación orientada a objetos?
#Personalizar o modificar el comportamiento de un método heredado en una subclase. Cuando se redefine un método en una subclase, se 
#proporciona una implementación específica para ese método en la subclase, lo que permite personalizar o modificar el comportamiento 
#original heredado de la superclase.

#¿Qué hace la función `super()` cuando se utiliza en la redefinición de métodos?
#Cuando se utiliza super(), puedes invocar el método de la superclase dentro de la subclase. Esto resulta útil cuando deseas agregar 
#funcionalidad adicional o personalizar parte del comportamiento heredado sin reemplazar por completo la funcionalidad original de la 
#superclase, lo que difiere de crear una "nueva implementación" desde cero.

#¿Cuál es uno de los beneficios de usar `super()` en la redefinición de métodos?
#Acceder y llamar al método de la superclase para extender o modificar su comportamiento. super() te permite acceder al método de la 
#superclase dentro de la subclase, lo que te permite extender o modificar el comportamiento heredado de la superclase sin reemplazarlo 
#por completo.

#¿Cuál es el propósito de la redefinición de métodos en una subclase?
#Personalizar o modificar el comportamiento heredado del método. Cuando redefinimos un método en una subclase, estamos permitiendo que 
#esa subclase proporcione su propia implementación del método, lo que le permite personalizar o modificar el comportamiento heredado 
#de la superclase según las necesidades específicas de la subclase.

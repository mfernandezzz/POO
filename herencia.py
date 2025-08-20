#En la POO, la herencia es la practica y/o capacidad de crear nuevas clases (sub-clases) basadas en clases preexistentes (super-clases). 
#Esto permite la reutilizacion del codigo y la organizacion de clases en una jerarquia coherente.

#¿Cuál es el propósito de una clase base (superclase)?
#Definir reglas generales compartidas por todas las clases derivadas. La clase base (superclase) tiene como propósito principal definir 
#reglas generales y comportamientos compartidos por todas las clases derivadas (subclases).

#¿Qué representa una clase derivada (subclase)?
#Una clase derivada (subclase) representa una instancia real y concreta de un concepto específico. A diferencia de una clase abstracta 
#que representa una idea general, una subclase es una implementación específica de esa idea en forma de objeto.

#Ejemplo:
class Dispositivo: #la superclase contiene a los metodos comunes que seran heredados a las sub-clases
    def __init__(self, bateria):
        self.bateria = bateria #el maximo de bateria debe ser 100 y el minimo 0

    def tiene_bateria(self):
        return self.bateria > 20 #comprueba si la bateria es mayor a 20
    
    def cargar_a_tope(self):
        self.bateria = 100 #se carga la bateria al maximo
        print('Bateria Cargada.')

    def tiene_bateria_maxima(self):
        return self.bateria == 100 #comprueba si la bateria esta al maximo
    
    def sin_carga(self):
        return self.bateria == 0 #comprueba si el dispositivo esta sin carga
    
    def carga_rapida(self, minutos): #metodo para cargar el dispositivo en x minutos (no es realista, no todos los dispositivos pueden cargarse en el mismo tiempo)
        if self.bateria < 0: #se comprueba que el valor para la bateria no sea negativo
            self.bateria = 0 #si la bateria tiene un valor de carga negativo, se le asigna cero
        self.bateria += (minutos * 2) #la bateria se carga al doble de los minutos establecidos

class Tablet(Dispositivo): #sub-clase tablet hereda de la super-clase dispositivo
    def utilizar(self, minutos): 
        if self.bateria > 100: #se comprueba si el valor de bateria es mayor a 100
            self.bateria = 100 #en caso afirmativo, el maximo de bateria es 100
        self.bateria -= (minutos / 2) #la bateria se reduce a la mitad de los minutos que fue utilizado el dispositivo
    
class Notebook(Dispositivo):
    def utilizar(self, minutos):
        if self.bateria > 100:
            self.bateria = 100
        self.bateria -= minutos #la bateria se reduce en los minutos que fue utilizado el dispositivo

una_tablet = Tablet(50)
una_notebook = Notebook(80)

#Ejemplo 2:
class Vehiculo:
    def __init__(self, combustible, capacidad_tanque=20):
        self.combustible = combustible  
        self.capacidad_tanque = capacidad_tanque  

    def necesita_combustible(self):
        return self.combustible < (self.capacidad_tanque * 0.2)  #Menos del 20% se considera bajo

    def llenar_tanque(self):
        self.combustible = self.capacidad_tanque #se llena el tanque hasta el maximo

class Moto(Vehiculo):  #Moto hereda de Vehiculo
    pass  #No agregamos métodos nuevos, pero hereda los de Vehiculo

moto_de_ana = Moto(combustible=2, capacidad_tanque=15)

#Ejemplo 3:
class Zombie:
    def __init__(self, hambre):
        self.hambre = hambre

    def sabe_correr(self):
        return True
    
    def es_peligroso(self):
        return self.hambre > 50 #es peligroso si su hambre es mayor a 50
    
    def recibir_danio(self, danio):
        self.hambre -= danio * 2 #reduce su hambre en el doble del daño recibido
        print('El zombie recibe daño')

    def descansar(self, minutos):
        self.hambre += minutos #aumenta su hambre en la cantidad de minutos descansados
        print('El zombie descansa')

class SuperZombie(Zombie): #hereda de Zombie
    def es_peligroso(self):
        return True #el superzombie siempre es un peligro
    
    def recibir_danio(self, danio):
        self.hambre -= danio #reduce se hambre en el daño recibido
        print('El superzombie recibe daño')

    def puede_regenerarse(self):
        self.hambre = 100 #aumenta su hambre al maximo
        print('El superzombie se regenera')

z1 = Zombie(60)
z2 = Zombie(40)
sz1 = SuperZombie(20)

#Dispositivo es una clase concreta. -Falso
#Dispositivo es una clase abstracta. -Verdadero
#Tablet es una clase concreta. -Verdadero
#Notebook es una clase abstracta. -Falso
#Tablet hereda de Dispositivo. -Verdadero
#Dispositivo hereda de Notebook. -Falso
#Notebook hereda de Dispositivo. -Verdadero
#Las clases abstractas sirven para proveer comportamiento a las subclases. -Verdadero
#Las clases concretas se usan para crear instancias. -Verdadero

#Las clases abstractas proporcionan una estructura común y definen métodos que deben ser implementados por las clases que las heredan.
#La abstraccion permite establecer jerarquias de clases por herencia, que le dan coherencia y orden al codigo. Las clases abstractas 
#(no instanciables) definen la estructura, mientras que las clases concretas se encargan de los detalles. Finalmente, las instancias
#tendran caracteristicas de ambas.

#Paradigma: en programacion, corresponde a una forma de pensar y estructurar el codigo; un conjunto de principios y practicas que
#preceden a la resolucion de problemas. Cada Paradigma tiene sus propias caracteristicas, lo que permite abordar diferentes tipos
#de problemas en diferentes contextos. Uno de los paradigmas mas populares y utilizados es la Programacion Orientada a Objetos.

#POO (programacion orientada a objetos): paradigma que se enfoca en organizar el codigo entorno a las entidades llamadas "objeto" y a
#las relaciones entre ellas. Estos objetos pueden ser representaciones del mundo real o de las necesidades que plantee una solucion. 
#Cada objeto posee propiedades y atributos propios. Un objeto automovil puede tener propiedades como Color - Cant. Puertas - Potencia 
#y sus atributos pueden ser Acelerar - Frenar - Enc Luces. La POO tambien trabaja con objetos provenientes de conceptos intangibles, 
#como un objeto "Cuenta Bancaria" con propiedades como Numero - Saldo - Titular y atributos como Depositar - Verificar - Retirar.

primos = [2, 3, 5, 7] #objeto de tipo lista
primos.append(11) #el mensaje
print(primos)
#En Python todo es un objeto, incluidos los strings y las listas. Primos es un objeto de tipo lista que entiende el mensaje append.
42 #int
"Python" #string
False #boolean
[2, 5, 7] #list
{"marca": "Toyota", "modelo": "Corolla", "año": 2020} #dictionary

#Objetos y referencias
#Cuando se crea un objeto en Python, se le asigna un espacio en memoria, y cuando se crea un nuevo objeto en base a el, lo que se hace
#es referenciarlo. Las variables son vistas como cajas (espacio de almacenamiento) con etiquetas (nombre de la variable). Al referenciar 
#un nuevo objeto, lo que ocurre es que se pone una segunda etiqueta a la misma caja. Esto implica que si se modifica el “segundo objeto”, 
#el “primero” también es modificado, ya que en realidad, el objeto guardado es el mismo.

#Por ejemplo, un objeto puede tener dos referencias, por lo que al cambiar alguna propiedad a través de una de las referencias, el
#cambio se evidencia al leer esa propiedad desde cualquiera de las referencias. Esto no es lo mismo que decir que dos objetos son iguales.
#Con algunos tipos de datos en Python (los llamados datos primitivos: bool, int, float y string) los datos siempre serán referenciados. 

#Diferencia entre datos primitivos (int) y datos complejos (list):
#primitivos
num1 = 5
num2 = 5
print(num1 is num2) #True
print(num1 == num2) #True

#complejos
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(lista1 is lista2) #False
print(lista1 == lista2) #True

lista1 = [1, 2, 3]
lista2 = lista1
print(lista1 is lista2) #True
print(lista1 == lista2) #True

fontanero = "Mario"
hermano_de_mario = "Luigi"

mario = fontanero
super_mario = mario
luigi = hermano_de_mario

print(mario is fontanero) #True
print(mario is super_mario) #True
print(luigi is hermano_de_mario) #True
print(mario is hermano_de_mario) #False

#Ejemplo de creacion de una clase:
class Auto:
    def __init__(self, combustible, capacidad_tanque = 50):
        self.combustible = combustible  #Nivel de combustible en litros
        self.capacidad_tanque = capacidad_tanque #capacidad maxima del tanque en litros

    def necesita_combustible(self): #mensaje
        return self.combustible < 10 #Supongamos que menos de 10 litros es considerado bajo
    
    def tiene_tanque_lleno(self):
        return self.combustible == self.capacidad_tanque #Devuelve True si el tanque esta lleno
    
    def llenar_tanque(self):
        self.combustible = self.capacidad_tanque #Llena el tanque completamente

auto_de_luis = Auto(7) #objeto
print(auto_de_luis.tiene_tanque_lleno())
print(auto_de_luis.necesita_combustible()) 
auto_de_luis.llenar_tanque()
print(auto_de_luis.tiene_tanque_lleno())

#¿Que es la interfaz en la POO?
#Conjunto de mensajes que se le pueden enviar a un objeto.

#¿Que hace el operador is?
#El operador is se utiliza para verificar si dos objetos tienen la misma referencia en memoria, lo que significa que apuntan al
#mismo objeto.

#¿Que es una referencia en Python?
#En Python, una referencia es una direccion de memoria que apunta a un objeto en lugar de contener directamente los datos del objeto.

#Mensajes y metodos: forma en que los objetos interactuan entre si a traves de funciones y procedimientos.
#Interfaz compartida: Mecanismo que permite a varias clases tener metodos en comun.

#En la POO, los objetos interactuan mediante el envio de mensajes. Estos mensajes son solicitudes para que un objeto realice
#acciones o proporcione informacion. Los mensajes se envian utilizando "objeto.mensaje()". El metodo input en POO permite recibir
#y transformar datos para su uso.

#Sintaxis para la creacion de una clase en Python
class Persona:
    def __init__(self, peso, nombre, edad, ocupacion):#constructor que inicializa los valores de las propiedades de un objeto.
        self.peso = peso #atributos: variables que almacenan informacion de un objeto. Caracteristicas que tendra el objeto.
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
#El estado de un objeto es el conjunto de atributos que definen sus caracteristicas.
    def trotar(self): #metodo: solicitud o instruccion para realizar una accion especifica.
        print('trotando...')

persona1 = Persona(84, 'Julian', 44, 'Enfermero')
persona2 = Persona(82, 'Marcelo', 38, 'Administrativo')
print(persona1.edad)
print(persona2.ocupacion)#acceder a los atributos de un objeto
persona1.trotar()#acceder a los metodos de un objeto
print(persona1)  #se devuelve en consola la direccion de la memoria RAM donde esta almacenado ese objeto.

#La Clase es como un "molde" abstracto que define como se crearan los objetos.
#La palabra reservada init inicializa las propiedades del objeto al crear una instancia de la clase.
#La palabra reservada Self hace referencia al objeto instanciado.
 
class Celular:
    def __init__(self, bateria, saldo, sistema_operativo):
        self.bateria = bateria
        self.saldo = saldo
        self.sistema_operativo = sistema_operativo
    
    def tiene_bateria_maxima(self):
        return self.bateria == 100
    
    def cargar_a_tope(self):
        self.bateria = 100
        print('Bateria cargada')

    def necesita_saldo(self):
        return self.saldo == 0
    
    def depositar_saldo(self, saldo):
        self.saldo = saldo
        print(f'Se acreditaron {saldo}$ de saldo.')

celular_de_ana = Celular(30, 0, 'Android 12') #objeto
print(celular_de_ana.tiene_bateria_maxima()) #False
celular_de_ana.cargar_a_tope() 
print(celular_de_ana.necesita_saldo()) #True
celular_de_ana.depositar_saldo()
print(celular_de_ana.necesita_saldo()) #False
print(celular_de_ana.sistema_operativo)

#¿Cual es el orden correcto para la creacion de una instancia de un objeto en Python?
#Crear una clase - Declarar un constructor utilizando la palabra reservada __init__ - Utilizar el constructor para crear una 
#instancia de la clase.

#Las clases son plantillas que definen objetos con atributos (datos) y metodos (comportamientos) compartidos. Las clases tienen
#atributos que representan caracteristicas del objeto y definen su estado. Los metodos describen las acciones que los objetos pueden 
#realizar.

#Interaccion entre dos objeto tipo personas
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self, receptor): #receptor recibe como parametro un objeto
        return(f'Que tal {receptor.nombre}, mi nombre es {self.nombre} y tengo {self.edad} años.')

    def responder(self, receptor):
        return(f'Un gusto {receptor.nombre}, mi nombre es {self.nombre} y tengo {self.edad} años.')

persona1 = Persona('Lautaro', 48)
persona2 = Persona('Ernesto', 50)

#print(persona1.presentarse(persona2))
#print(persona2.responder(persona1))

class Caballo:
    def __init__(self, energia, raza):
        self.energia = energia
        self.raza = raza

    def comer(self, gramos):
        self.energia += gramos * 2 #su energia aumenta al doble de los gramos digeridos
        print('Comiendo...')

    def galopar(self, kms):
        self.energia -= kms #reduce su energia segun la cantidad de kilometros recorridos
        print('Galopando...')

mi_caballo = Caballo(500, 'Arabe')
print(mi_caballo.energia)
mi_caballo.comer(1800)
print(mi_caballo.energia)
mi_caballo.galopar(27)
print(mi_caballo.energia)

class Golondrina:
    def __init__(self, energia, ciudad):
      self.energia = energia
      self.ciudad = ciudad #la ciudad en la que se encuentra la Golondrina

    def comer(self, gramos):
       self.energia += (gramos * 0.5) #su energia aumenta en la mitad de los gramos ingeridos
       print('Comiendo...')

    def volar_hacia(self, destino):
       self.ciudad = destino #cambia la ciudad actual de la Golondrina
       self.energia -= (self.energia * 0.5) #su energia se reduce a la mitad
       print('Volando...')
    
golondrina_random = Golondrina(85, 'Montevideo')
print(f'Energia de la Golondrina: {golondrina_random.energia}. Su ciudad actual es: {golondrina_random.ciudad}')
golondrina_random.comer(500)
print(golondrina_random.energia)
golondrina_random.volar_hacia('Maldonado')
print(f'Energia de la Golondrina: {golondrina_random.energia}. Su ciudad actual es: {golondrina_random.ciudad}')

class Gato:
    def __init__(self, energia, edad):
        self.energia = energia
        self.edad = edad

    def comer(self, gramos):
        self.energia += gramos #su energia aumenta en la cantidad de gramos ingeridos

    def cumplir_anios(self):
        self.edad += 1

un_gato = Gato(110, 4)
un_gato.comer(float(input('Cantidad de comida consumida por el gato en gramos: ')))
un_gato.cumplir_anios()
print(f'Energia del gato: {un_gato.energia}. Edad del gato: {un_gato.edad}')

#¿Qué elementos principales se representan en un diagrama de clases?
#Los diagramas de clases en POO se utilizan para modelar la estructura de un sistema, mostrando las clases, sus atributos, metodos y 
#las relaciones entre ellas.

#¿Cuál es la función principal del método constructor "init" en una clase de Python?
#Inicializar las propiedades del objeto al crear una instancia de la clase.

#¿Por qué no es necesario pasar el parámetro "self" al llamar a un método desde un objeto?
#Python agrega automáticamente el parámetro "self" al llamar a un método desde un objeto. No es necesario pasarlo manualmente.

#¿Qué palabra clave se utiliza en un método para hacer referencia al objeto en sí mismo?
#En Python, se utiliza la palabra clave "self" para hacer referencia al objeto en sí mismo dentro de sus métodos.


#alt
#Asi como con la palabra def se pueden crear funciones, con la palabra reservada class se pueden crear clases o variables
#propias. 
#Tipo de variable que se llama Persona que tiene un nombre y un dato de altura.
class Persona():
    def __init__(self):
        self.nombre = 'sin nombre'
        self.altura = 0

#Ahora se puede empezar a crear variables de esta clase y modificar sus valores.
persona1 = Persona()
persona1.nombre = 'Alicia'
persona1.altura = 1.70
print(f'Nombre: {persona1.nombre}')
print(f'Altura: {persona1.altura}')
#Se puede crear variables de este tipo tanto como se quiera
persona2 = Persona()
persona2.nombre = 'Julian'
persona2.altura = 1.85
print(f'Nombre: {persona2.nombre}')
print(f'Altura: {persona2.altura}')
#A las variables creadas a partir de clases tambien se les llama objetos.
#A las funciones de una clase tambien se las conoce como metodos.

#Una clase tambien puede tener funciones
class Persona():
    def __init__(self):
        self.nombre = 'sin nombre'
        self.altura = 0
        self.peso = 0

    def indice_masa_corporal(self):
        imc = self.peso / (self.altura**2)
        return imc
#Notemos que las funciones que estan dentro de las clases siempre el primer parametro que reciben corresponde a la variable
#creada con ella. Por convencion se le da el nombre de self, que significa yo mismo en ingles.

persona3 = Persona()
persona3.nombre = 'Jorge'
persona3.altura = 1.92
persona3.peso = 88
print(f'Nombre: {persona3.nombre}, Altura: {persona3.altura}m, Peso: {persona3.peso}kg')
print(f'Indice de masa corporal: {persona3.indice_masa_corporal()}')

#Ejercicio: crear nuevamente la clase Persona, pero esta vez ademas de la funcion de imc (self), crear otra llamada 
#diagnostico de imc (self, maximo) que reciba el parametro maximo y que devuelva el string 'Correcto' si el indice de masa
#corporal es menor a maximo. De lo contrario, debe devolver obesidad.
class Persona():
    def __init__(self):
        self.nombre = 'sin nombre'
        self.altura = 0
        self.peso = 0

    def indice_masa_corporal(self):
        imc = self.peso / (self.altura**2)
        return imc
    
    def diagnostico_de_IMC(self, maximo):
        maximo = 25
        if self.indice_masa_corporal() <= maximo:
            return('Correcto')
        else:
            return('Obesidad')
        
persona01 = Persona()
persona01.nombre = 'Carlos'
persona01.altura = 1.78
persona01.peso = 85
maximo = 25
print(f'El indice de masa corporal para {persona01.nombre} es: {persona01.indice_masa_corporal()}')
print(f'El diagnostico de IMC para {persona01.nombre} es: {persona01.diagnostico_de_IMC(maximo)}')

#La funcion def _init_(self): es una funcion especial en donde se crean las variables que va a tener dicha clase y que solo
#se ejecuta una vez al crear una variable de ese tipo.
class Individuo():
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

    def indice_masa_corporal(self):
        imc = self.peso / (self.altura**2)
        return imc
    
    def diagnostico_de_imc(self, maximo):
        maximo = 25
        if self.indice_masa_corporal() <= maximo:
            return('Correcto')
        else:
            return('Obesidad')
        
individuo01, maximo = Individuo('Teo', 1.79, 74), 25
print(f'Altura: {individuo01.altura}, Peso: {individuo01.peso}')
print(f'La persona {individuo01.nombre} tiene un indice de masa corporal de {individuo01.indice_masa_corporal()}')
print(f'Su diagnostico de IMC es {individuo01.diagnostico_de_imc(maximo)}')
#La funcion init nos obliga a pasar los parametros que necesita para crear una variable de dicha clase. De lo contrario dara 
#error.

#Extender las variables y funciones de una clase
#Las clases se pueden extender heredando todas las variables y funciones de otra clase.
class Tenista(Individuo):
    def __init__(self, nombre, altura, peso, victorias, derrotas):
        super().__init__(nombre, altura, peso)
        self.victorias = victorias
        self.derrotas = derrotas
#Al poner Individuo en los parentesis de la clase Tenista, se esta diciendo que esta clase va a tener todas las variables y
#funciones de la clase Individuo y que ademas se le sumaran nuevas variables.
#Debajo del _init_() de la clase Tenista aparece una funcion super()._init_() que lo que hace es ejecutar la funcion
#_init_() de la clase Individuo.
tenista01, maximo = Tenista('George', 1.85, 80, 10, 2), 25
print(f'Nombre: {tenista01.nombre}, Altura: {tenista01.altura}, Peso: {tenista01.peso}')
print(f'Victorias: {tenista01.victorias}, Derrotas: {tenista01.derrotas}')
print(f'El indice de masa corporal de {tenista01.nombre} es: {tenista01.indice_masa_corporal()}')
print(f'El diagnostico de IMC del tenista {tenista01.nombre} es: {tenista01.diagnostico_de_imc(maximo)}')

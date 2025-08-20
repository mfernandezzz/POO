#Refiere a la capacidad de diferentes objetos de clases distintas para responder al mismo metodo o funcion de manera coherente. Se puede 
#tratar varios objetos diferentes de manera uniforme si comparten un comportamiento comun.
#En la POO, significa que se puede utilizar una interfaz comun para objetos que pertenecen a diferentes clases, siempre y cuando
#implementen los mismos metodos. 

#Para estar ante un caso de polimorfismo, es necesaria la presencia de un objeto que envíe el mensaje y dos de clases distintas que 
#puedan entenderlo.

#En Python, cuando queremos que un metodo no haga nada, simplemente se coloca la palabra pass. De esta forma. el objeto entendera el
#mensaje pero no devolvera nada, evitando asi que se muestre un error en consola.

#Ejemplo 1
class FeedInstagram:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion
        self.me_gusta = 0

    def interactuar(self):
        self.me_gusta += 1
        print('Has dado un me gusta')

class ReelInstagram:
    def __init__(self, id, duracion):
        self.id = id
        self.duracion = duracion

    def interactuar(self):
        print('Reel visualizado')

feed = FeedInstagram(20, 'Mirando el feed')
reel = ReelInstagram(55, '18 segundos')
#los dos objetos responderan al metodo en comun interactuar() pero responderan de manera diferente.

#Ejemplo 2
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def obtener_area(self):
        print(self.radio * 3.14 ** 2)
    
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def obtener_area(self):
        print(self.base * self.altura)

un_circulo = Circulo(2)
un_rectangulo = Rectangulo(14, 8)

def obtener_figura(figura): #la funcion recibe como parametro el objeto para llamar a su metodo y devolver su area
    return (f'El area de la figura es: {figura.obtener_area()}')
obtener_figura(un_circulo)
obtener_figura(un_rectangulo)

#Ejemplo 3
class AsistenteDeZoologico:#no tiene atributos propios pero si metodos
    def alimentar(self, animal, cantComida): #metodo alimentar
        animal.comer(cantComida) #llama al metodo comer compartido por el leon y el elefante 
        print('Animal alimentado')
    
    def rehabilitar(self, animal):
        animal.recibir_rehabilitacion()#llama al metodo recibir_rehabilitacion compartido por todos los animales

    def dar_alta_medica(self, animal): #los animales solo pueden recibir alta medica si estan felices
        return animal.esta_feliz() #se llama al metodo compartido por los otros objetos y se devuelve su valor booleano
    
class Leon:
    def __init__(self, energia):
        self.energia = energia

    def comer(self, gramos):
        self.energia += gramos #el leon aumenta su energia en la cantidad de gramos digeridos
        print('Comiendo...')
    
    def recibir_rehabilitacion(self):
        if self.energia < 5000: #si tiene energia insuficiente, se llama al metodo comer
            self.comer(500) #el metodo comer posee un valor por defecto
            print('Recibiendo rehabilitacion.')
        else:
            print('No necesita rehabilitacion') #si su energia es suficiente, no necesita rehabilitacion

    def esta_feliz(self):
        return self.energia > 3000 #el leon necesita 3000 de energia como minimo para estar feliz

class Elefante:
    def __init__(self, energia):
        self.energia = energia
        self.comidaConsumida = 0

    def comer(self, gramos):
        self.energia += gramos #su energia aumenta en la cantidad de comida consumida en gramos
        self.comidaConsumida += gramos #aumenta su energia en la cantidad de gramos de comida consumidos
        print('Comiendo...')

    def recibir_rehabilitacion(self):
        if self.energia < 5000:
            self.comer(1000)
            print('Recibiendo rehabilitacion.')
        else:
            print('No necesita rehabilitacion.')

    def esta_feliz(self):
        return self.comidaConsumida > 2000 #el elefante necesita haber consumido al menos 2000 gramos de comida para estar feliz

class Mono:
    def __init__(self, energia):
        self.energia = energia
        self.horasDescanso = 0

    def descanso(self, horas):
        self.energia += (horas * 100) #el mono recupera su energia en la cantidad de horas dormidas * 100
        self.horasDescanso += horas
        print('Descansando...')

    def recibir_rehabilitacion(self):
        if self.energia < 5000: #si su energia es insuficiente
            self.descanso(2) #se llama al metodo descanso con un valor predeterminado
            print('Recibiendo rehabilitacion.')
        else:
            print('No necesita rehabilitacion.')

    def esta_feliz(self):
        return self.horasDescanso >= 5 #el mono necesita haber descansado como minimo 5 horas para estar feliz
            
asistente = AsistenteDeZoologico()
simba = Leon(2000)
donkey = Mono(4800)
dumbo = Elefante(500)

#Ejemplo 4 
class Cazador:
    def __init__(self, destreza):
        self.destreza = destreza

    def enfrentar(self, criatura):
        if criatura.es_un_peligro(): #se llama al metodo compartido por todos los demas objetos
            print('Es demasiado peligroso enfrentarlo')
        else:
            self.destreza += 10 #si la criatura no es un peligro, aumenta la destreza del cazador en 10
            print('El cazador enfrenta la criatura')

class LoboOscuro:
    def __init__(self, muertes):
        self.muertes = muertes

    def es_un_peligro(self):
        return self.muertes > 3 #es un peligro si ha matado mas de 3 veces
    
class Zombi:
    def __init__(self, hambre):
        self.hambre = hambre

    def es_un_peligro(self):
        return self.hambre > 50 #es un peligro si su hambre es mayor a 50
    
class Vampiro:
    def __init__(self, sed_sangre):
        self.sed_sangre = sed_sangre

    def es_un_peligro(self):
        return self.sed_sangre > 30 #es un peligro si su sed de sangre es mayor a 30
    
cazador = Cazador(20)
loboNegro = LoboOscuro(8)
zombi01 = Zombi(40)
vampiro = Vampiro(45)

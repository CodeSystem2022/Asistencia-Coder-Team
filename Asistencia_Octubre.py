
#-------------Alumna: Verónica Cardenas-----------------

class Cubo:
     def __init__(self,ancho, alto, profundidad):
          self.ancho = ancho
          self.alto = alto
          self.profundidad = profundidad

     def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad
ancho = int(input('Ingrese el valor del ancho: '))
alto = int(input('Ingrese el valor del alto: '))
profundidad = int(input('Ingrese el valor de la profundidad: '))

cubo1 = Cubo(ancho,alto,profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')


#-------------Alumno: Gonzalo Quiroga   -----------------

class Rectangulo:
    '''
    crear una clase llamada rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular area utilizando la formula:
    area = base * altura
    pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser 3
    '''

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura


base = int(input("Digite el numero para la base del rectangulo: "))
altura = int(input("Digite el numero para la altura del rectangulo: "))
rectangulo1 = Rectangulo(base, altura)
print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")


#-------------Alumno: Adan Gomez   -----------------
class Vehiculo:
    """"
    Definir una clase padre llamada vehiculo y dos clases hijas llamadas
    auto y bicicleta, las cuales heredan de la clase padre vehiculo. La clase
    padre debe tener los siguientes atributos y metodos:
    Vehiculo(clase padre)
    -Atributos(color,rueda)
    -Metodos(__init__(color, rueda) y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(veloidad (km/hr))
    -Metodos(__init__(color, rueda, velocidad) y __str__())

     Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(montaaña/urbana/etc..)
    -Metodos(__init__(color, rueda, tipo) y __str__())

    Crear un objeto de cada clase
    """

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)


class Auto(Vehiculo):
    def __int__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ", Velocidad(km/hr): " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __int__(self, color, ruedas, tipo):
        super().__int__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", Tipo: " + self.tipo



# Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo("Blanco", 4)
print(vehiculo)

# Segundo objeto de la clase auto
auto = Auto("Amarillo", 4, 120 )
print(auto)

# Tercer objeto, el de la clase  Bicicleta
bici = Bicicleta("Azul", 2, "Urbana")
print(bici)

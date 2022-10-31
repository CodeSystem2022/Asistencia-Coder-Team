
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

#-------------Alumno: Marcelo Lamas   -----------------
class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.wkargs = kwargs

    def mostrar_detalle(self): # self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.wkargs}')


persona1 = Persona('Ariel', 'Betancud', 32456987, 40)  # Necesitamos enviar argumentos
# print(persona1.nombre) # Tarea: Hacer el print igual que con el objeto 2
# print(persona1.apellido)
# print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')
persona2 = Persona('Osvaldo', 'Giordanini', 30321456, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona2.mostrar_detalle()

persona1.telefono = '44445555289'
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}') # Hemos creado un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error
persona3 = Persona('Rogelio', 'Romero', 35789456, 22, 'Teléfono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()

#-------------Alumno: Diego Alvarez-----------------

class Persona(): # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self): # Override = sobreescribir
        return f'Persona:[ Nombre: {self._nombre}, Edad: {self._edad}]'

class Empleado(Persona): # La clase empleado es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    
empleado1 = Empleado('Diego', 24, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
# Tarea: encapssular los atributos y agregar los metodos gatters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado('Fernando', 35, 85000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado3 = Empleado('Arnolito', 44, 90000)
print(empleado3.nombre)
print(empleado3.edad)
print(empleado3.sueldo)

#-------------Alumno: Natán Jabie-----------------

class Aritmetica:     
     """
     DocString: Operación aritmetica - Suma de dos valores
     """     
     def __init__(self, opA, opB):
          self.opA = opA
          self.opB = opB
          
     #Suma (método)
     def suma(self):
               return self.opA + self.opB

aritm = Aritmetica(15, 10)
print(aritm.sumar())
Po
r hildaortiz 

class Rectangulo : 
    """ 
    crear una clase llamado rectangulo, debe tener 2 atributos: 
    altura y base, el nombre del metodo sera calcular, area = 
    base * altura. pero la base y la altura deben ser ingresado por teclado 
    y los objetos deben ser tres 
    """ 
    def __init__(self, altura, base): 
        self.altura = altura 
        self.base = base 
    def area(self): 
        return self.altura * self.base 
print("calculamos el area de tres rectangulos") 
i = 1 
while i <= 3: 
      print(f"ingrese los datos para el {i} rectangulo ") 
      altura = int(input( "ingrese la altura ")) 
      base = int(input("ingrese la base ")) 
      are_rect = Rectangulo(altura, base) 
      print(f'el Area del {i} rectangulo es {are_rect.area()}') 
      i +=1 
print("terminamos") 
 
y la ejecución 

 

"C:\Program Files\Python310\python.exe" C:/Users/ANDRES/Tecnicaturagit/python/lession6/Rectangulo.py 

calculamos el area de tres rectangulos 

ingrese los datos para el 1 rectangulo  

ingrese la altura 5 

ingrese la base 7 

el Area del 1 rectangulo es 35 

ingrese los datos para el 2 rectangulo  

ingrese la altura 3 

ingrese la base 5 

el Area del 2 rectangulo es 15 

ingrese los datos para el 3 rectangulo  

ingrese la altura 7 

ingrese la base 9 

el Area del 3 rectangulo es 63 

terminamos 

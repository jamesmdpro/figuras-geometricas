from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# figura = FiguraGeometrica()


cuadrado1 = Cuadrado (5, 'rojo')
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
print('Creacion Objeto Cuadrado'.center(50, '-'))
print(f'Calculo del area Cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo( 10, 9 ,'verde')
print(f'Calculo del area Rectangulo : {rectangulo1.calcular_area()}')
print(rectangulo1)


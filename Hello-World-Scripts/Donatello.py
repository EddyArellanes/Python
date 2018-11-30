'''
Python Turtle Graphics
Is a Graphic Module used to learn relative coordinates
...Pending Description in English


Es un módulo de programación gráfica para Python utilizado como método para enseñar programación a través de coordenadas relativas

A la tortuga es un objeto al cual se le puede dar órdenes de movimiento (avance, retroceso, giro, etc). Moviendo adecuadamente la tortuga se puede conseguir dibujar todo tipo de figuras. La tortuga dispone de 3 atributos esenciales:

Posición: Respecto al centro de coordenadas.
Orientación: Dirección hacia donde mira la tortuga.
Pluma: Rastro que puede dejar la tortuga al desplazarse
Las funciones principales para animar nuestro objeto son las siguientes:

forward(distance): Avanzar una determinada cantidad de píxeles.
backward(distance): Retroceder una determinada cantidad de píxeles.
left(angle): Girar hacia la izquierda un determinado ángulo.
right(angle): Girar hacia la derecha un determinado ángulo.

'''

import turtle

window = turtle.Screen()
donatello = turtle.Turtle()

donatello.forward(100)
donatello.right(90)

donatello.forward(100)
donatello.right(90)

donatello.forward(100)
donatello.right(90)

donatello.forward(100)
donatello.right(90) 

window.mainloop()
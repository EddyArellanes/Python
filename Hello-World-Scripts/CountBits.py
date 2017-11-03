#Program that count the length of bits for a integer example: 2= 10 in Binary 10 length is 2, other example 3= 11 that lenght is 3.

def countBits(n):
    return n.bit_length()

import os
value= int(input("Escribe el número el cuál quieres saber su tamaño de Bits: "+'\n'))
bit= countBits(value)
print("El número "+str(value)+" tiene un tamaño de: "+'\n'+str(bit))


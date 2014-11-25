#!/usr/bin/python3

import os, sys
import numpy as np

##fonction de récupération d'index
def index_of(base, c):
    i = 0
    while base[i]:
        if base[i] == c:
            return i
        i += 1
    print("Phrase invalide")
    exit

##put_nbr_base
def putnbr_base(nbr, base):
    div = 1
    size_base = len(base)
    if nbr < 0:
        print("-")
        nbr *= -1
    while (div * size_base) <= nbr:
        div *= size_base
    while div >= 1:
        print(base[nbr/div])
        nbr = nbr % div
        div /= size_base
    return 0


''' debut de programme '''

##gestion nombre argument
if (len(sys.argv) != 8):
    print("Usage: ./102chiffrement {phrase} {key1} {key2} {key3} {key4} {base} {chiffrement: 0 ou dechiffrement: 1}")
    exit

##création de la clef
if (int(sys.argv[7]) == 0):
    key = np.matrix([[int(sys.argv[2]), int(sys.argv[4])],[int(sys.argv[3]), int(sys.argv[5])]])
    print("Chiffrement")
elif (int(sys.argv[7]) == 1):
    key = np.matrix([[int(sys.argv[5]), int(sys.argv[4]) * -1], [int(sys.argv[3]) * -1, int(sys.argv[2])]])
    print("Dechiffrement")
else:
    print("Chiffrement = 0 ou dechiffrement = 1")
    exit

##chiffrement
if (int(sys.argv[7]) == 0):
    print("j'entre dans le chiffrement")
    i = 0
    caract = sys.argv[1]
    while i < len(caract):
        caract[i] = index_of(str(" abcdefghijklmnopqrstuvwxyz"), caract[i])
        i += 1
    x_max = (len(caract) + 1) /2
    crypt = [2][x_max]
    x = 0
    while x < x_max:
        y = 0
        while y < 2:
            crypt[y][x] = 0
            y += 1
        x += 1
    print("je suis ici\n")
    x = 0
    i = 0
    while (x < x_max) and i < len(caract):
        y = 0
        while (y < 2) and i < len(caract):
            crypt[y][x] = caract[i]
            i += 1
            y += 1
        x += 1
    crypt *= key
    print("je suis la\n")
    putnbr_base(crypt, sys.argv[6])

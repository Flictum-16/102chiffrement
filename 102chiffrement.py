#!/usr/bin/python3

import os, sys
import numpy as np

##fonction de recuperation d'index
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
    if int(nbr) < 0:
        print("-", end="")
        nbr *= -1
    while (div * size_base) <= nbr:
        div *= size_base
    while div >= 1:
        print(base[int(nbr/div)], end="")
        nbr = nbr % div
        div /= size_base
    return 0

##convert_base
def 



''' debut de programme '''

##gestion nombre argument
if (len(sys.argv) != 8):
    print("Usage: ./102chiffrement {phrase} {key1} {key2} {key3} {key4} {base} {chiffrement: 0 ou dechiffrement: 1}")
    exit

##creation de la clef
if (int(sys.argv[7]) == 0):
    key = np.matrix([[int(sys.argv[2]), int(sys.argv[4])],[int(sys.argv[3]), int(sys.argv[5])]])
elif (int(sys.argv[7]) == 1):
    key = np.matrix([[int(sys.argv[5]), int(sys.argv[4]) * -1], [int(sys.argv[3]) * -1, int(sys.argv[2])]])
else:
    print("Chiffrement = 0 ou dechiffrement = 1")
    exit

##chiffrement
if (int(sys.argv[7]) == 0):
    caract = [index_of(" abcdefghijklmnopqrstuvwxyz", c) for c in sys.argv[1]]
    x_max = int((len(caract) + 1) /2)
    crypt = [[0 for x in range(x_max)] for x in range(2)]
    x = 0
    i = 0
    while (x < x_max) and i < len(caract):
        y = 0
        while (y < 2) and i < len(caract):
            crypt[y][x] = caract[i]
            i += 1
            y += 1
        x += 1
    crypt = key * np.matrix(crypt)
    crypt = crypt.tolist()
    print("chiffrement de \"" + sys.argv[1] + "\" à l'aide la clé " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5] + " dans la base \"" + sys.argv[6] +"\"\n=>", end="")
    x = 0
    while x < x_max:
        y = 0
        while y < 2:
            print(" ", end="")
            putnbr_base(int(crypt[y][x]), sys.argv[6])
            y += 1
        x += 1

##dechiffrement
if (int(sys.argv[7]) == 1):
    caract = sys.argv[1]
    caract = caract.split()
    for x in caract:
        x = convert_base("0123456789", x)
    print(caract)

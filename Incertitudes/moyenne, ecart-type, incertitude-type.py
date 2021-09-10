import math as m

def moyenne(L):
    somme = 0
    for elt in L:
        somme += elt
    return somme/len(L)

def ecart_type(L):
    somme = 0
    moy = moyenne(L)
    for i in range(len(L)):
        somme += (L[i] - moy)**2
    return m.sqrt((1/(len(L)-1))*somme)

def incertitude_type(L):
    return ecart_type(L)/m.sqrt(len(L))

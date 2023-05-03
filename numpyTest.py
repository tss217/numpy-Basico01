
import numpy as np

##cria uma lista com 10 itens 

x = np.arange(10)

print(x)
print("")

##cria array apatir de uma lista

array1 = np.array([100,2021,3894,8439])

print(f"array 1: {array1}")
print(type(array1))
print(array1.dtype)
print("")

## importando arquivos

km = np.loadtxt(fname="carros-km.txt", dtype= int)
print(km)
print("")

##oparações com arrays

km2  = np.array([32233,21212,2121,34343,2939])
anos = np.array([2003,2013,2000,2001,2004])

idade = 2022 - anos

print(idade)
print("")

##operações com array de duas dimenções 

dados = np.array([km2,anos])
    ### função para saber a dimenção do array 
print(dados.shape) 

print(dados)
kmMedia = dados[0] /(2022 - dados[1])
print(kmMedia)
print("2")
    ### seleciona coluna e linha do array
print(dados[1,2])
print("")

##fatiamento

contador = np.arange(100)
print(contador[1:20])
print(contador[0:100:10])
print(contador[::10])





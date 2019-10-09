from random import *
import sqlite3
import os
from bd import *

def inicio():
    op = opcao()
    if op == 1:
        sorteador()
    elif op == 2:
        adicionador()
    else:
        pass
    
def opcao():
    x = int(input("Digite sua escolha: \n 1 - Sortear 10 bichos \n 2 - Adicionar resultados \n 3 - Sair \n"))
    return x

def sorteador():
    lista = bd.getBichos()
    bichos = []
    for x in range(10):
        bichos.append(lista.pop(lista.index(max(lista))))
    print(bichos)    
    
    
    
    
    
def adicionador():
    os.system("cls")
    num = "x"
    while num != 's':
        num = input("Digite um numero, ou s para sair:\n")
        if num != 's':
            bd.addPeso(int(num),1)
            

    
                      
inicio()

            
    
    
       

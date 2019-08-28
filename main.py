from random import *
import sqlite3

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
    bichos = []
    for i in range(10):
        x = randint(1,20)
        bichos.append(x)
    print(bichos)
    
    
def adicionador():
    pass

    
                      
inicio()

            
    
    
       

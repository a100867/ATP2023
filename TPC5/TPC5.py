# Solução do exercício 3

import os
import random
import time
 
global condconsulta
condconsulta = False
global listp
listp = []



def listar():
    print("\nNumero de parques existentes: "+str(len(listp)))
    if listp == []:
        print("[]")
    else:
        print(*listp,sep='\n')
    input("Enter to continue...")
    menu()

def disponivel():
    cond = False
    while cond == False:
        os.system('cls')
        nome = input("Nome do parque que pretende procurar: ")
        for parque in listp:
                if parque[2] == nome:
                    xx = listp[parque]
                    cond = True
                else:
                    cond = False
    while cond == True:
        num_lugar = int(input("Numero do lugar do parque que pretende procurar : "))
        
    
    return

def estaciona():
    global condconsulta
    global list_lug_ocup
    condconsulta = True
    lugest = int(input("\nEm que lugar quer estacionar: "))
    try:
        for parque in listp:
            if parque[2] == nome_p:
                if lugest in parque[1]:
                    input("Lugar já está ocupado..")
                    consulta_parque()
                else:
                    input("Carro estacionado no lugar "+str(lugest))
                    parque[1].append(lugest)
                    consulta_parque()
    except ValueError:
        consulta_parque()


def liberta_lugar():
    global condconsulta
    global list_lug_ocup
    condconsulta = True
    luglib = int(input("\nQual lugar quer libertar: "))
    try:
        for parque in listp:
            if parque[2] == nome_p:
                if luglib in parque[1]:
                    input("Carro libertado no lugar "+str(luglib))
                    parque[1].remove(luglib)
                    consulta_parque()
                else:
                    input("Lugar já está livre..")
                    consulta_parque()
    except ValueError:
        consulta_parque()

def tamanho_parque():
    global condconsulta
    global listp
    global nome_p
    condconsulta = True
    size_num = int(input("\nNovo tamanho do parque: "))
    try:
        for parque in listp:
            if parque[2] == nome_p:
                parque[0] = size_num
                input("Tamanho do parque alterado")
                consulta_parque()
    except ValueError:
        consulta_parque()

def consulta_parque():
    global condconsulta
    global listp
    global list_lug_ocup
    global nome_p
    n = 0
    if listp == []:
        input("\nNão existem parques para consultar\nEnter to continue...")
        menu()
    os.system('cls')
    if condconsulta == True:
        #mostrar parque
        for parque in listp:
            if parque[2] == nome_p:
                condconsulta = True
                #val quadrado
                while parque[0] >= n*n:
                    n = n + 1
                n = n - 1
                #exec quadrado
                countlug = 1
                nv = n
                while nv > 0:
                    nh = n
                    while nh>0:
                        #ocupado = y/n
                        if countlug in parque[1]:
                            print("| "+str(countlug)+"(ocup) ", end="")
                        else:
                            print("|    "+str(countlug)+"    ", end="")
                        countlug = countlug + 1
                        nh = nh - 1
                    nv = nv - 1
                    print(" \n \n")
                while countlug <= parque[0]:
                    if countlug in parque[1]:
                        print("| "+str(countlug)+"(ocup) ", end="")
                    else:
                        print("|    "+str(countlug)+"    ", end="")
                    countlug = countlug + 1
                print("\nEste é o parque "+str(nome_p)+"\nTem "+str(parque[0])+" lugares")
                print("(1) Estacionar um carro\n(2) Libertar um lugar\n(3) Alterar tamanho do parque\n(0) Sair")
                x = input("Escolha uma opção: ").lower()
                if x == '1':
                    estaciona()
                elif x == '2':
                    liberta_lugar()
                elif x == '3':
                    tamanho_parque()
                elif x == '0':
                    condconsulta = False
                    menu()
                else:
                    consulta_parque()
    if condconsulta == False:
        nome_p = input("Nome do parque para consultar: ")
        for parque in listp:
            if parque[2] == nome_p:
                condconsulta = True
                consulta_parque()
        condconsulta = False
        consulta_parque()
        

def criaParque():
    cond = False
    global list_lug_ocup
    global listp
    while cond == False:
        os.system('cls')
        nome = input("Nome do parque: ")
        if listp == []:
            cond = True
        for parque in listp:
            if parque[2] == nome:
                cond = False
            else:
                cond = True
    cond = False
    while cond == False: 
        os.system('cls')
        num_lug_str = input("Numero total de lugares do parque: ")
        try:
            num_lug = int(num_lug_str)
            cond = True
            if num_lug == 0:
                cond = False
        except ValueError:
            os.system('cls')       
    cond = False
    list_lug_ocup = []
    while cond == False:
        os.system('cls')
        str = input("Insira um número dos lugares ocupados (p para parar): ")
        if str == 'p': 
            time.sleep(0.5)
            cond = True
            list_lug_ocup = list(set(list_lug_ocup))
            list_lug_ocup = sorted(list_lug_ocup)
            parque = [num_lug,list_lug_ocup,nome]
            listp.append(parque)
            input("Parque adicionado!\nEnter to continue...")
            menu()
        try:
            num = int(str)
            if num > num_lug:
                os.system('cls')
            else:
                list_lug_ocup.append(num)
        except ValueError:
            os.system('cls')

def removeParque():
    global listp
    if listp == []:
        input("\nNão existem parques para remover\nEnter to continue...")
        menu()
    os.system('cls')
    cond = False
    while cond == False:
        nome = input("Nome do parque para remover: ")
        for parque in listp:
            if parque[2] == nome:
                cond = True
                yn = input("Deseja eliminar o parque "+str(nome)+"? (y/n) ")
                if yn == "y":
                    listp.remove(parque)
                else:
                    menu()
            else:
                os.system('cls')

def menu():
    while True:
        os.system('cls')
        print("███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗")
        print("████╗░████║██╔════╝████╗░██║██║░░░██║")
        print("██╔████╔██║█████╗░░██╔██╗██║██║░░░██║")
        print("██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║")
        print("██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝")
        print("╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░\n")
        print("(1) Reset\n(2) Criar Parque\n(3) Remover Parque\n(4) Listar Parques\n(5) Consulta Parque\n(6) \n(7) \n(8) \n(9) \n(0) Sair")
        x = input("Escolha uma opção: ").lower()
        if x == '1':
           lista_random()
        elif x == '2':
            criaParque()
        elif x == '3':
            removeParque()
        elif x == '4':
            listar()
        elif x == '5':
            consulta_parque()
        elif x == '6':
            menor_lista()
        elif x == '7':
            ord_cres()
        elif x == '8':
            ord_decres()
        elif x == '9':
            find_elem()
        elif x == '0':
            os.system('cls')
            print("░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗")
            print("██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝")
            print("██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░")
            print("██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░")
            print("╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗")
            print("░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝")
            time.sleep(1)
            exit()
        elif x == 'p':
            os.system('cls')
            print("Lista atual:")
            print(lista_num)
            input("Enter to continue...")
        elif x == 'u':
            lista_num = lista_num_undo
        else:
            menu()
menu()
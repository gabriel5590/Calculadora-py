from funcoes import *
import time
from termcolor import colored
import pyfiglet 
import os 



while True:
    resultado = pyfiglet.figlet_format("Calculadora ")
    print(colored(resultado, 'cyan'))
    print(colored("1. Somar: ", 'green'))
    print(colored("2. Multiplicar: ", 'green'))
    print(colored("3. Dividir: ", 'green'))
    print(colored("4. Subtrair: ", 'green'))
    print(colored("5. Sair:", 'red'))
    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:
        while True:
            os.system('clear')
            painel_somar = pyfiglet.figlet_format("Somar")
            print(colored(painel_somar, 'cyan'))
            somar()
            break
    elif opcao == 2:
        while True:
            os.system('clear')
            painel_multiplicar = pyfiglet.figlet_format("Multiplicar")
            print(colored(painel_multiplicar, 'cyan'))
            multiplicar()
            break
    elif opcao == 3:
        while True:
            os.system('clear')
            painel_dividir = pyfiglet.figlet_format("Dividir")
            print(colored(painel_dividir, 'cyan'))
            dividir()
            break
    elif opcao == 4:
        while True:
            os.system('clear')
            painel_subtrair = pyfiglet.figlet_format("Somar")
            print(colored(painel_subtrair, 'cyan'))
            subtrair()
            break
    elif opcao == 5:
        os.system('clear')
        print_pause("Saindo...")
        break
    else:
        print(colored("Nenhuma opcao selecionada, Tente novamente", 'cyan'))

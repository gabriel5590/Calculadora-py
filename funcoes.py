
from funcoes import *
import time
from termcolor import colored
import pyfiglet 



def somar():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    resultado = nota1 + nota2 
    print("R:", resultado,)

def multiplicar():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    resultado = nota1 * nota2 
    print("R:", resultado,)

def dividir():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    resultado = nota1 / nota2 
    print("R:", resultado,)

def subtrair():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    resultado = nota1 - nota2 
    print("R:", resultado,)

def print_pause(text, pause=1):
    print(text)
    time.sleep(pause)



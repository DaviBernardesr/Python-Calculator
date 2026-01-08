#Calculadora em Python

from operacoes import operacoes
import math

#Inicializando.
num = 0

while (num == 0):

    num1 = 0
    num2 = 0

    print(f"Seja Bem-vindo a Calculadora em Python")
    print(f"--------------------------------------")
    print("Escolha a operação a ser realizada:")
    print("+")
    print("-")
    print("*")
    print("** (Potência)")
    print("/ (Divisão\n")

    print("x = Sair")

    operacao = input("Digite qual operação realizar:\n")

    if (operacao == "+"):
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite outro número:"))
        print(num1)
        print(num2)
    elif (operacao == "-"):
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite outro número:"))
        print(num1)
        print(num2)
    elif (operacao == "*"):
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite outro número:"))
        print(num1)
        print(num2)
    elif (operacao == "**"):
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite outro número:"))
        print(num1)
        print(num2)
    elif (operacao == "/"):
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite outro número"))
        print(num1)
        print(num2)
    elif (operacao == "x"):
        print("Saindo da Calculadora...\n")
        exit()
    else:
        print("Opção Inválida, Tente outra!!\n")

#Calculadora em Python

from operacoes import operacoes
import math

#Global
result = 0

from operacoes.operacoes import adicao
from operacoes.operacoes import subtracao
from operacoes.operacoes import multiply
from operacoes.operacoes import poten
from operacoes.operacoes import divis


#Inicializando.
num = 0

#1° Operação
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
    print("/ (Divisão)\n")

    print(f"Visor: {result}")

    print("x = Sair\n")

    operacao = input("Escolha sua operação:\n")

    if (operacao == "+"):
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite outro número:"))
        result = adicao(num1, num2)
        print(f"{result}")
    elif (operacao == "-"):
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite outro número:"))
        result = subtracao(num1, num2)
        print(f"{result}")
    elif (operacao == "*"):
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite outro número:"))
        result = multiply(num1, num2)
        print(f"{result}")
    elif (operacao == "**"):
        num1 = float(input("Digite a base:"))
        num2 = float(input("Digite a potência:"))
        result = poten(num1, num2)
        print(f"{result}")
    elif (operacao == "/"):
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite outro número"))
        result = divis(num1, num2)
        print(f"{result}")
    elif (operacao == "x"):
        print("Saindo da Calculadora...\n")
        exit()
    else:
        print("Opção Inválida, Tente outra!!\n")


    num = 1

    #2° Operação
    while ( num == 1):
        print("--------------------------------------")
        print("Escolha a operação a ser realizada: ")
        print("+")
        print("-")
        print("*")
        print("** (Potência)")
        print("/ (Divisão)\n")

        print(f"Visor: {result}")
        print("X = Sair\n")

        operacao = input("Escolha sua operação:\n")


        if(operacao == "+"):
            num3 = float(input("Digte um número:"))
            result = adicao(result, num3)
        elif(operacao == "-"):
            num3 = float(input("Digite um número:"))
            result = subtracao(result, num3)
        elif(operacao == "*"):
            num3 = float(input("Digite um número"))
            result = multiply(result, num3)

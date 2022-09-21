# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
import math
print("Olá, vou te ajudar a calcular seu salario")
try:
    salario_hora = float(input("Por favor, me informe qual o valor da sua hora de trabalho:"))
    try:
        horas_trabalhadas = int(input("E quantas horas você trabalhou este mês:"))
        salario = salario_hora * horas_trabalhadas
        print("Seu salario este mês sera de R${}".format(salario))
    except:
        print("O valor informado não é um numero inteiro!")
        print(horas_trabalhadas)
except:
    print("Você digitou um valor invalido")

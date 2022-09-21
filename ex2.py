#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]
try:
    numero = int(input("Digite um numero inteiro:"))
    print("O numero digitado foi:{}".format(numero))
except:
    print("O tipo de dado informado não e um numero inteiro")

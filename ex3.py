#Faça um Programa que peça dois números e imprima a soma.
try:
    primeiro_numero = int(input("Digite um numero inteiro:"))
    segundo_numero = int(input("Digite outro numero:"))
    print("A soma dos numeros digitados é:{}".format(primeiro_numero+segundo_numero))
except:
    print("O tipo de dado informado não e um numero inteiro")
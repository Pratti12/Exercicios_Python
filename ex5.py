#Faça um Programa que converta metros para centímetros.
print("Olá, irei converter metros em centimetros para você")
try:
    valor_metros = float(input("Por favor digite quantos metros você gostaria de converter:"))
    valor_centimetros = valor_metros * 100
    print("\nO valor de {} metros corresponde a {} centimetros".format(valor_metros,valor_centimetros))
except:
    print("O valor digitado não e um numero")
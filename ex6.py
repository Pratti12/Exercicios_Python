#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
print("Olá eu vou te ajudar a calcular a area de um círculo")
try:
    raio = float(input("Por favor digite o raio do círculo:"))
    area = 3.14159265359 * raio ** 2
    print("A area do circulo é {:.2f}".format(area))
except:
    print("O valor digitado não e um numero")
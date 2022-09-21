#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print("Olá estarei te ajudando a calcular a area de um quadrado.")
try:
    lado = float(input("Digite o lado do quadrado:"))
    area = lado ** 2
    print("A area do quadrado é: {}\nE o dobro da area é: {}".format(area,area*2))
except:
    print("O valor digitado não e um numero")
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print("olá, ajudarei a calcular sua media bimestral\n")
try:
    nota_1 = float(input("Digite sua primeira nota:"))
    nota_2 = float(input("Digite sua segunda nota:"))
    nota_3 = float(input("Digite sua terceira nota:"))
    nota_4 = float(input("Digite sua quarta nota:"))
    if(nota_1 < 0 or nota_1 > 10 or nota_2 < 0 or nota_2 > 10 or nota_3 < 0 or nota_3 > 10 or nota_4 < 0 or nota_4 > 10):
        print("O valor inserido em uma ou mais notas esta fora do escopo de 0 a 10")
    else:
        media = (nota_1 + nota_2 + nota_3 + nota_4)/4
        if(media >=6):
            if(media == 10):
                print("Parabens você e incrivel, sua media foi {}".format(media))
            else:
                print("Você foi aprovado com media {} parabens".format(media))
        else:
            print("Você esta reprovado pois sua media foi {} e não atingiu o media necessaria".format(media))
except:
    print("O valor digitado não e um numero")
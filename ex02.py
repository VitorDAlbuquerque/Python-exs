n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1+n2)/2

print("A média do aluno foi: " , media)

if(media >= 7 and media <= 9.99):
    print("Aprovado")
if (media < 7):
    print("Reprovado")
elif (media == 10):
    print("Aprovado com Distinção")

else:
    print ("Notas erradas")





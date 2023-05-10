altura = float(input("Digite a altura que você deseja soltar a bola: "))
i=0
total=altura
while (altura > 0.5):
    total += altura
    altura = altura * 0.6
    i +=1
print ("A bola quicou um total de", i, "vezes")
print ("A distâncial total percorrida foi de: " ,total,"m")

# Escreva um programa que leia o comprimento de três lados de um triângulo como
#entrada. A saída do programa deve indicar se o triângulo é ou não um triângulo
#retângulo. Lembre-se do teorema de Pitágoras que diz que em um triângulo
#retângulo, o quadrado de um lado é igual à soma dos quadrados dos outros dois
#lados.

l1 = int(input("Digite o comprimento do 1° lado"))
l2 = int(input("Digite o comprimento do 2° lado"))
l3 = int(input("Digite o comprimento do 3° lado"))

if (l1**2 == l2**2+l3**2):
    print("É um triângulo retângulo")
elif (l2**2 == l1**2+l3**2):
    print("É um triângulo retângulo")
elif (l3**2 == l2**2+l1**2):
    print("É um triângulo retângulo")
else:
    print("Não e um triângulo retângulo")
    

nota_a = int(input("Digite a nota 1: "))
nota_b = int(input("Digite a nota 2: "))
nota_c = int(input("Digite a nota 3: "))
media = (nota_a+nota_b+nota_c)/3

if media <5:
    print("Reprovado")
elif 5<= media <7:
    print("Em recuperação")
elif media >=7:
    print("Aprovado")

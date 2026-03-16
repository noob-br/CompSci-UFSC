print("Calculadora de IMC")

peso = int(input("Digite quantos kgs você tem: "))
altura = int(input("Digite qual sua altura em cm: "))
altura_conta = altura/100
imc = peso/(altura_conta**2)

if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <= imc < 25:
    print("peso ideal")
elif 25 <= imc < 30:
    print("sobrepeso")
elif 30 <= imc <= 40:
    print("obesidade")
elif imc > 40:
    print("obesidade mórbida")


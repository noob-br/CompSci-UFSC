valor_total = float(input("Vamos fazer seu empréstimo\nInforme o valor da casa: "))
salario = float(input("Informe o salário do comprador: "))
anos = int(input("Informe em quantos anos o comprador irá pagar: "))

meses = anos*12
limite_salario = salario*0.3
valor_mensal = valor_total/meses

print("Analisando a proposta...")


# logica da aprovacao
if valor_mensal <= limite_salario:
    print("Empréstimo CONCEDIDO! Aproveite sua casa nova.")
else:
    print("Empréstimo NEGADO. A parcela excede 30% do seu salário.")


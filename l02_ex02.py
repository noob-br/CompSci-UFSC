valor_produto = float(input("Informe o valor do produto: "))

while True:
    try:
        opcao = int(input(("Digite 1 para pagar à vista (dinheiro/cheque) e 2 para opções de cartão: ")))
       
        if 1 <= opcao <= 2:
            break #para o loop
        else: 
            print("Valor inválido. Por favor, digite um número entre 1 e 2.")
    except ValueError:
        print("Inválido, não invente moda, apenas inteiros.")
    
print(f"Você escolheu a opção {opcao}. Carregando opções...")

if opcao == 1:
    a = valor_produto*0.9
    print(f"Você ganhou 10% de desconto, o valor é de R${a:.2f}")

elif opcao == 2:
    try:
        parcela = int(input("Digite em quantas vezes deseja parcelar: "))
        
        if parcela == 1:
               # b. 1x no cartão – 5% de d100esconto
             b = valor_produto*0.95
             print(f"Você ganhou 5% de desconto, 1x de R${b:.2f}")

        elif parcela == 2:
            #c. 2x cartão – preço normal
            c = valor_produto/2
            print(f"Parabéns, você ganhou parcelamento sem juros. 2x de R${c:.2f}")

        elif parcela >= 3:
            #d. 3x ou mais no cartão - 20% de juros 
             d = (valor_produto*1.2)/parcela
             print(f"Com o parcelamento você pagará {parcela:.2f}x de R${d:.2f}")

        else:
            print("Erro, o número de parcelas precisa ser maior que zero.")
    except ValueError:
        print("Erro: Digite apenas números inteiros")

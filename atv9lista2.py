#Atividade 9
valor = float(input("Digite o valor do prodruto:R$"))

if valor > 100:
    desconto = valor* 0.10
    valor_final = valor - desconto
    print(f"Voce recebeu um desconto de R$ {desconto:.2f}. valor final: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. valor final: R$ {valor:.2f}")    
    
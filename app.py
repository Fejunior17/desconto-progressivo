# Entrada de dados
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verificação da faixa de desconto
if valor_compra < 200:
    percentual_desconto = 5
elif valor_compra < 300:
    percentual_desconto = 10
else:
    percentual_desconto = 15

# Cálculo do desconto
valor_desconto = valor_compra * (percentual_desconto / 100)

# Cálculo do valor final da compra
valor_final = valor_compra - valor_desconto

# Exibição dos resultados
print("\n--- Resultado da compra ---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
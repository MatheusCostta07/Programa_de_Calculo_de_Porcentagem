def calcular_desconto(preco, porcentagem_desconto):
  return preco - (preco * porcentagem_desconto / 100)

preco = float(input('Digite o valor do produto: '))
porcentagem_desconto = float(input('Digite a porcentagem que gostaria de aplicar ao produto: '))

valor_final = calcular_desconto(preco, porcentagem_desconto)
print(f'O preço inicial do produto era de R${preco:.2f},a porcentagem solicitada foi de {porcentagem_desconto}% e O valor final com o desconto é de R${valor_final:.2f}.')

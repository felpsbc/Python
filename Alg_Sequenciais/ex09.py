#Faça um algoritmo que leia o preço de um produto e mostre o seu valor com desconto de 10%.

product_value = float(input("Digite o valor do Produto: "))

desconto = 0.1

product_desc = product_value - desconto*product_value

print(f"O valor do produto com desconto e {product_desc}")

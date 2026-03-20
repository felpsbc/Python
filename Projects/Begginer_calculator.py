num1 = float(input("Digite um número: "))
num2 = float(input("Digite o Segundo número: "))

operador = input("Digite + (adição) - (subtração) * (multiplicação) e / (divisão) para realizar sua operação: ")

if operador == "+":
    print(f"O valor da sua Soma é: {num1 + num2}")
elif operador == "-": 
    print(f"O valor da sua Subtração é: {num1 - num2}")
elif operador == "*": 
    print(f"O valor da sua Multiplicação é: {num1 * num2}")
elif operador == "/":
    print(f"O valor da sua Divisão é: {num1 / num2}")
else:
    print("Coloque um Operador Válido")


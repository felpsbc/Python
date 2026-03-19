#Faça um algoritmo que imprima os números de 1 a 100, substituindo os múltiplos de 3 pela palavra "Fizz" 
# e os múltiplos de 5 pela palavra "Buzz". 
# Para os números que são múltiplos de ambos, utilize a palavra "FizzBuzz".

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0: # A Ordem do If importa, pois caso coloque ele por ultimo ele imprimira a primeira condição que for verdadeira
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
#Faça um algoritmo que leia um número inteiro entre 1 e 7 e 
# mostre o dia da semana correspondente (1 = domingo, 2 = segunda-feira, etc.).

num = int(input("Digite um numero entre 1 e 7: "))

match num:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terca")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabado")
    case _:
        print("Escolha um numero de 1 a 7, por favor")
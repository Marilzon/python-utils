
def table_calc():
    import os
    os.system("clear")
    print("\n******************* Python Calculator *******************")
    print("Selecione a  operacao desejada\n")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    operation = int(input())

    if (operation == 1):
        number_one = int(input("Digite o primeiro valor: "))
        number_two = int(input("Digite o segundo valor: "))
        print("Resultado: ", number_one + number_two)
    elif (operation == 2):
        number_one = int(input("Digite o primeiro valor: "))
        number_two = int(input("Digite o segundo valor: "))
        print("Resultado: ", number_one - number_two)
    elif (operation == 3):
        number_one = int(input("Digite o primeiro valor: "))
        number_two = int(input("Digite o segundo valor: "))
        print("Resultado: ", number_one * number_two)
    elif (operation == 4):
        number_one = int(input("Digite o primeiro valor: "))
        number_two = int(input("Digite o segundo valor: "))
        if (number_two < 1):
                print("Nao e possivel dividir por numeros menores que 1")
        else:
                print("Resultado: ", number_one / number_two)
    else:
        print("Operacao invalida")
        table_calc()
    return

table_calc()

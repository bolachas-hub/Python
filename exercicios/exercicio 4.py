numero = int(input("Digite um número: "))

match numero:
    case i if i < 0:
        print("Categoria: negativo")

    case 0:
        print("Categoria: zero")

    case i if i > 0:
        if i % 3 == 0 and i % 5 == 0:
            print("Categoria: divisível por 3 e 5")
        elif i % 2 == 0:
            print("Categoria: positivo e par")
        elif i % 2 != 0:
            print("Categoria: positivo e ímpar")
        else:
            print("Categoria: outros números positivos")

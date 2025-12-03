import os 
os.system('cls')

j1=""
j2=""
var2 = True



while var2:
    j1=int(input("escolha entre pedra(1) papel(2) ou tesoura(3): "))
    os.system('cls')
    j2=int(input("escolha entre pedra(1) papel(2) ou tesoura(3): "))
    os.system('cls')
 
    match j1:
        case 1:
            match j2:
                case 1:
                    print("empate, os dois escolheram pedra")
                case 2:
                    print("o jogador 2 ganhou")
                case 3:
                  print("o jogador 1 ganhou")
                case _:
                  print("Escolha errada")
        case 2:
            match j2:
                case 1:
                    print("o jogador 1 ganhou")
                case 2:
                    print("empate, os dois escolheram papel")
                case 3:
                    print("o jogador 2 ganhou")
                case _:
                    print("Escolha errada")
        case 3:
            match j2:
                case 1:
                    print("o jogador 2 ganhou")
                case 2:
                    print("o jogador 1 ganhou")
                case 3:
                    print("empate, os dois escolheram tesoura")
                case _:
                    print("Escolha errada")
        case _:
            print("Escolha errada")
    var1 = int(input("deseja voltar a jogar ? 1- sim 2- nao "))
    match var1:
        case 2:
            print("adeus")
            var2 = False
        case 1:
            print("a recomeçar")    
        case _:
            print("resposta errada")
opc=0
saida= True

print("1- para receber um bom dia")
print("2- para receber um boa tarde")
print("3- para receber um boa noite")
print("4- para sair")




while saida:
    opc=int(input("intrud a opção: "))
    match opc:
        case 1:
            print("Bom dia")
        case 2:
            print("boa tarde")
        case 3: 
            print("boa noite")
        case 4:
            saida = False
            print("adeus")
            break
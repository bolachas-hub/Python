# Lista original de strings com números inteiros
lista_str = [str(i) for i in range(1, 42, 4)]  # ["1", "5", "9", ..., "41"]

# Converter cada string para inteiro com list comprehension
lista_int = [int(x) for x in lista_str]

print(lista_str)
print(lista_int)



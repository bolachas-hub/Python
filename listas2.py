# Lista original com 15 strings (algumas numéricas, outras não)
lista_mista = ["10", "abc", "25", "42", "hello", "7", "world", "99", "33", "foo", "bar", "123", "0", "9x", "88"]

# Criar uma nova lista apenas com as strings numéricas, convertidas para int
lista_numerica = [int(x) for x in lista_mista if x.isdigit()]

print(lista_mista)
print(lista_numerica)

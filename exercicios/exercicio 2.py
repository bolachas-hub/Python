num1=0
num2=0
num3=0


num1 =int( input("intrude 1 numero"))
num2 =int( input("intrude 2 numero"))
num3 =int( input("intrude 3 numero"))


if num1 > num2 > num3:  

    print(f"maior: {num1} \nmenor: {num3}")

elif num1 > num3 >num2 :

    print(f"maior: {num1} \nmenor: {num2}")

elif num2 > num3 > num1 :

    print(f"maior: {num2} \nmenor: {num1}")

elif num2 > num2 > num3 :

    print(f"maior: {num2} \nmenor: {num3}")

elif num3 > num1 > num2 :

    print(f"maior: {num3} \nmenor: {num2}")

elif num3 > num2 > num1 :

    print(f"maior: {num3} \nmenor: {num1}")
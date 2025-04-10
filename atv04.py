num=int(input("Digite um número: "))
if num <= 0:
    print("Número invalido")
else:
    for i in range(1, num+1, 1):
        print(i, end=" ")


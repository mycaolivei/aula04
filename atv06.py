dentro=0
fora=0
for i in range(10):
    num= int(input("Digite um número: "))
    if num<10 or num>20:
        fora=fora + 1
    else:
        dentro = 5 - fora
print(f"Encontrei {dentro} números no intervalo e {fora} números fora do intervalo")
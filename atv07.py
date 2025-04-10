soma=0
qntd=int(input("Digite a quantidade de números que voce quer a media: "))
for i in range(qntd):
    num=int(input("Digite o número: "))
    soma=(soma+num)
media=soma/qntd
print(media)


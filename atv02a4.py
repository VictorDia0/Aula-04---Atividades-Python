#Faça um programa que receba duas notas (0 a 10), calcule e mostre a média aritmética e a mensagem que está na tabela a seguir
# Media Mensagem
#0,00 - 4,00 Reprovado
#4,00 - 7,00 Recupeeração
#7,00 - 10,00 Aprovado

print('Abaixo digite as notas dos alunos!!')
nome = str(input('Digite seu nome: '))
n01 = float(input('Digite a nota da primeira prova: '))
n02 = float(input('Digite a nota da segunda prova: '))

md = (n01 + n02) / 2

if md >= 7 :
    print(f'Parabêns {nome}, você foi aprovado!')
elif md >= 4 and md < 7 :
    print(f'{nome}, você está de recuperação')
else :
    print(f'{nome}, você foi reprovado')
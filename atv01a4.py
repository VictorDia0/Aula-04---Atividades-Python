#Faça um programa que receba quatro notas de um aluno, calcule e mostre a média aritmética das notas e a mensagem de aprovado ou reprovado, considerando para aprovação a média 7.

print('Abaixo descreva as notas do aluno!')
nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a nota da prova 1: '))
nota2 = float(input('Digite a nota da prova 2: '))
nota3 = float(input('Digite o valor da prova 3: '))
nota4 = float(input('Digite o valor da prova 04: '))
md = (nota1 + nota2 + nota3 + nota4) / 4

if md >= 7 :
    print(f'Parabéns {nome}, você foi aprovado com {md} de média!')
else :
    print(f'Infelizmente {nome}, você foi reprovado com {md} de media!')
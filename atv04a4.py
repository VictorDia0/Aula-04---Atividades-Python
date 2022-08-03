#Uma empresa decide dar um aumento de 30% aos funcionários com salários inferiores a R$ 500,00. Faça um programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem, caso o funcionário não tenha direito ao aumento.

print('Abaixo descreva os salrios dos funcionarios.')
sal = float(input('Digite o salario: '))

if sal < 500.00 :
    res = sal * 1.30 
    print (f'O salario do funcionario será reajustado para {res} reais.')
else :
    print(f'O salario do funcionario não será reajustado')
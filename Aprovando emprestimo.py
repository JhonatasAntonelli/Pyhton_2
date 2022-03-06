print('-*-'*5, 'Bom dia!', '-*-'*5)
valor = float(input('Qual o valor da casa que você quer financiar?'))
salario = float(input('Qual é o seu salário?'))
tempo = float(input('Para quantos anos você que fincanciar?'))
parcela = valor/(tempo*12)
if parcela > (salario * 0.3):
    print('Infelizamente não podemos financiar a sua casa')
else:
    print('Seu imprestimo foi aprovado, parabéns!')
print('-*-'*5, 'Bom dia!', '-*-'*5)
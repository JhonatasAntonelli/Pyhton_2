s = 0
for c in range (0,6):
    x = int(input('Digite um valor a ser saomado'))
    y = x%2
    if y == 0:
        s += x
print ('A soma de todos os pares é {}'.format(s))
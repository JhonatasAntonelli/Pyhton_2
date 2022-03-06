x = int(input('Digite um número'))
n = x - 1
for c in range (0, x-2):
    y = x % n
    if y == 0:
        print ('Não é primo')
        break
    n = n -1
if n == 1 and y!=0:
    print ('É primo')

n = int(input('Digite o número que você queira iniciar asequência Fibonacci: '))
x = 3
f1 = f2 = 1
sequencia = f1 + f2
print (1)
print (1)
print (sequencia)
while x < n:
    sequencia1 = sequencia + f2
    x = x + 1
    print (sequencia1)
    if x < n:
        sequencia2 = sequencia1 + sequencia
        x = x + 1
        print(sequencia2)
    f2 = sequencia1
    sequencia = sequencia2



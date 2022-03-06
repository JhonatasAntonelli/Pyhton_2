for c in range (0,6):
    print('oi')
for c in range (0,6):
    print(c)
for c in range (6,0,-1):
    print(c)
for c in range (0,20,2):
    print(c)
n = int(input('Digite um número'))
for c in range (0,n+1):
    print(c)
i = int(input('Digite um número inicial'))
f = int(input('Digite um número final'))
p = int(input('Digite a frequência'))
for c in range (i, f+1, p):
    print(c)
s = 0
for c in range (0,4):
    n = int(input('digite um número para ser somado'))
    s += n
print (s)
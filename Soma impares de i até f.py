i = int(input('Digite o inicio da contagem'))
f = int(input('Digite o fim da contagem'))
x = i%2
s = 0
if x == 0:
    i = i+1
for c in range (i,f,2):
    if c % 3 == 0:
        s += c
print ('O valor da soma é {}'.format(s))
n = int(input('Digite o tempo inicial da progressão'))
r = int(input('Digite a razão da progressão'))
y = 0
#for c in range (n, n+(10*r), r):
    #print(c)
for c in range (0,10):
    x = n + (r * y)
    y = y+1
    print (x)
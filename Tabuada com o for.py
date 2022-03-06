x = int(input('Digite um número que você queira saber a tabuada'))
z = 1
for c in range (0, x):
    y = x * z
    print( z, "X", x, "=", y)
    z = z + 1
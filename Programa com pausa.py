import time

n = int(input('Digite um número para contagem regresiva'))
for c in range (n, 0, -1):
    print(c)
    time.sleep(1)
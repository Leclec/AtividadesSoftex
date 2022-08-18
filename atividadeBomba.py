# contador regressivo de uma bomba

from time import sleep

print("Iniciando contagem regressiva\n")
for cont in range (10, -1, -1):
    print(cont)
    sleep(1)
    print("\n")
print("BUUMMM!!")
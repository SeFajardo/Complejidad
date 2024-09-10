from time import time
from memory_profiler import profile
@profile
def prueba():
    sum = 0
    b = int(input("Ingrese la base: "))
    e = int(input("Ingrese el exponente: "))
    n = b**e
    start_time = time()
    while (n>0):
        n = n//2
        i = 0
        while (i<n):
            sum = sum + 1
            i = i +1
    print(sum)
    elapsed_time = time() - start_time
    print("Tiempo trascurrido: %.20f seconds." % elapsed_time)
prueba()
from time import time
from memory_profiler import profile
@profile
def prueba():
    sum = 0
    b = int(input("Ingrese la base: "))
    e = int(input("Ingrese el exponente: "))
    n = b**e
    i = 1
    start_time = time()
    while (i < n):
        i = i*2
        j = 0
        while (j < n):
            sum = sum + 1
            j = j +1
    print(sum)
    elapsed_time = time() - start_time
    print("Tiempo trascurrido: %.20f seconds." % elapsed_time)
prueba()
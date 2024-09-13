def two_sum(lst, target):
    lista=lst["elements"]
    encontrado=False
    for numero in lista:
        for otros_elem in lista[numero:lst["size"]]:
            if otros_elem+numero==target:
                encontrado=True
                return encontrado
    return encontrado
        
two_sum({"elements":[1,4,8,10,6],"size":5},9)
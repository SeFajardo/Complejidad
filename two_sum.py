def remove_element(my_set, element):
    if element in my_set:
        my_set.remove(element)
    return my_set

def two_sum(lst, target):
    for numero in lst:
        lst2=lst
        lst2=remove_element(lst,numero)
        for otros_elem in lst2:
            if otros_elem+numero==target:
                return True
    return False
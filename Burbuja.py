def ord_insercion(lista):
    for i in range(len(lista)-1):
        if lista[i+1]< lista[i]:
            reubicar(lista, i+1)
 
        print ("DEBUG: ", lista)
 
def reubicar(lista, p):
    v = lista[p]
    j = p
    while j > 0 and v < lista[j-1]:
        lista[j] = lista[j-1]
        j -= 1
    lista[j] = v
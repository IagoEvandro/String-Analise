def encontrar_numero(arr):

    pares = [encontrar_numero % 2 == 0 for encontrar_numero in arr[:3]]
    maioria_pares = pares.count(True) >= 2

    for encontrar_numero in arr:
        if (encontrar_numero % 2 ==0) != maioria_pares:
            return encontrar_numero

print(encontrar_numero([ 2, 4, 6, 7, 10, 78]))
print(encontrar_numero([ 1, 3, 5, 8, 9, 47]))
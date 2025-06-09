impre = input("Digite uma String ")
numero_letras = len(impre)
erros = 0

for letras in impre:
    if letras < 'a' or letras > 'm':
        erros += 1 

printer_error = (erros / 20)
print(printer_error)

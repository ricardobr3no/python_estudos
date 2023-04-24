print("[Q] to exit")
while 1:
    idade_cliente = input("Informe a idade do cliente: ")
    if idade_cliente.upper == 'Q':
        break
    else:
        idade_cliente = int(idade_cliente)
        if idade_cliente <= 3: print("GRATUITO")
        elif idade_cliente <= 12: print("$10,00")
        else: print ("$15,00")
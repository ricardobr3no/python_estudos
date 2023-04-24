sanduba_comanda = ['pastrami', 'tradicional', 'pastrami', 'duplo', 'tropical', 'big-mac', 'pastrami']
sanduba_feito = []

print(sanduba_comanda)
print("Nao tem pastrami\n\tAtualizando...")
while 'pastrami' in sanduba_comanda: sanduba_comanda.remove('pastrami')

while 1:
    i = 1
    for sanduba in sanduba_comanda:
        print(f"{i} -> {sanduba}")
        i+=1

    opcao = int(input("Qual sanduba escolhe preparar? [0 p/ SAIR]\n"))
    if opcao != 0:
        sanduba_atual = sanduba_comanda.pop(opcao-1)
        print("preparando " + str(sanduba_atual) + "...")
        sanduba_feito.append(sanduba_atual)
    else:
        break

print("os sandubas preparados foram:", sanduba_feito)
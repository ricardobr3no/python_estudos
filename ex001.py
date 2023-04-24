ingredientes = []

print("\n'quit' to exit")
while True:
    ingrediente = input("Que ingrediente voce deseja colocar? ")
    if ingrediente == "quit":
        break
    ingredientes.append(ingrediente)
    print(f"{ingrediente} adicionado!")

print("ingredientes adicionados:", ingredientes)
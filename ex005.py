# Álbum: Escreva uma função chamada make_album() que construa um dicionário descrevendo um álbum musical. A função deve aceitar o nome de um artista e o título de um álbum e deve devolver um dicionário contendo essas duas informações. Use a função para criar três dicionários que representem álbuns diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão armazenando as informações do álbum corretamente. Acrescente um parâmetro opcional em make_album() que permita armazenar o número de faixas em um álbum. Se a linha que fizer a chamada incluir um valor para o número de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo menos uma nova chamada da função incluindo o número de faixas em um álbum.

n_albums = 0
albuns_total = []

def make_album(artist_name: str, titulo: str, faixas: int = ''):
    album = {}
    album['Nome'] = artist_name.title()
    album['Titulo'] = titulo.title()
    album['N° faixas'] = faixas
    return album
    

while True:
    nome = input("Informe o nome do artista: ")
    titulo = input("informe o nome do album: ")
    opcao_faixa = input("inserir numero de faixas? [S/N]\n")
    
    if opcao_faixa.lower() == 's':
        faixas = int(input("Informe o numero de faixas: "))  
        print("voce criou o album " + str(make_album(nome, titulo)))
        albuns_total.append(make_album(nome, titulo))   
    
    elif opcao_faixa.lower() == 'n':
        print("voce criou o album " + str(make_album(nome, titulo)))
        albuns_total.append(make_album(nome, titulo))   

    print("voce criou o album " + str(make_album(nome, titulo, faixas)))  

    n_albums += 1
    opcao = input("Deseja adicionar outro album? [S/N]\n")
    
    if opcao.lower() == 's': print("reinicinado...")
    
    elif opcao.lower() == 'n':   
        print(f"Voce criou {n_albums} albums, sendo eles: {albuns_total}\nFim do programa")
        break

    else: print("opcao invalida, tente novamente")


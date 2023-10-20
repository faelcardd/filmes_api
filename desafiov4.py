import requests
import json





#função de busca pela API
def buscar_filme_por_titulo(titulo, api_key):
    base_url = f'http://www.omdbapi.com/?apikey=b0ee5ebb'
    params = {
        't': titulo
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data.get('Response') == 'True':
            return data  #retorna o filme encontrado
        else:
            print("Nenhum filme encontrado com o título fornecido.")
            return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None
    




#função para adicionar filme aos favoritos
def adicionar_filme_a_favoritos(filme, favoritos_file):
    with open(favoritos_file + '.json', 'a') as file:
        json.dump(filme, file)
        file.write('\n')
    print("Filme adicionado aos favoritos!")





#função para listar os filmes favoritos
def listar_filmes_favoritos(favoritos_file):
    try:
        with open(favoritos_file + '.json', 'r') as file:
            for line in file:
                filme = json.loads(line)
                print("Título do filme:", filme['Title'])
                print("Ano de lançamento:", filme['Year'])
                print("Classificação:", filme['Rated'])
                print("Sinopse:", filme['Plot'])
                print("Diretor:", filme['Director'])
                print()
    except FileNotFoundError:
        print("Nenhum filme favorito encontrado.")





#função menu opções
def menu():
    api_key = 'b0ee5ebb'
    favoritos_file = 'favoritos_file'
    
    while True:
        print("Escolha uma opção:")
        print("1. Pesquisar um filme por título")
        print("2. Adicionar filme aos favoritos")
        print("3. Listar filmes favoritos")
        print("4. Sair")
        
        escolha = input("Digite o número da opção desejada: ")


        #chama a primeira função
        if escolha == '1':
            titulo = input("Digite o título do filme que você deseja buscar: ")
            filme = buscar_filme_por_titulo(titulo, api_key)
            if filme:
                print("Título do filme:", filme['Title'])
                print("Ano de lançamento:", filme['Year'])
                print("Classificação:", filme['Rated'])
                print("Sinopse:", filme['Plot'])
                print("Diretor:", filme['Director'])


        #chama a segunda função        
        elif escolha == '2':
            titulo = input("Digite o título do filme que você deseja adicionar aos favoritos: ")
            print("******************************************************************")
            filme = buscar_filme_por_titulo(titulo, api_key)
            if filme:
                adicionar_filme_a_favoritos(filme, favoritos_file)


        #chama a terceira função        
        elif escolha == '3':
            listar_filmes_favoritos(favoritos_file)
        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

#retorna menu
if __name__ == "__main__":
    menu()
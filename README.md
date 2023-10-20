# Meus Filmes Favoritos

## Descrição

O projeto "Meus Filmes Favoritos" é um script Python que permite aos usuários pesquisar informações detalhadas sobre filmes e manter uma lista de seus filmes favoritos. Ele utiliza a API OMDB para obter informações sobre filmes com base em seus títulos.

## Funcionalidades

- Pesquisar informações sobre filmes por título.
- Adicionar filmes à lista de favoritos.
- Listar filmes favoritos.

## Como Usar

1. Clone este repositório em seu ambiente local.
2. Execute o script `filmes_api.py`.
3. Siga as opções do menu para pesquisar filmes, adicionar filmes aos favoritos ou listar filmes favoritos.

## Pré-requisitos

- Python 3
- Import requests

## Uso de funções

- Foram construídas 4 funções com diferentes funcionalidades para que o script pudesse atender todos os pré-requisitos.
```python
def buscar_filme_por_titulo(titulo, api_key):
def adicionar_filme_a_favoritos(filme, favoritos_file):
def listar_filmes_favoritos(favoritos_file):
def menu():
```

Para instalar as dependências necessárias, execute o seguinte comando:

```bash
pip install requests



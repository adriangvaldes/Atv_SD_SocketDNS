"""
Author: Adrian Garcia Valdes

Quote // "Como vimos em aula, este é um serviço WEB, que recebe requisições HTTP e envia as
respostas caso a rota seja reconhecida, se a rota não for reconhecida o o framework
Flask retorna o erro 404 NOT FOUND automaticamente.
Para rodar o programa digite...
$ python3 app.py
experimente então no Browser as rotas definidas, se a rota tiver <algum_nome>,
a função vinculada a rota deve ter como parâmetro uma variável com o o mesmo nome,
(veja a rota de comentários) e você terá acesso ao valor que foi passado nesta variável.
Tente criar novas rotas com elementos referentes a um sistema de blogs, como curtidas em
posts e comentários, grupos, etc.
Caso tenham dúvidas usem o nosso grupo do Discord ou enviem um e-mail para
msbrito@uesc.br." By: José Mathias //

"""
import json
import time

from flask import Flask

app = Flask(__name__)

def loadClients():
    dataClients = [{
        "name": "Felisbelo Silva",
        "id": 1,
        "email": "felisbelo@email.com"
        },
        {
        "name": "Maria Joaquina",
        "id": 2,
        "email": "mjoaquina@email.com"
        },
        {
        "name": "Robert Joseph",
        "id": 3,
        "email": "robertj@email.com"
        },
        {
        "name": "Tobias Malaquias",
        "id": 4,
        "email": "tobmalaq@email.com"
        },
    ]   
    return dataClients

def loadProducts():
    dataProducts = [{
        "id": 1,
        "name": "Intel i7 9500",
        "category" : "Processador",
        "price": "R$ 2200,90"
        },
        {
        "id": 2,
        "name": "RTX 3080 ti",
        "category" : "Placa de vídeo",
        "price": "R$ 3500,00"
        },
        {
        "id": 3,
        "name": "Intel i5 9770",
        "category" : "Processador",
        "price": "R$ 1500,90"
        },
        {
        "id": 4,
        "name": "RTX 2060",
        "category" : "Placa de vídeo",
        "price": "R$ 1600,90"
        },
        {
        "id": 5,
        "name": "Intel i3 8750",
        "category" : "Processador",
        "price": "R$ 999,90"
        },
        {
        "id": 6,
        "name": "RTX 1650 Super",
        "category" : "Placa de vídeo",
        "price": "R$ 1100,90"
        }
    ]
    return dataProducts

def loadStock():
    dataStock = [{
        "id": 1,
        "amount": "136"
        },
        {
        "id": 2,
        "amount": "340"
        },
        {
        "id": 3,
        "amount": "245"
        },
        {
        "id": 4,
        "amount": "110"
        },
        {
        "id": 5,
        "amount": "30"
        },
        {
        "id": 6,
        "amount": "32"
        }
    ]
    return dataStock

@app.route('/')
def index():
    return "GV Store"

@app.route('/clients')
def clients():
    clients = loadClients()
    time.sleep(1)  # Insere uma demora artificial com sleep na requisição para simular

    return json.dumps(clients)


@app.route('/products')
def products():
    products = loadProducts()
    time.sleep(1)  # Insere uma demora artificial com sleep na requisição para simular
                   # demora no processamento
    return json.dumps(products)


@app.route('/products/<id>')
def productById(id):
    productId = int(id)
    products = loadProducts()

    try:
        for product in products:
            if product['id'] == productId:
                productById = product
                return json.dumps(productById)
    except:
        return 'Erro ao buscar produto!'


@app.route('/products/<id>/stock')
def stockOfProduc(id):
    stock = loadStock()
    products = loadProducts()

    try:
        for productStock in stock:
            if productStock['id'] == int(id):
                productStockById = productStock
                amount = productStockById['amount']
                
                for product in products:
                    if product['id'] == int(id):
                        name = product['name']

                return f'Quantidade do produto {name} : {amount}'
    except:
        return 'Erro ao buscar o estoque do produto!'


if __name__ == '__main__':
    app.run()
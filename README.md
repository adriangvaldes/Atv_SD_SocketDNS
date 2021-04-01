# Python Flask - Atividade

## Resumo

O que eu fiz foi uma simulação de um backend de uma loja de hardware, colocando os dados manualmente sobre os produtos e clientes (Sem nenhum tipo de uso de outras ferramentas), apenas para estudar sobre o Flask.

## Descrição do programa

As primeiras funções do programa: `loadClients()`, `loadProducts()` e `loadStock`, são as funções que simulam o carregamento das informações do banco de dados, apenas retornando o objeto no formato JSON (lista de dicionários no python).

A primeira rota é a home, que nada tem implementado, apenas o nove da loja. 

Depois temos a rota de `/clients` onde listamos todos os clientes cadastrados na loja, apenas guardando o retorno da função `loadClients` dentro de uma variável `clients` e dps retornando via método `json.dumps(clients)` , para transformar esse objeto python em um objeto JSON de fato.

Em seguida temos a rota `/products` que segue a exata mesma logica da rota acima, porem dessa vez com a função `loadProducts`.

> Coloquei um time.sleep(1) para simular a demora da busca das informações em um banco de dados.

Na rota `/products/<id>` temos o retorno do produto indicado pelo id no header da requisição. Utilizando esse `<id>` fazemos uma iteração via `products` uitilizando um for, e quando achamos aquele determinado produto com esse id retornamos esse produto. Coloquei um try/except para caso dê algum erro nessa busca, retornar essa mensagem de erro.

A rota `/products/<id>/stock` retorna a quantidade que tem no estoque do produto com o id passado no header. A logica é bem parecida com a realizada na rota acima, apenas com um plus, caso encontre esse id dentro dos produtos, se faz outra iteração para achar esse mesmo produto na variável que contem o estoque `stock`.


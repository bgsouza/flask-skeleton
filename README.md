# Flask Skeleton API
Proposta de modelo para trabalhar com o framework Flask.
Propõe estrturação de diratórios, inicializadores, exemplos de uso de ORM e Redis


# API Flask
Existem duas formas de se executar o projeto:

    - Forma 1: Execução manual (local) na raiz: 
        - $ pipenv --three (!!! ATENÇÃO caso ja tenha executado esta linha, não precisa executa-la novamente)
        - $ pipenv shell
        - $ export APP_CONFIG_ENV=.env
        - $ flask run
        - Modo iterativo:
            - $ flask shell    
    - Forma 2: Executando em Docker
        - Exceução padrão:
            - $ docker-compose up -d --build
        - Compilando versão de QA
            - Criando uma imagem:
                - $ docker build -t app_cand_lata:<version> .
            - Atualizar "image" com o nome app_cand_lata:<version> no arquivo "docker-compose-qa.yml"
            - Rodar o docker ed QA:
                - $ docker-compose -f docker-compose-qa.yml up -d

# Testes
Existem duas formas de se executar o teste

     - Forma 1 (caso a aplicação esteja executando localmente):
       - $ pipenv shell
       - $ python -m unittest tests/* 
     - Forma 2 (caso a aplicação esteja executando via docker):
       - $ docker-compose exec app /bin/bash
       - $ python -m unittest tests/* 

# Ajuda e Extras

## Flask DB
- Comandos do flask db:
    - flask db init: prepara as migrations (models.py)
    - flask db migrate: excuta as migrations
    - flask db upgrade: envia as tabelas

- Acessar postgres  
  - docker network create --driver bridge postgres-network
  - docker run -it --rm --name some-postgres --network postgres-network -e "POSTGRES_PASSWORD=123456" -p 5432:5432 -d 
  postgres
  - docker exec -it some-postgres bash
    -  psql -U postgres
- Helps Postgres
    - `\l`: lista databases
    - `create database <database>;` : cria um database, ex: flask_contacts
    - `\connect <database>`: seleciona database
    - `\dt`: lista as tabelas de um <database>
    - `\d+ <table>`: mostra a estrutura da tabela

## Redis
        Uso via flask shell
        - Testando instância do redis
            - $ r
        - Set simples
            - $ r.set("chave",123)
        - Get simples
            - $ r.get("chave")
        - Adicionando itens de teste
            - $ r.zincrby("teste",1,"batata")
            - $ r.zincrby("teste",1,"cenoura")
            - $ r.zincrby("teste",1,"maça")
        - Consultando o ranking geral
            - $ r.zrange("teste", 0 , -1)
        - Consultando o ranking de um item
            - $ r.zscore("teste","batata")

## Gerar o requirements.txt
    - Atualizar pipenv
    - $ pipenv run pip freeze > requirements.txt

## Docker
    - Apagar as imagens orfãns (docker)
    - docker rmi -f $(docker images -f "dangling=true" -q) 

## Suporte ao Postman
Importar o arquivo `Flask-Contacts.postman_collection.json` para o Postman 

## Author
Bruno Gomes de Souza <bruno@bgsouza.com> [![StackShare](https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/bgsouza/profile)

# Contribuição
    1. Crie sua feature branch: git checkout -b my-new-feature
    2. Commit suas mudanças: git commit -am 'Add some feature'
    3. Envie seu branch para o repositório: git push origin my-new-feature
    4. Envie um Pull Request :D

# SAMBA Br Project

Plataforma para promoção do Plano Municipal de Saneamento Básico.

# Instalação

## Passo 1

Adcionar sua chave ssh ao projeto.
Se não conseguir, mande a chave para cleyton@tagi.com.br

## Passo 2

### Clone o projeto

    $ git clone git@gitlab.com:sambabr/samba-server.git

### Construa o ambiente Virtual

Se você não tem python3, virtualenv e pip3 instale.
Criando ambiente virtua:

    $ cd samba-server/
    $ virtualenv -p python3 venv

Ative seu ambeinte virtualenv

    $ source venv/bin/activate

O resultado será:

    (venv) $

Agora precisamos instalar as dependências.

    (venv) $ pip3 install -r requirements.txt

Configurações para ambiente Dev.
Primeiro configure suas variaveis de ambeinte, elas vão entá em um arquivo de texto chamado .env um modelo exite em .env.example, faça uma copia dele.

    (venv) $ cp .env.example .env

Agora só precisa editar a linha referente ao drive, mude de postgres para sqlite3, altere a variavel:

- SAMBA_DATABASE_URL para sqlite, Ex. -> SAMBA_DATABASE_URL=sqlite:///samba.db

Construa a base de dados da aplicação:

    (venv) $ ./manage.py migrate

Carregue os dados das cidades, os dados estão em um arquivo JSON loaddata/geo_data/initial_data.json
Para carregar utilize um loaddata do proprio django.

    (venv) $ ./manage.py loaddata loaddata/geo_data/initial_data.json

Crie um usuário admin

    (venv) $ ./manage.py createsuperuser

Agora rode a aplicação

    (venv) $ ./manage.py runserver

Acesse a aplicação em um navegador de internet: http://localhost:8000

# Comunidade Marujos
## Considerações
A Comuidade Marujos tem como objetivo compartilhar informações referente ao mundo do desenvolvimento. Este projeto é referente ao site principal da comunidade em estágio de desenvolvimento. Todas as sugestões e colaborações são bem vindas.

## Informações
Este projeto foi desenvolvido utilizando o Django v3.0.5 e o PostgreSQL v12.2.
- [django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [pgAdmin](https://www.pgadmin.org/)

## Instalação

- Crie o arquivo .env baseado no arquivo .env.example
- Insira as credenciais do banco de dados no arquivo .env

- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
    ```
    virtualenv venv
    Linux: source venv/bin/activate
    Windows: virtualenv\virtual_1\Scripts\activate
    ```
    
- Requirements
    ```
    pip install -r requirements.txt
    ```
- Create SECRET_KEY
    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```
    Insira a SECRET_KEY gerada no arquivo .env
    
- Migrations
    ```
    python manage.py migrate
    ```
    
- Superuser
    ```
    python manage.py createsuperuser
    ```
- Execute
    ```
    python manage.py runserver
    ```
  

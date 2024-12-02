# PostManager

PostManager é uma aplicação **FastAPI** para gerenciar postagens e histórico de postagens com autenticação baseada em OAuth2 e cache com Redis para otimizar o desempenho das operações.

## 🎯 Funcionalidades

- **Gerenciamento de Postagens**: Criação, listagem, consulta por ID e atualização do status de postagens.
- **Histórico de Postagens**: Rastreie alterações de status de cada postagem.
- **Autenticação**: Sistema de login com geração de tokens JWT.
- **Cache**: Implementação de cache com Redis para rotas GET.
- **Organização**: Código estruturado em camadas (rota, serviço, repositório e cache).

---

## 🚀 Como rodar o projeto

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.10+](https://www.python.org/)

### 🛠 Dependências
Dependências de Python
- [FastAPI](https://fastapi.tiangolo.com): Framework para construção de APIs rápidas e escaláveis.
- [Uvicorn](https://www.uvicorn.org): Servidor ASGI para rodar a aplicação FastAPI.
- [SQLAlchemy](https://www.sqlalchemy.org): ORM para interagir com o banco de dados.
- [Psycopg2](https://pypi.org/project/psycopg2/): Driver para conexão com PostgreSQL.
- [Redis-py](https://pypi.org/project/redis/): Biblioteca para interação com o servidor Redis.
- [python-jose](https://python-jose.readthedocs.io/en/latest/): Para geração e validação de tokens JWT.
- [Passlib](https://passlib.readthedocs.io/en/stable/): Para hashing de senhas.
- [Pydantic](https://docs.pydantic.dev/latest/): Para validação e serialização de dados.

Dependências de Banco de Dados
- [PostgreSQL](https://www.postgresql.org): Banco de dados relacional utilizado para armazenar dados.

Ferramentas de Cache
- [Redis](https://redis.io): Utilizado para implementação do sistema de cache.

Ferramentas de Contêinerização
- [Docker](https://www.docker.com): Para empacotar a aplicação e suas dependências.
- [Docker Compose](https://docs.docker.com/compose/): Para orquestrar os serviços da aplicação (API, PostgreSQL e Redis).

### 🛡 Segurança
- Autenticação: Implementada com JWT.
- Variáveis sensíveis: Armazenadas em um arquivo .env.

### 💡Funcionalidades Principais
 Postagens:
- Cadastro de postagens.
- Listagem com paginação.
- Atualização de status.

 Histórico:
- Registro das alterações realizadas nas postagens.
- Consulta ao histórico de uma postagem específica.

 Usuários:
- Cadastro de novos usuários.
- Login com geração de token JWT.

### ⏯ Passos para executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-RoggerMartins22/PostManager
   cd seu-repositorio

2. **Suba os serviços com Docker Compose:**
    ```bash
    docker-compose up --build

3. **Acesse a aplicação:**
- Documentação interativa Swagger: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

### 🧪 Testes
Como testar a API?
- 1 - Use ferramentas como Postman ou Insomnia.
- 2 - Insira o Bearer Token no cabeçalho das requisições protegidas.
- 3 - Utilize as rotas disponíveis no Swagger para validar o funcionamento.
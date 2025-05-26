# 🧼 Quart Clean Architecture API

Uma API moderna desenvolvida com [Quart](https://pgjones.gitlab.io/quart/) (um Flask assíncrono) utilizando os princípios da **Clean Architecture**. A API possui autenticação JWT, CRUD de usuários e login, documentação Swagger, e persistência assíncrona com `aiosqlite`.

---

## 📁 Estrutura do Projeto

quart-clean-arch/
│
├── app/
│ ├── controllers/ # Controladores (rotas organizadas por domínio)
│ ├── core/ # Lógica compartilhada (autenticação, segurança, utils)
│ ├── docs/ # Swagger JSON (documentação da API)
│ ├── entities/ # Entidades da aplicação
│ ├── repositories/ # Repositórios que acessam o banco de dados
│ ├── routes/ # Registro das rotas
│ ├── usecase/ # Casos de uso (regras de negócio)
│ ├── database.py # Conexão assíncrona com SQLite
│ └── config.py # Configurações gerais (chave JWT, DB path etc.)
│
├── main.py # Ponto de entrada da aplicação
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo


---

## 🚀 Como Rodar o Projeto

### 1. Clone o projeto

```
git clone https://github.com/seu-usuario/quart-clean-arch.git
cd quart-clean-arch
```

### 2. Ambiente virtual
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar as dependências
```
pip install -r requirements.txt
```

### 4. Rodando o app
```
python main.py
```

A API será servida em: http://localhost:5000
Com documentação : http://localhost:5000/docs


🛠️ Rotas Disponíveis
✅ Registro & Autenticação
Método	Rota	Descrição
POST	/register	Registra novo usuário
POST	/login	Login com JWT

👤 Usuários (JWT obrigatório)
Método	Rota	Descrição
GET	/users	Lista todos os usuários
GET	/users/<id>	Busca um usuário por ID
PUT	/users/<id>	Atualiza dados do usuário
DELETE	/users/<id>	Deleta o usuário

🔐 Logins (JWT obrigatório)
Método	Rota	Descrição
GET	/logins	Lista todos os logins
GET	/logins/<user_id>	Busca login por ID
PUT	/logins/<user_id>	Atualiza login
DELETE	/logins/<user_id>	Exclui login


🧪 Tecnologias Usadas
Quart

SQLite + aiosqlite

JWT para autenticação

Clean Architecture (controller, usecase, repository, entity)

Swagger para documentação

✅ Requisitos
Python 3.8+

Quart

aiosqlite

pyjwt

bcrypt


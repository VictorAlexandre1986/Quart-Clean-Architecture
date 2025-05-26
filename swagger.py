swagger_spec = {
  "openapi": "3.0.0",
  "info": {
    "title": "Quart Clean Architecture API",
    "version": "1.0.0"
  },
  "paths": {
    "/register": {
      "post": {
        "summary": "Registrar novo usuário",
        "requestBody": {
          "required": True,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" },
                  "email": { "type": "string" },
                  "password": { "type": "string" }
                },
                "required": ["name", "email", "password"]
              }
            }
          }
        },
        "responses": {
          "200": { "description": "Usuário registrado com sucesso" },
          "400": { "description": "Erro de validação" }
        }
      }
    },
    "/login": {
      "post": {
        "summary": "Login de usuário",
        "requestBody": {
          "required": True,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "email": { "type": "string" },
                  "password": { "type": "string" }
                },
                "required": ["email", "password"]
              }
            }
          }
        },
        "responses": {
          "200": { "description": "Login bem-sucedido, retorna token JWT" },
          "400": { "description": "Credenciais inválidas" }
        }
      }
    },
    "/users": {
      "get": {
        "summary": "Listar todos os usuários",
        "security": [{ "bearerAuth": [] }],
        "responses": {
          "200": { "description": "Lista de usuários" }
        }
      }
    },
    "/users/{user_id}": {
      "get": {
        "summary": "Obter usuário por ID",
        "security": [{ "bearerAuth": [] }],
        "parameters": [
          {
            "name": "user_id",
            "in": "path",
            "required": True,
            "schema": { "type": "integer" }
          }
        ],
        "responses": {
          "200": { "description": "Usuário encontrado" },
          "404": { "description": "Usuário não encontrado" }
        }
      },
      "put": {
        "summary": "Atualizar usuário",
        "security": [{ "bearerAuth": [] }],
        "parameters": [
          {
            "name": "user_id",
            "in": "path",
            "required": True,
            "schema": { "type": "integer" }
          }
        ],
        "requestBody": {
          "required": True,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" },
                  "email": { "type": "string" },
                  "password": { "type": "string" }
                }
              }
            }
          }
        },
        "responses": {
          "200": { "description": "Usuário atualizado com sucesso" },
          "404": { "description": "Usuário não encontrado" }
        }
      },
      "delete": {
        "summary": "Deletar usuário",
        "security": [{ "bearerAuth": [] }],
        "parameters": [
          {
            "name": "user_id",
            "in": "path",
            "required": True,
            "schema": { "type": "integer" }
          }
        ],
        "responses": {
          "200": { "description": "Usuário deletado com sucesso" },
          "404": { "description": "Usuário não encontrado" }
        }
      }
    },
    "/logins": {
      "get": {
        "summary": "Listar todos os logins",
        "security": [{ "bearerAuth": [] }],
        "responses": {
          "200": { "description": "Lista de logins" }
        }
      }
    },
    "/logins/{user_id}": {
      "get": {
        "summary": "Obter login por ID",
        "security": [{ "bearerAuth": [] }],
        "parameters": [
          {
            "name": "user_id",
            "in": "path",
            "required": True,
            "schema": { "type": "integer" }
          }
        ],
        "responses": {
          "200": { "description": "Login encontrado" },
          "404": { "description": "Login não encontrado" }
        }
      },
      "put": {
        "summary": "Atualizar login",
        "security": [{ "bearerAuth": [] }],
        "parameters": [
          {
            "name": "user_id",
            "in": "path",
            "required": True,
            "schema": { "type": "integer" }
          }
        ],
        "requestBody": {
          "required": True,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "email": { "type": "string" },
                  "password": { "type": "string" }
                }
              }
            }
          }
        },
        "responses": {
          "200": { "description": "Login atualizado com sucesso" },
          "404": { "description": "Login não encontrado" }
        }
      },
      "delete": {
        "summary": "Excluir login",
        "security": [{ "bearerAuth": [] }],
        "parameters": [
          {
            "name": "user_id",
            "in": "path",
            "required": True,
            "schema": { "type": "integer" }
          }
        ],
        "responses": {
          "200": { "description": "Login deletado com sucesso" },
          "404": { "description": "Login não encontrado" }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  }
}

from quart import request, jsonify
from app.core.auth import jwt_required, verify_token
from app.repositories.user_repository import UserRepository
from app.usecase.user_usecase import UserUseCase

async def user_controller(app, db_session):

    @app.post("/register")
    async def register():
        data = await request.json
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        try:
            user = await usecase.register(data["name"], data["email"], data["password"])
            return jsonify({"id": user.id, "email": user.email})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.post("/login")
    async def login():
        data = await request.json
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        try:
            return jsonify(await usecase.login(data["email"], data["password"]))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.get("/users")
    @jwt_required
    async def get_users():
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        users = await usecase.get_all_users()
        return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

    @app.get("/users/<int:user_id>")
    @jwt_required
    async def get_user(user_id):
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        user = await usecase.get_user_by_id(user_id)
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
        return jsonify({"id": user.id, "name": user.name, "email": user.email})

    @app.put("/users/<int:user_id>")
    @jwt_required
    async def update_user(user_id):
        data = await request.json
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        try:
            user = await usecase.update_user(user_id, data)
            return jsonify({"id": user.id, "name": user.name, "email": user.email})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    @app.delete("/users/<int:user_id>")
    @jwt_required
    async def delete_user(user_id):
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        try:
            await usecase.delete_user(user_id)
            return jsonify({"msg": "Usuário deletado"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    @app.get("/verify-token")
    @jwt_required
    async def verify_user_token():
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token não fornecido"}), 401
        try:
            user_data = await verify_token(token)
            return jsonify(user_data)
        except ValueError as e:
            return jsonify({"error": str(e)}), 401

    @app.get("/logout")
    @jwt_required
    async def logout():
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token não fornecido"}), 401
        try:
            await verify_token(token, logout=True)
            return jsonify({"msg": "Usuário deslogado com sucesso"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 401

    @app.get("/logins")
    @jwt_required
    async def list_logins():
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        users = await usecase.get_all_logins()
        return jsonify([{"id": u.id, "email": u.email} for u in users])

    @app.get("/logins/<int:user_id>")
    @jwt_required
    async def get_login(user_id):
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        try:
            user = await usecase.get_login_by_id(user_id)
            return jsonify({"id": user.id, "email": user.email})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    @app.put("/logins/<int:user_id>")
    @jwt_required
    async def update_login(user_id):
        data = await request.json
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        try:
            user = await usecase.update_login(user_id, data)
            return jsonify({"id": user.id, "email": user.email})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    @app.delete("/logins/<int:user_id>")
    @jwt_required
    async def delete_login(user_id):
        repo = UserRepository(db_session())
        usecase = UserUseCase(repo)
        try:
            await usecase.delete_login(user_id)
            return jsonify({"msg": "Login deletado"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

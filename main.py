from quart import Quart, jsonify
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_session
from app.models.user_model import Base
from app.controllers.user_controller import user_controller
from app.core.config import DATABASE_URL
from swagger import swagger_spec
from app.routes.routes import register_routes


app = Quart(__name__)
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# Registra rotas
register_routes(app, async_session)

@app.before_serving
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await user_controller(app, SessionLocal)

@app.route("/swagger.json")
async def swagger_json():
    return jsonify(swagger_spec)

@app.route("/docs")
async def swagger_ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Swagger UI</title>
        <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css" />
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
        <script>
        const ui = SwaggerUIBundle({
            url: '/swagger.json',
            dom_id: '#swagger-ui'
        });
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()

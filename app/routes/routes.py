from app.controllers.user_controller import user_controller

def register_routes(app, db_session):
    app.before_serving(lambda: user_controller(app, db_session))

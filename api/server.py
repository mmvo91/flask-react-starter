from flask import Flask

from api import routes
from api.extensions import sql, ma, bcrypt, jwt
from api.config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    sql.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(routes.api_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()

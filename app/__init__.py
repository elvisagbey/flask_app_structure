from flask import Flask


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    # initialize extensions
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # add routes

    return(app)

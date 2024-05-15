from flask import Flask
from utils.db import db
from flask_migrate import Migrate
from config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['default'])
    db.init_app(app)

    Migrate(app, db)

    with app.app_context():
        db.create_all()

    from routes.hello_route import hello_route
    from routes.author_route import author_routes
    from routes.book_route import book_routes

    app.register_blueprint(hello_route)
    app.register_blueprint(author_routes)
    app.register_blueprint(book_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
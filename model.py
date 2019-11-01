from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    Game.query.delete()
    checkers = Game(name='checkers', description='board game with red and black chips')
    hot_potato = Game(name='hot-potato', description='pass around a potato until time runs out!')

    db.session.add_all([checkers, hot_potato])
    db.session.commit()


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")

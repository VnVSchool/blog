from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.secret_key = 'seOnI5C9Jx6V57JOC9elNvxKrMjYD6pM'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@db:3306/vnv_blog"

db = SQLAlchemy(app)

migrate = Migrate(app, db)

with app.app_context():
    from routes.main import *
    from routes.articles import *
    from routes.users import *
    from models import Article, User

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kamila@localhost:5432/dictionary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = "dict"
    id = db.Column(db.Integer, primary_key=True)
    description1 = db.Column(db.String(), nullable=False)
    description2 = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'< {self.description1} - {self.description2}>'


db.create_all()


@app.route('/')
def index():
    rand = db.session.query(func.count(Todo.id)).scalar()
    random_number = random.randrange(0, rand)

    output = Todo.query.get(random_number)

    return render_template('index.html', random_number=random_number, output=output)


if __name__ == '__main__':
    app.run(debug=True)

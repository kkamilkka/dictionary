from flask import Flask, render_template, url_for, request, redirect, abort
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
        global nl_trans
        nl_trans = self.description2
        return f'{self.description1}'


db.create_all()


@app.route('/form', methods=['post'])
def form():
    pl_translation = request.form['pl_translation']
    nl_translation = request.form['nl_translation']
    if nl_translation == nl_trans:
        return render_template('goed.html', pl_translation=pl_translation, nl_translation=nl_translation)
    else:
        print('zle')

    #return render_template('index.html')


@app.route('/')
def index():
    rand = db.session.query(func.count(Todo.id)).scalar()
    random_number = random.randrange(1, rand + 1)

    output = Todo.query.get(random_number)

    return render_template('index.html', output=output)


if __name__ == '__main__':
    app.run(debug=True)

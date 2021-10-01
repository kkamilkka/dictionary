from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select
from sqlalchemy.sql import and_
import random
from sqlalchemy.dialects import postgresql

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
        return f'< id: {self.id}, description: {self.description1}, description: {self.description2}>'


db.create_all()


@app.route('/')
def index():
    rand = db.session.query(func.count(Todo.id)).scalar()
    random_number = random.randrange(0, rand)

    stmt = select([Todo.__table__.columns.description1, Todo.__table__.columns.description2])
    stmt = stmt.where(and_(Todo.id == random_number))
    result = stmt.compile(dialect=postgresql.dialect())
    print (result)
    # print(stmt)

    return render_template('index.html', rand=rand, random_number=random_number, result=result)


if __name__ == '__main__':
    app.run(debug=True)

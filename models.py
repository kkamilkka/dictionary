from app import db

class Todo(db.Model):
    __tablename__ = "_dict"# zmien
    id = db.Column(db.Integer, primary_key=True)
    description1 = db.Column(db.String(), nullable=False)
    description2 = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'{self.description1, self.description2}'


db.create_all()


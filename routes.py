from crypt import methods
from app import app
from flask import render_template

@app.route('/')
def index():
    rand = db.session.query(func.count(Todo.id)).scalar()
    random_number = random.randrange(1, rand + 1)
    output = Todo.query.get(random_number)
    return render_template('index.html', output=output)


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('submitted title', form.title.data)
        return render_template('about.html', form=form, title=form.title.data)
    return render_template('about.html', form=form)


    # return render_template('index.html')


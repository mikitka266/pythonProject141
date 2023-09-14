from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProject

from form import RegistrationForm

app = Flask(__name__)


app.config['SECRET KEY'] = '121292kimono'
csrf = CSRFProject(app)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///mydatabase_user.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Homework3'

@app.cli.command('/init')
def init():
    db.create_all()
    print('OK')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        return f'You are success registration'
    return render_template('login.html', form=form)


if __name__== '__main__':
    app.run(debug=True)
import sqlalchemy
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_login import LoginManager, login_user

from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

login_manager = LoginManager()
login_manager.init_app(app)


class RegisterForm(FlaskForm):
    email = StringField('Login / Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
def home():
    jobs = session.query(Jobs).all()
    return render_template('home.html', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            email = form.email.data
            password = form.password.data
            surname = form.surname.data
            name = form.name.data
            age = form.age.data
            position = form.position.data
            speciality = form.speciality.data
            address = form.address.data

            user = User(email=email, surname=surname, name=name, age=age, position=position, speciality=speciality,
                        address=address)
            user.set_password(password)
            session.add(user)
            session.commit()
            return redirect('/')
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            return redirect('/register')

    return render_template('register.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)

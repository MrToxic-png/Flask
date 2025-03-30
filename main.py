import sqlalchemy
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email

from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()


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
                        address=address, hashed_password=password)
            session.add(user)
            session.commit()
            return redirect('/')
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            return redirect('/register')

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)

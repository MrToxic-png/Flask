import sqlalchemy
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_login import LoginManager, login_user, current_user, logout_user

from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
username = None

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


class AddJobForm(FlaskForm):
    team_lead = IntegerField('Id лидера', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = IntegerField('Количесво часов', validators=[DataRequired()])
    collaborators = StringField('Список id рабочих', validators=[DataRequired()])
    is_finished = BooleanField('Работа закончена?')
    submit = SubmitField('Завершить')


@app.route('/')
def home():
    global username
    if current_user.is_authenticated and username:
        jobs = session.query(Jobs).all()
        return render_template('home.html', username=username, jobs=jobs, user=current_user)
    else:
        return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    global username
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
            username = name + ' ' + surname
            return redirect('/')
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            return redirect('/register')

    return render_template('register.html', username=username, form=form, user=current_user)


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global username
    logout_user()
    form = LoginForm()
    if form.validate_on_submit():
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            username = user.name + ' ' + user.surname
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form, user=current_user)

    return render_template('login.html', title='Авторизация', username=username, form=form, user=current_user)


@app.route('/addjob', methods=['GET', 'POST'])
def addjob():
    global username
    if not username:
        return redirect('/login')
    form = AddJobForm()
    if form.validate_on_submit():
        new_job = Jobs(team_leader=form.team_lead.data, job=form.job.data, work_size=form.work_size.data,
                       collaborators=form.collaborators.data, is_finished=form.is_finished.data)
        session.add(new_job)
        session.commit()
        return redirect('/')
    return render_template('addjob.html', username=username, form=form, user=current_user)


@app.route('/editjob/<int:job_id>', methods=['GET', 'POST'])
def editjob(job_id):
    form = AddJobForm()
    jobs = session.query(Jobs).filter(Jobs.id == job_id).first()
    if not jobs:
        return redirect('/')
    if jobs.team_leader != current_user.id and current_user.id != 1:
        return redirect('/')
    if form.validate_on_submit():
        jobs.job = form.job.data
        jobs.team_leader = form.team_lead.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_finished.data
        session.commit()
        return redirect('/')

    return render_template('editjob.html', username=username, form=form, user=current_user)

@app.route('/deletejob/<int:job_id>', methods=['GET', 'POST'])
def deletejob(job_id):
    jobs = session.query(Jobs).filter(Jobs.id == job_id).first()
    if not jobs:
        return redirect('/')
    if jobs.team_leader != current_user.id and current_user.id != 1:
        return redirect('/')
    session.delete(jobs)
    session.commit()
    return redirect('/')



if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)

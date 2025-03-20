from flask import Flask, render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_wtf_key'


class LoginForm(FlaskForm):
    astronaut_id = StringField('Id астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('Id капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<lst>')
def list_prof(lst):
    return render_template('professions.html', lst=lst)


@app.route('/answer')
@app.route('/auto_answer')
def anwser():
    slowar = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман',
        'sex': 'male',
        'motivation': 'застрять на марсе',
        'ready': True
    }
    return render_template('auto_answer.html', **slowar)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/submit')
    return render_template('login.html', form=form)

@app.route('/submit')
def submit():
    return 'ptichka'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

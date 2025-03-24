from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    """user = User(surname='Лудоман', name='Семен', age=0, position='я хз сколько ему', speciality='programmer',
                address='module_0', email='semuk@git.hub')
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()"""


if __name__ == '__main__':
    main()

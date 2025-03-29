import datetime

from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data.jobs import Job
from data.users import User
from data import db_session

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run('127.0.0.1', port=8080)


@app.route('/')
def home():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    return render_template('home.html', jobs=jobs)


if __name__ == '__main__':
    main()

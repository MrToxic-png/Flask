from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_wtf_key'


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)

@app.route('/list_prof/<lst>')
def list_prof(lst):
    return render_template('professions.html', lst=lst)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

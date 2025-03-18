from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lst = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
           "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]

    return "</br>".join(lst)


@app.route('/image_mars')
def image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  <img src="{url_for('static', filename='img/mars.png')}" 
              alt="здесь должна была быть картинка, но не нашлась">
                    <div>Еше что то</div>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!DOCTYPE HTML>
    <head>
    <meta charset="utf-8">
    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
    <h1>
    Жди нас, Марс!
    </h1>
    <img src="{url_for('static', filename='img/mars.png')}" 
              alt="здесь должна была быть картинка, но не нашлась">
    <div class="alert alert-primary" role="alert">
    Человечество вырастает из детства
    </div>
    <div class="alert alert-secondary" role="alert">
    Человечеству мала одна планета
    </div>
    <div class="alert alert-thirdly" role="alert">
    Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    </body>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

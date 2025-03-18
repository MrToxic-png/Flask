from flask import Flask, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return """
            <!DOCTYPE HTML>
            <head>
            <meta charset="utf-8">
            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
            <link href="{{ url_for('static', filename='css/forum_style.css') }}" rel="stylesheet">
            </head>
            <body>
            <h1>
            Анкета претендента
            </h1>
            <h2>
            на участие в миссии
            </h2>
            <div>
                <form class="login_form" method="POST">
                    <input type="lustname" class="form-control" id="lustname" placeholder="Фамилия" name="lustname">
                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                    <div class="form-group">
                        <label for="classSelect">Образование</label>
                        <select class="form-control" id="education" name="education">
                          <option>Начальное общее</option>
                          <option>Основное общее</option>
                          <option>Среднее общее</option>
                          <option>Среднее профессиональное</option>
                          <option>Высшее</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="about">Профессии</label>
                    </div>
                      <label>
                        <input type="checkbox" name="interests" value="job1">
                        инженер-исследователь
                      </label><br>
                      <label>
                        <input type="checkbox" name="interests" value="job2">
                        пилот
                      </label><br>
                      <label>
                        <input type="checkbox" name="interests" value="job3">
                        строитель
                      </label><br>
                      <label>
                        <input type="checkbox" name="interests" value="job4">
                        экзобиолог
                      </label><br>
                      <label>
                        <input type="checkbox" name="interests" value="job5">
                        врач
                      </label><br>
                      <label>
                        <input type="checkbox" name="interests" value="job6">
                        климатолог
                      </label><br>
                      <label>
                        <input type="checkbox" name="interests" value="job7">
                        специалист по радиационной защите
                      </label><br>
                      <label>
                        <input type="checkbox" name="interests" value="job8">
                        астрогеолог
                      </label><br>
                    <div class="form-group">
                        <label for="form-check">Укажите пол</label>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                          <label class="form-check-label" for="male">
                            Мужской
                          </label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                          <label class="form-check-label" for="female">
                            Женский
                          </label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="about">Почему хотите учавствовать?</label>
                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="photo">Приложите фотографию</label><br>
                        <input type="file" class="form-control-file" id="photo" name="file">
                    </div>
                    <label>
                        <input type="checkbox" name="ready" value="ready">
                        Готовы остаться на марсе?
                      </label><br>
                      <button type="submit" class="btn btn-primary">Записаться</button>
                </form>
            </body>
            """
    elif request.method == 'POST':
        print(request.form['lustname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['ready'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    if planet_name == 'Mars':
        return '''<!DOCTYPE HTML>
    <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
    <h1 class="alert alert-heading" role="alert">
    мб Марс!
    </h1>
    <h2 class="alert alert-primary" role="alert">
    Близко
    </h2>
    <h3 class="alert alert-secondary" role="alert">
    Ресы
    </h3>
    <h4 class="alert alert-primary" role="alert">
    Вода
    </h4>
    <h5 class="alert alert-secondary" role="alert">
    Поле
    </h5>
    </body>'''
    elif planet_name == 'Jupiter':
        return '''<!DOCTYPE HTML>
            <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
            </head>
            <body>
            <h1 class="alert alert-heading" role="alert">
            мб Юпитер!
            </h1>
            <h2 class="alert alert-primary" role="alert">
            Крупная
            </h2>
            <h3 class="alert alert-secondary" role="alert">
            Газовая
            </h3>
            <h4 class="alert alert-primary" role="alert">
            Много водорода
            </h4>
            <h5 class="alert alert-secondary" role="alert">
            Еще что то
            </h5>
            </body>'''
    elif planet_name == 'Saturn':
        return '''<!DOCTYPE HTML>
                    <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    </head>
                    <body>
                    <h1 class="alert alert-heading" role="alert">
                    мб Сатурн!
                    </h1>
                    <h2 class="alert alert-primary" role="alert">
                    2 по размеру
                    </h2>
                    <h3 class="alert alert-secondary" role="alert">
                    Газовая
                    </h3>
                    <h4 class="alert alert-primary" role="alert">
                    Много водорода
                    </h4>
                    <h5 class="alert alert-secondary" role="alert">
                    Кольца вокруг
                    </h5>
                    </body>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

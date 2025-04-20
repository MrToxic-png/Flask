import sqlalchemy
from flask import Blueprint, jsonify, make_response, abort, request
from sqlalchemy.exc import SQLAlchemyError

from . import db_session
from .users import User

db_session.global_init("db/mars_explorer.db")

session = db_session.create_session()

blueprint = Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@blueprint.route('/api/users')
def get_users():
    users = session.query(User).all()
    list_of_dicts = []
    for user in users:
        dict_of_users = {'id': user.id, 'surname': user.surname, 'name': user.name, 'age': user.age,
                         'position': user.position, 'speciality': user.speciality, 'address': user.address,
                         'email': user.email, 'hashed_password': user.hashed_password}
        list_of_dicts.append(dict_of_users)

    return jsonify(list_of_dicts)


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_particular_users(user_id):
    if type(user_id) is not int:
        abort(400)
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        abort(404)

    dict_of_users = {'id': user.id, 'surname': user.surname, 'name': user.name, 'age': user.age,
                     'position': user.position, 'speciality': user.speciality, 'address': user.address,
                     'email': user.email, 'hashed_password': user.hashed_password}

    return jsonify(dict_of_users)


@blueprint.route('/api/users/', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    user = User(
        surname=request.json.get('surname'),
        name=request.json.get('name'),
        age=request.json.get('age'),
        position=request.json.get('position'),
        speciality=request.json.get('speciality'),
        address=request.json.get('address'),
        email=request.json.get('email'),
        hashed_password=request.json.get('hashed_password')
    )
    session.add(user)
    session.commit()
    return jsonify({'id': user.id})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_news(user_id):
    user = session.get(User, user_id)
    if user is None:
        abort(404)
    session.delete(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_job(user_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    changing_user = session.query(User).filter_by(id=user_id).first()
    changing_user.surname = request.json['surname']
    changing_user.name = request.json['name']
    changing_user.age = request.json['age']
    changing_user.position = request.json['position']
    changing_user.speciality = request.json['speciality']
    changing_user.address = request.json['address']
    changing_user.email = request.json['email']
    changing_user.hashed_password = request.json['hashed_password']
    session.commit()
    return jsonify({'id': changing_user.id})

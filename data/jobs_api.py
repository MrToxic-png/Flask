import sqlalchemy
from flask import Blueprint, jsonify, make_response, abort, request
from sqlalchemy.exc import SQLAlchemyError

from . import db_session
from .jobs import Jobs

db_session.global_init("db/mars_explorer.db")

session = db_session.create_session()

blueprint = Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@blueprint.route('/api/jobs')
def get_jobs():
    jobs = session.query(Jobs).all()
    list_of_dicts = []
    for job in jobs:
        dict_of_jobs = {'id': job.id, 'team_leader': job.team_leader, 'job': job.job, 'category': job.category,
                        'is_finished': job.is_finished, 'work_size': job.work_size, 'collaborators': job.collaborators,
                        'start_date': job.start_date, 'end_date': job.end_date}
        list_of_dicts.append(dict_of_jobs)

    return jsonify(list_of_dicts)


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_particular_jobs(job_id):
    if type(job_id) is not int:
        abort(400)
    job = session.query(Jobs).filter_by(id=job_id).first()
    if not job:
        abort(404)

    dict_of_jobs = {'id': job.id, 'team_leader': job.team_leader, 'job': job.job, 'category': job.category,
                    'is_finished': job.is_finished, 'work_size': job.work_size, 'collaborators': job.collaborators}

    return jsonify(dict_of_jobs)


@blueprint.route('/api/jobs/', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'is_finished', 'work_size', 'collaborators']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    type_conditions = (isinstance(request.json.get('job'), str),
                      isinstance(request.json.get('team_leader'), int),
                      isinstance(request.json.get('work_size'), int),
                      isinstance(request.json.get('collaborators'), str),
                      isinstance(request.json.get('is_finished'), bool))
    if not all(type_conditions):
        abort(400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        is_finished=request.json['is_finished'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})

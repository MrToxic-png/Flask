from flask import Blueprint, jsonify, make_response, abort

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


@blueprint.route('/api/jobs/<int:job_id>')
def get_particular_jobs(job_id):
    if type(job_id) is not int:
        abort(400)
    job = session.query(Jobs).filter_by(id=job_id).first()
    if not job:
        abort(404)

    dict_of_jobs = {'id': job.id, 'team_leader': job.team_leader, 'job': job.job, 'category': job.category,
                    'is_finished': job.is_finished, 'work_size': job.work_size, 'collaborators': job.collaborators,
                    'start_date': job.start_date, 'end_date': job.end_date}

    return jsonify(dict_of_jobs)

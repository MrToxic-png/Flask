import requests
from pprint import pprint


def test_correct():
    request = requests.put('http://127.0.0.1:8080/api/jobs/4',
                            json={'job': 'qwe', 'team_leader': 7, 'work_size': 15, 'collaborators': '2, 3',
                                  'is_finished': True})
    assert request.status_code == 200


def test_no_argument():
    request = requests.put('http://127.0.0.1:8080/api/jobs/4',
                            json={'team_leader': 7, 'work_size': 15, 'is_finished': True})
    assert request.status_code == 400


def test_invalid_job_type():
    request = requests.put('http://127.0.0.1:8080/api/jobs/4',
                            json={'job': 1, 'team_leader': 7, 'work_size': 15, 'collaborators': '2, 3',
                                  'is_finished': True})
    assert request.status_code == 400


def test_invalid_work_size_type():
    request = requests.put('http://127.0.0.1:8080/api/jobs/4',
                            json={'job': 'qwe', 'team_leader': 7, 'work_size': '15', 'collaborators': '2, 3',
                                  'is_finished': True})
    assert request.status_code == 400


if __name__ == '__main__':
    test_correct()
    test_no_argument()
    test_invalid_job_type()
    test_invalid_work_size_type()
    pprint(requests.get('http://127.0.0.1:8080/api/jobs').json())
    print('All tests passed')

import requests

def test_all_jobs():
    response = requests.get('http://127.0.0.1:8080/api/jobs')
    jsoned_jobs = response.json()

    assert response.status_code == 200
    assert isinstance(jsoned_jobs, list)

def test_particular_job():
    response = requests.get('http://127.0.0.1:8080/api/jobs/1')
    jsoned_job = response.json()

    assert response.status_code == 200
    assert isinstance(jsoned_job, dict)

def test_particular_job_id():
    response = requests.get('http://127.0.0.1:8080/api/jobs/1982674510986390813')

    assert response.status_code == 404

def test_particular_job_input():
    response = requests.get('http://127.0.0.1:8080/api/jobs/KiReal')

    assert response.status_code == 404


if __name__ == '__main__':
    test_all_jobs()
    test_particular_job()
    test_particular_job_id()
    test_particular_job_input()
    print('All tests passed')
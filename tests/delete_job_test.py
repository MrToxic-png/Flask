import requests
from pprint import pprint


def test_correct():
    request = requests.delete('http://127.0.0.1:8080/api/jobs/5')
    assert request.status_code == 200


def test_invalid_type():
    request = requests.delete('http://127.0.0.1:8080/api/jobs/qwe')
    assert request.status_code == 404


def test_invalid_id():
    request = requests.delete('http://127.0.0.1:8080/api/jobs/2109127390111')
    assert request.status_code == 404


if __name__ == '__main__':
    test_correct()
    test_invalid_type()
    test_invalid_id()
    pprint(requests.get('http://127.0.0.1:8080/api/jobs').json())
    print('All tests passed')
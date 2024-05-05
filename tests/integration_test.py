import os
import requests
from main import main


def test_integration(monkeypatch):

    def example_response_mock(*args, **kwargs):
        response = requests.Response()
        response.status_code = 200
        response._content = read_file('example.html').encode('utf-8')
        return response
    monkeypatch.setattr(requests, "get", example_response_mock)

    main()

def read_file(filename):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

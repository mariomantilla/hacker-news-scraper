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

    data = main()

    assert len(data[0]) == 30
    assert len(data[0]) == len(data[1]) + len(data[2])
    assert all(len(item['title'].split()) > 5 for item in data[1])
    assert all(len(item['title'].split()) <= 5 for item in data[2])

    comments = [item['comments_count'] for item in data[1] if item['comments_count'] is not None]
    points = [item['points'] for item in data[2] if item['points'] is not None]

    assert is_sorted(comments)
    assert is_sorted(points)

def read_file(filename):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def is_sorted(items):
    return all(items[i] <= items[i+1] for i in range(len(items) - 1))

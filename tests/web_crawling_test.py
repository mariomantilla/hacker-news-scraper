import pytest
import requests
from web_crawling import get_source_code


def mock_response(status, text, *args, **kwargs):
    response = requests.Response()
    response.status_code = status
    response._content = text.encode('utf-8')
    return response


def test_get_source_code_success(monkeypatch):

    def good_response_mock(*args, **kwargs):
        return mock_response(200, 'this worked!', *args, **kwargs)
    monkeypatch.setattr(requests, "get", good_response_mock)

    code = get_source_code('https://example.com')
    assert code == 'this worked!'


def test_get_source_code_fails(monkeypatch):

    def bad_response_mock(*args, **kwargs):
        return mock_response(404, 'error!', *args, **kwargs)
    monkeypatch.setattr(requests, "get", bad_response_mock)

    with pytest.raises(requests.HTTPError):
        get_source_code('https://example.com')

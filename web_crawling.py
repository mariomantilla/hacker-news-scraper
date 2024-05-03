import requests
import constants


def get_source_code(url):
    response = requests.get(url, timeout=constants.REQUEST_TIMEOUT)
    if response.status_code >= 400:
        response.raise_for_status()
    return response.text

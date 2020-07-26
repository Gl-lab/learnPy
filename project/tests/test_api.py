import pytest
import requests

from corona.main.api.api import API


def test_send_request():
    api = API()
    assert isinstance(api._send_request("acbdsdjlbkc"), str), "Should return UNDEFINED_LANGUAGE value"

    api = API("http://asdnalksjdsadkjlnsadkjlnsad")
    try:
        api._send_request("abc")
        assert False, "Must fail with this url"
    except requests.exceptions.ConnectionError:
        assert True


def test_pull_languages():
    texts = ["abcde", "hello world"]
    api = API()
    api.pull_languages(texts)
    assert len(api.languages) == len(texts), "self.languages not changed"
    languages_backup = api.languages.copy()
    api.pull_languages(texts)
    assert api.languages == languages_backup, "self.languages changed after same request"

    api = API()
    api.pull_languages(texts[0])
    assert len(api.languages) == 1, "self.languages not changed"
    api.pull_languages(texts[1])
    assert len(api.languages) == 2, "self.languages not changed"
    languages_backup = api.languages.copy()
    api.pull_languages(texts[0])
    assert api.languages == languages_backup, "self.languages changed after same request"


@pytest.fixture()
def prepare_get_language():
    api = API()
    api.pull_languages(["abcdef"])
    return api


def test_get_language(prepare_get_language):
    assert prepare_get_language.get_language("abc") is None, "got unexisting language"
    assert prepare_get_language.get_language("abcdef") is not None, "got None instead of language"

import os
import shutil

import pytest

from corona.main.api.constants import NOT_LABELED_LANGUAGE
from corona.main.local_files.local_files import LocalFiles
from tests.constants import BASE_DIR, IN_DIR, OUT_DIR


def test_constructor():
    try:
        LocalFiles("abc", "dcnjk")
        assert False, "ValueError for incorrect paths must be raised"
    except ValueError:
        assert True


@pytest.fixture(autouse=True)
def file_structure():
    os.makedirs(IN_DIR)
    os.makedirs(OUT_DIR)
    for file in os.listdir(r"tests\resources"):
        shutil.copy(os.path.join(r"tests\resources", file), os.path.join(IN_DIR, file))
    yield
    shutil.rmtree(BASE_DIR)


def test_read_file():
    lf = LocalFiles(IN_DIR, OUT_DIR)
    for file in os.listdir(IN_DIR):
        assert len(lf.read_file(os.path.join(IN_DIR, file))) <= 400, "text is too long"


def test_make_out_dir():
    lf = LocalFiles(IN_DIR, OUT_DIR)
    lf._make_out_dir("fr")
    assert os.path.isdir(os.path.join(OUT_DIR, "fr")), "incorrect out dir creation"
    lf._make_out_dir("fr")
    assert os.path.isdir(os.path.join(OUT_DIR, "fr")), "incorrect out dir creation"
    try:
        lf._make_out_dir('')
        assert False, "no ValueError for empty directory name"
    except ValueError:
        assert True


def test_prepare_paths():
    lf = LocalFiles(IN_DIR, OUT_DIR)
    lf.prepare_paths()
    assert len(lf.api.languages) == len(os.listdir(IN_DIR)), "incorrect length of api languages"


def test_move_files():
    lf = LocalFiles(IN_DIR, OUT_DIR)
    lf.move_files()
    assert os.listdir(OUT_DIR) == [NOT_LABELED_LANGUAGE], "some files appeared with no languages prepared"
    lf.prepare_paths()
    lf.move_files()
    assert len(os.listdir(OUT_DIR)) > 0, "no directories created"
    for directory in os.listdir(OUT_DIR):
        assert os.path.isdir(os.path.join(OUT_DIR, directory)), "not a directory"
    for directory in os.listdir(OUT_DIR):
        for file in os.listdir(os.path.join(OUT_DIR, directory)):
            assert os.path.isfile(os.path.join(OUT_DIR, directory, file)), "not a file"

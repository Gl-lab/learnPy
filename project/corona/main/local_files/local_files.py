
import datetime
import os.path
from language_sort.sorter.api.constants import FILE_STORE, FILE_STORE_INFO
from language_sort.sorter.api.api import API


class LocalFiles:
    def __init__(self):

        self.api = API()

    def read(self):
        with open(FILE_STORE) as f:
            text = f.read()
        return text

    def isHaveStore(self):
        return os.path.exists(FILE_STORE)

    def lastUpdate(self):
        with open(FILE_STORE_INFO) as f:
            text = f.read()
        return text

    def save(self, data):
        f = open(FILE_STORE, 'w')
        f.write(data)
        fc = open(FILE_STORE_INFO, 'w')
        fc.write(str(datetime.datetime.now()))

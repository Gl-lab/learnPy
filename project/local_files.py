
import datetime
import os.path
from constants import FILE_STORE, FILE_STORE_INFO
import json



class LocalFiles:

    def read(self):
        with open(FILE_STORE) as f:
            text = f.read()
            result = json.loads(text)
        return result

    def isHaveStore(self):
        return os.path.exists(FILE_STORE)

    def lastUpdate(self):
        with open(FILE_STORE_INFO) as f:
            text = f.read()
        return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

    def save(self, data):
        f = open(FILE_STORE, 'w')
        f.write(json.dumps(data))
        fc = open(FILE_STORE_INFO, 'w')
        fc.write(str(datetime.datetime.now()))

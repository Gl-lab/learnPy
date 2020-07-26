import requests

import datetime
from constants import PRE_BASE_URL, DEFAULT_COUNTRY, POST_BASE_URL
from local_files import LocalFiles

class API:
    def __init__(self, country=DEFAULT_COUNTRY):
        self.localStore = []
        self.country = country
        self.fileService = LocalFiles()

    def get_url(self):
        return PRE_BASE_URL+self.country+POST_BASE_URL

    def _send_request(self):
        response = requests.get(self.get_url())
        response.raise_for_status()
        response_dict = response.json()
        if response_dict:
            return response_dict
        else:
            print('error')
        return []

    def get_statistics(self):       
        if self.fileService.isHaveStore():
            if self.fileService.lastUpdate() <= datetime.datetime.now() - datetime.timedelta(days=1):
                self.fileService.save(self._send_request())    
        else:
            self.fileService.save(self._send_request())
        self.localStore =  self.fileService.read()
        return 'ok'
    
    def get_cases_by_date(self, date):#=str(datetime.datetime.today().strftime("%Y-%m-%d"))
        self.get_statistics()
        result = -1
        #date = datetime.datetime.strptime(date, "%Y-%m-%d")
        for item in self.localStore:
            Date = item.get('Date')
            Date = Date.replace('T',' ').replace('Z','')
            Date = datetime.datetime.strptime(Date, '%Y-%m-%d %H:%M:%S')
            if Date == date:    
                result = item.get('Cases')
        if result > 0:
            return 'За {} количество больных {}'.format(date, result)
        else: return 'На запрошенную дату отсутствуют данные'

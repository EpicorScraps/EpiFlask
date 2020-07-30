#Types.py
import requests
from requests.auth import HTTPBasicAuth

import pyodbc


class EpicorSQL:
    def __init__(self, sqlurl,user,password,db):
        self.sqlurl = sqlurl
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.sqlurl+';DATABASE='+self.db+';UID='+self.user+';PWD='+self.password)
        return cnxn.cursor()

    def sql(self,query):
        cur = self.connect()
        r = cur.execute(query)
        return r




class EpicorAPI:
    def __init__(self, appserverurl, user, password, name):
        self.AppServerURL = appserverurl
        self.User = user
        self.Pass = password
        self.name = name

    def get(self, apifunc, apifilter='', other=''):
        r = requests.get(
            self.AppServerURL + apifunc + (("?$filter=" + apifilter) if apifilter != "" else "") + other,
            auth=HTTPBasicAuth(self.User, self.Pass),
            verify=False,
            headers={'Content-type': 'application/json'}
        )
        print (self.AppServerURL + apifunc + (("?$filter=" + apifilter) if apifilter != "" else "") + other )
        return r
    def post(self, apifunc, data):
        r = requests.post(
            self.AppServerURL + apifunc,
            auth=HTTPBasicAuth(self.User, self.Pass),
            verify=False,
            data=data,
            headers={'Content-type': 'application/json'})
        return r


def pretty_time_delta(seconds):
    sign_string = '-' if seconds < 0 else ''
    seconds = abs(int(seconds))
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        return '%s%dd%dh%dm%ds' % (sign_string, days, hours, minutes, seconds)
    elif hours > 0:
        return '%s%dh%dm%ds' % (sign_string, hours, minutes, seconds)
    elif minutes > 0:
        return '%s%dm%ds' % (sign_string, minutes, seconds)
    else:
        return '%s%ds' % (sign_string, seconds)


class jItem:
    def __init__(self,vals):
        self.__dict__ = vals


from flask import Flask, render_template, send_from_directory, request, redirect, flash
import json
#from waitress import serve

from Types import EpicorAPI, jItem

app = Flask(__name__, static_url_path='')

#get epicor login details from secure txt
f=open("./creds.txt","r")
lines=f.readlines()
username=lines[0].rstrip()
password=lines[1].rstrip()
f.close()

APIURL = "https://erpappserver01.ddc.local/Production/api/v1/"

ProductionAPI = EpicorAPI(APIURL, username, password, "Production")
selectedAPI = ProductionAPI

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js',path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css',path)

@app.route('/media/<path:path>')
def send_media(path):
    return send_from_directory('media',path)

@app.route('/')
def main():
    x = selectedAPI.get('BaqSvc/act-currentusers(act)/')
    print(x.json()['value'])
    type(x)
    return render_template('index.html', peeps=[jItem(i) for i in x.json()['value']])


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

from flask import Flask, render_template, send_from_directory, request, redirect, flash
from waitress import serve



app = Flask(__name__, static_url_path='')


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
    return render_template('index.html')


if __name__ == '__main__j':
    app.run(host='0.0.0.0', debug=True)


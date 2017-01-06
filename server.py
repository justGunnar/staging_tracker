import json

from flask import Flask

app = Flask('server')

@app.route('/', methods=['GET'])
def home():
    return 'nosy little shit arent you'

@app.route('/list_stagings', methods=['GET'])
def list_staging():
    f = open('staging.json', 'r')
    return json.dumps(f.read(), indent=4)

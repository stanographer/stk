import json
import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, flash, jsonify, url_for, make_response
from flask_restful import Api
from .json_dictionary import Dictionary
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = os.environ.get('ALLOWED_EXTENSIONS')
MONGO_ENDPOINT = os.environ.get('MONGO_ENDPOINT')

app = Flask(__name__)
api = Api(app)

app.config['DICTIONARIES_DIRECTORY'] = os.environ.get('DICTIONARIES_DIRECTORY')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')

def read_json_dictionary(filename):
    print(filename)
    try:
        with open(os.path.join(app.config['DICTIONARIES_DIRECTORY'], filename)) as f:
            dictionary_file = json.load(f)
            codex = Dictionary(dictionary_file)

            return codex._entries

    except Exception as e:
        return 'There was an error reading your dictionary file.', e


def composed_response(status, message, payload):
    data = {
        'status': status,
        'message': message,
        'payload': payload,
    }

    response = make_response(jsonify(data))
    response.status = status
    response.mimetype = 'application/json'
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/')
def homepage_get():
    return render_template('upload.html', name='Upload', mongo_endpoint=MONGO_ENDPOINT)

@app.route('/edit')
def edit_get():
    return render_template('edit.html', name='Edit')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ('ALLOWED_EXTENSIONS')

def get_extension(filename):
    return filename.rsplit('.', 1)[1].lower()

@app.route('/upload-file', methods=['GET', 'POST'])
def upload_dictionary():
    # file = request.files['file']
    # user_id = request.args['sub']
    # file.save(os.path.join(app.config['DICTIONARIES_DIRECTORY'], secure_filename(file.filename)))
    
 

    sub = request.form.get('sub')
    file = request.files['file']
    now = datetime.now()
    extension = get_extension(file.filename)
    dictionary_name = secure_filename(f'{sub}_{now.strftime("%d/%m/%Y_%H:%M:%S")}.{extension}')

    file.save(os.path.join(app.config['DICTIONARIES_DIRECTORY'], dictionary_name))
    json_dictionary = read_json_dictionary(dictionary_name)

    print('JSON DICTIONARIIIIIIIIIIIIIIIIIII', json_dictionary)
    print(sub, json_dictionary, get_extension(file.filename))

    return composed_response(200, f'{file.filename} was uploaded successfully!', file.filename)

@app.route('/mongo-connect', methods=['GET'])
def get_mongo_connect():
    return MONGO_ADDRESS

@app.route('/addmongo', methods=['GET'])
def add_mongo():
    try:
        mongo_client.set_dictionary('testsub', {'test': 'hello'}, 'json')
    except Exception as e:
        return composed_response(500, 'Request could not be completed.', e)

    return composed_response(200, {'message', f'was uploaded successfully!'})

@app.route('/entries', methods=['GET'])
def entries_get():
    args = request.args
    json_dictionary = read_json_dictionary(args.get('filename'))
    message = 'We got you your dictionary successfully!'

    return composed_response(200, message, json_dictionary)

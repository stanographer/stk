import json
import os
from flask import Flask, render_template, redirect, request, flash, jsonify, url_for, make_response
from flask_restful import Api
from .json_dictionary import Dictionary
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = os.environ.get('ALLOWED_EXTENSIONS')
CODEX_LOCATION = os.environ.get('CODEX_LOCATION')
MONGO_ENDPOINT = os.environ.get('MONGO_ENDPOINT')

with open(CODEX_LOCATION) as f:
    dictionary_file = json.load(f)

codex = Dictionary(dictionary_file)
app = Flask(__name__)
api = Api(app)

app.config['UPLOAD_FOLDER'] = 'static/'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')

def composed_response(status, message, file_name):
    data = {
        'status': status,
        'message': message,
        'fileName': file_name,
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
        
@app.route('/upload-file', methods=['GET', 'POST'])
def upload_dictionary():
    file = request.files['file']
    file.save(secure_filename(file.filename))
    
    return composed_response(200, f'{file.filename} was uploaded successfully!', file.filename)

    # if request.method == 'POST':
    #     if 'file' not in request.files:
    #         flash('no file part')
    #         return redirect(request.url)

    #     # try:
    #     file = request.files['file']
    #     print(file.filename)

    #     if file.filename == '':
    #         flash('no selected file')
    #         return redirect(request.url)

    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(app.config['UPLOAD_FOLDER'], filename)
    #         # saved_file = open(app.config['UPLOAD_FOLDER'], filename)
    #         # content = saved_file.read()

    #         # return jsonify(content)
    #         return 'file uploaded successfully'
    #     # except Exception as e:
    #     #     print(f'Couldn\'t upload file {e}')
        

@app.route('/entries')
def entries_get():
    return codex._entries

@app.route('/define', methods=['POST'])
def entry_define():
    request_data = request.get_json()
    if not request_data:
        return 'Nothing!'
    
    return codex.entries_update(request_data)

from flask import Flask
from flask import request
from requests import codes
from time import time_ns
from os import walk
from json import dumps, loads
app = Flask(__name__)
headers = {'Content-Type': 'application/json'}



@app.route('/test-suites', methods=['GET'])
def get_suite_ids():

    return app.make_response((dumps(get_file_ids('./tests')), codes.ok, headers))


@app.route('/test-run', methods=['GET'])
def somename():
    run_id = time_ns()
    execution_paths = validate_ids(request.args.getlist('file_id'), './tests/')
    print(execution_paths)
    return execution_paths


def get_file_ids(execution_path, id_filter=None):
    list_of_dicts = []
    for root, dirs, files in walk(execution_path):
        for filename in files:
            if 'cpython' not in filename and 'conftest' not in filename:
                if id_filter is not None:
                    if filename.find(id_filter) != -1:
                        list_of_dicts.append({'id': filename.split('.py')[0]})
                else:
                    list_of_dicts.append({'id': filename.split('.py')[0]})
    return list_of_dicts


def validate_ids(file_ids, root_dir):
    execution_paths = []
    for file_id in file_ids:
        for root, dirs, files in walk(root_dir):
            if '{}.py'.format(file_id) in files:
                execution_paths.append('{}.py'.format(path.join(root, file_id)))
    if len(file_ids) != len(execution_paths):
        message = {'error': 'One or more file ids are not invalid!'}
        return app.make_response((message, codes.unprocessable_entity, headers))
    return execution_paths


if __name__ == '__main__':
    app.run(debug=True)

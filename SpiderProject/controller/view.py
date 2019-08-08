from flask import Flask, render_template, jsonify

from SpiderProject.dao.jobDao import JobDao

app = Flask(__name__)

dataDao = JobDao()


@app.route('/')
def index():
    return 'hello world'


@app.route('/data')
def data():
    return render_template('index.html')


@app.route('/get_data', methods=['GET'])
def get_data():
    data_info = {}
    data_info['echarts1'] = dataDao.query_indestury_field()
    return jsonify(data_info)

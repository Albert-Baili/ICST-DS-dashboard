import os
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

from readcsv import make_suggestions,get_rules,add_rules,generate_hash
from datamark import dealwithcsv,tuominLists

app = Flask(__name__)
CORS(app, resources=r'/*')

# 临时存储上传的CSV文件的目录
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/getrules', methods=['GET'])
def getrules():
 return get_rules()

@app.route('/addrules', methods=['POST'])
def addrules():
    requests_data=request.get_json()
    sensitive_fields = requests_data['sensitive_fields']
    range_fields=requests_data['range_fields']
    new_rules={
        'sensitive_fields':sensitive_fields,
        'range_fields':range_fields
        }
    print(new_rules)
    return add_rules(new_rules)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file_hash = generate_hash(file.filename)
        new_filename = file_hash + os.path.splitext(file.filename)[1]

        file.save(os.path.join(UPLOAD_FOLDER, new_filename))
       
        df = pd.read_csv(os.path.join(UPLOAD_FOLDER, new_filename))
        # 获取表头信息
        headers = df.columns
        suggestions = make_suggestions(headers)
        print(suggestions)
        ##接入数据库后重新修改
        return jsonify({'suggestions': suggestions,"file_id":file_hash}), 200

@app.route('/atuomin', methods=['POST'])
def atuomin():
    requests_data=request.get_json()
    suggestions = requests_data['suggestions']
    file_id= requests_data['file_id']
    return dealwithcsv(suggestions,file_id)

@app.route('/gettuolinLists', methods=['GET'])
def gettuolinLists():
 return {
    'success':True,
    'data':{
       'list':tuominLists[-40:]
    }
 }

@app.route('/api/asset_num', methods=['GET', 'POST'])
def get_data():
    msg = {'success': True,
           'data': {'alarmNum': 2, 'offlineNum': 17, 'onlineNum': 22, 'totalNum': 39},
           'msg': '出错啦！'}
    return jsonify(msg)


@app.route('/api/asset_info', methods=['GET', 'POST'])
def get_info():
    info = {
        'success': True,
        'data':
            [
                {
                    'devicename': 'Personal Computer',
                    'onlineState': 1,
                    'IP': '192.168.123.46',
                    'mac': '04:7C:16:DC:7A:D6'

                },
                {
                    'devicename': 'CyberTAN Technology',
                    'onlineState': 1,
                    'IP': '192.168.123.198',
                    'mac': '28:39:26:63:39:9D'

                },
                {
                    'devicename': 'Micro-Star Intl',
                    'onlineState': 1,
                    'IP': '192.168.123.45',
                    'mac': '24:7C:26:DC:7A:A6'

                },
                {
                    'devicename': 'Beijing Xiaomi Mobile Software',
                    'onlineState': 1,
                    'IP': '192.168.123.1',
                    'mac': 'D4:DA:21:0B:89:4F'

                },
                {
                    'devicename': 'Ruijie Networks',
                    'onlineState': 1,
                    'IP': '10.133.24.1',
                    'mac': '58:69:6C:4C:47:53'

                },
            ],
        'msg': '出错啦！',
    }
    return jsonify(info)

@app.route('/api/asset_graph', methods=['GET', 'POST'])
def graph():
    graph_info ={
        'success': True,
        'data': {
            'relations': [
                {
                  'id': 0,
                  'name': '总路由器',
                  'source': '',
                  'target': '',
                  'value': [50, 200]
                },
                {
                    'id': 1,
                    'name': '重要设备1',
                    'source': '重要设备1',
                    'target': '总路由器',
                    'value': [0, 300]
                },
                {
                  'id': 2,
                  'name': '重要设备2',
                  'source': '重要设备2',
                  'target': '总路由器',
                  'value': [0, 100]
                },
                {
                  'id': 3,
                  'name': '重要设备3',
                  'source': '总路由器',
                  'target': '重要设备3',
                  'value': [100, 100]
                },
                {
                  'id': 4,
                  'name': '重要设备4',
                  'source': '总路由器',
                  'target': '重要设备4',
                  'value': [100, 300]
                },
            ]
        },
        'msg': '出错啦！'
    }
    return jsonify(graph_info)

if __name__ == '__main__':
    app.run(debug=True)

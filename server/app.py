from flask import Flask
from flask import jsonify 
from flask_cors import CORS
import json
import MySQLdb

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

_db = MySQLdb.connect(host="localhost", user="root", passwd="QAQ不给你看", db='AquaSaying', charset='utf8')
_cursor = _db.cursor()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api', methods=['GET', 'POST'])
def week_price():
    sql = '''SELECT * FROM AquaSaying order by rand() limit 1;'''
    _cursor = _db.cursor()

    try:
        _cursor.execute(sql)
        row_headers = [x[0] for x in _cursor.description]
        results = _cursor.fetchall()

        print(row_headers)
        json_data = []
        for result in results:
            json_data.append(dict(zip(row_headers, result)))
        print(json_data[0])
        # _db.commit()
    except:
        _db.rollback()

    _cursor.close()

    return jsonify(json_data[0])


if __name__ == '__main__':
    app.run(host="0.0.0.0")
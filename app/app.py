from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def all_persons() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'persons'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM all_persons')
    results = [{name: country} for (name, country) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'Return read database as Json': all_persons()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

from flask import Flask, render_template
from flask_cors import CORS
import pandas as pd
import numpy as np
import json
import requests

app = Flask(__name__, static_folder="./dist/static",
            template_folder="./dist/templates")
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/data")
def get_df():
    random_data = np.random.randint(0, 100, size=1000)
    mod = np.array([s % 10 for s in random_data])

    d = {'a': random_data, 'b': mod}
    df = pd.DataFrame(data=d)
    result = df.to_json(orient="columns")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

# These are all we need for our purposes
from flask import Flask, render_template
import pandas as pd
import numpy as np
import json

DEBUG = True
app = Flask(__name__)


@app.route("/data")
def get_df():
    random_data = np.random.randint(0, 100, size=1000)
    mod = np.array([s % 10 for s in random_data])

    d = {'a': random_data, 'b': mod}
    df = pd.DataFrame(data=d)
    result = df.to_json(orient="columns")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4)


if __name__ == '__main__':
    app.run()

from flask import Flask, request
from sklearn.externals import joblib
import json
import pandas as pd


app = Flask(__name__)


@app.route("/")
def hello():
    return "iRoads trained model accessing API"


@app.route('/getIri', methods=['POST'])
def get_iri():
    content = request.json

    df = pd.DataFrame(content["array"])
    print(df)
    joblib_file = "./models/joblib_model-" + content["segment"] + ".pkl"

    model = joblib.load(joblib_file)
    val_predictions = model.predict(df)
    print(val_predictions)

    return json.dumps(val_predictions.tolist())


if __name__ == '__main__':
    app.run(host="0.0.0.0")
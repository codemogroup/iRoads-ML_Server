from sklearn.externals import joblib
import json

import pandas as pd


def predict(input):

    df = pd.DataFrame(input["array"])
    print(df)
    joblib_file = "./models/joblib_model-"+input["segment"]+".pkl"

    model = joblib.load(joblib_file)
    val_predictions = model.predict(df)
    print(val_predictions)

    return json.dumps(val_predictions.tolist())

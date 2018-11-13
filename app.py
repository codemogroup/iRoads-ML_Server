from flask import Flask, request
import predictor
app = Flask(__name__)


@app.route("/")
def hello():
    return "iRoads trained model accessing API"


@app.route('/getIri', methods=['POST']) 
def get_iri():
    content = request.json
    return predictor.predict(content)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9006)
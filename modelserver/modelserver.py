from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def hello():
    return "iRoads trained model accessing API"


@app.route('/getIri', methods=['POST'])
def get_iri():
    content = request.json

    from modelserver import predictor
    return predictor.predict(content)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
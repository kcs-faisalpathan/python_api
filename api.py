import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/healthcheck', methods=['GET'])
def home():
    return "<h1>Python API</h1><p>Your API is healthy!</p>"

@app.route('/details', methods=['GET'])
def detail():
    return "<h1>Python API</h1><p>Your API verion is V1.0.0.</p>"

app.run()
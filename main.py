from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1> Dummy API </h1>"

app.run(host='0.0.0.0')
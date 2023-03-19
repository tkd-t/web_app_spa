from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3001"}})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', text="")

@app.route('/', methods=['POST'])
def response_text():
    # result = request.get_data()
    # print(result)
    # print(request.get_data("text"))
    json_data = request.get_json() # POSTされたjsonを取得
    # dict_data = json.loads(json_data) # jsonを辞書に変換
    print(json_data)
    # return jsonify({"text": json_data["text"]})
    return json_data["text"]


if __name__ == '__main__':
    app.run(debug = True)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():
    return "hello world"

@app.route("/board", methods=['GET'])
def board_list_get():
    return ""


@app.route("/board", methods=['POST'])
def board_list_post():
    return ""
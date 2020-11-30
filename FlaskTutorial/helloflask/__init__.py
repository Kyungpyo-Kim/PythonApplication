from flask import Flask
from flask import g
from flask import Response, make_response

app = Flask(__name__)
app.debug = True

@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)

@app.route('/res2')
def res2():
    return make_response("custom response")

@app.before_request
def before_request():
    print("before_request!")
    g.str="한글"

@app.route('/gg')
def helloworld_global_object():
    return "hello flask world" + getattr(g, 'str', '111')

@app.route('/')
def helloworld():
    return "hello flask world"
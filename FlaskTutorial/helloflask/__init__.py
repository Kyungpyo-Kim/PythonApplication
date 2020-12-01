from flask import Flask
from flask import g
from flask import request, Response, make_response

app = Flask(__name__)
app.debug = True
# app.config['SERVER_NAME']='local.com:5000'

@app.route('/sd')
def helloworld_local():
    return "hello local.com"

@app.route('/sd', subdomain='g')
def helloworld_glocal():
    return "hello Glocal.com"

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

@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = "The request method was %s" % environ['REQUEST_METHOD']
        headers = [('Content-Type', 'text/plain'),('Content-Length', str(len(body)))]
        start_response('200 OK', headers)
        return [body]
    return make_response(application)

@app.route('/rp')
def rp():
    # q = request.args.get('q')
    q = request.args.getlist('q')
    return 'q= %s' % str(q)

@app.route('/')
def helloworld():
    return "hello flask world"
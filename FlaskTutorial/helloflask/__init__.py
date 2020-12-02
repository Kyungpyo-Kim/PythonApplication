from flask import Flask
from flask import g
from flask import request, Response, make_response, session
from datetime import datetime, date, timedelta

app = Flask(__name__)
app.debug = True

app.config.update(
    SECRET_KEY = 'MY super secret key',
    SESSION_COOKIE_NAME = 'MY_FLASK_SESSION',
    PERMANENT_SESSION_LIFETIME=timedelta(31)
)

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

## request 처리용 함수
def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)

@app.route('/')
def helloworld():
    return "hello flask world"

@app.route('/reqenv')
def reqenv():
    return (
        'REQUEST_METHOD: %(REQUEST_METHOD) s <br>'
        'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
        'PATH_INFO: %(PATH_INFO) s <br>'
        'QUERY_STRING: %(QUERY_STRING) s <br>'
        'SERVER_NAME: %(SERVER_NAME) s <br>'
        'SERVER_PORT: %(SERVER_PORT) s <br>'
        'SERVER_PROTOCOL: %(SERVER_PROTOCOL) s <br>'
        'wsgi.version: %(wsgi.version) s <br>'
        'wsgi.url_scheme: %(wsgi.url_scheme) s <br>'
        'wsgi.input: %(wsgi.input) s <br>'
        'wsgi.errors: %(wsgi.errors) s <br>'
        'wsgi.multithread: %(wsgi.multithread) s <br>'
        'wsgi.multiprocess: %(wsgi.multiprocess) s <br>'
        'wsgi.run_once: %(wsgi.run_once) s <br>'
    ) % request.environ

@app.route('/wc')
def write_cookie():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    return make_response(res)

@app.route('/rc')
def return_cookie():
    key = request.args.get('key')
    val = request.cookies.get(key)
    return "cookie: {} {}".format(key, val)

@app.route('/setsess')
def setsess():
    session['Token'] = '123X'
    return "session 이 설정되었습니다."

@app.route('/getsess')
def getsess():
    return session.get('Token')

@app.route('/delsess')
def deltsess():
    if session.get('Token'):
        del session['Token']
    return "session 이 삭제되었습니다."
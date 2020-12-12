from flask import Flask
from flask import g
from flask import request, Response, make_response, session
from flask import render_template, Markup
from flask import url_for
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
app.debug = True
# app.jinja_env.trim_blocks = True

app.config.update(
    SECRET_KEY = 'MY super secret key',
    SESSION_COOKIE_NAME = 'MY_FLASK_SESSION',
    PERMANENT_SESSION_LIFETIME=timedelta(31)
)

# app.config['SERVER_NAME']='local.com:5000'

class Radio:
    def __init__(self, name, id, value, checked):
        self.name = name
        self.id = id
        self.value = value
        self.checked = checked

@app.route('/')
def idx():
    r1 = Radio('aaa', '123', '456', 'checked')
    r2 = Radio('aaa', '123', '456', 'checked')
    r3 = Radio('aaa', '123', '456', '')
    r4 = Radio('aaa', '123', '456', '')
    radio_list = [r1, r2, r3, r4]
    # today = date.today()
    today = datetime.now()
    d = datetime.strptime("2019-02-01", "%Y-%m-%d")
    sdt = d.weekday() * -1
    mm = d.month
    edt = (d + relativedelta(months=1) - timedelta(1)).day + 1
    year = request.args.get('year', date.today().year, int)
    return render_template("app.html", year=year, ttt="TTT", radio_list=radio_list, today=today, sdt=sdt, mm=mm, edt=edt)
@app.route('/main')
def main():
    return render_template('main.html', title='Title')

def make_date(dt, fmt):
    if not isinstance(dt, date):
        return datetime.strptime(dt, fmt)
    else:
        return dt

@app.template_filter('sdt')
def sdt(dt, fmt='%Y-%m-%d'):
    d = make_date(dt, fmt)
    wd = d.weekday()
    return (-1 if wd == 6 else wd) * -1
@app.template_filter('edt')
def edt(dt, fmt='%Y-%m-%d'):
    d = make_date(dt, fmt)
    return (d + relativedelta(months=1) - timedelta(1)).day + 1
@app.template_filter('month')
def month(dt, fmt='%Y-%m-%d'):
    return make_date(dt, fmt).month

@app.route('/tmpl')
def tmpl():
    tit = Markup("<strong>Title</strong>")
    mu = Markup("<h1>iii = <i>%s</i></h>")
    h = mu % "Italic"
    print("h=", h)
    lst2 = []
    lst = [("만남1", "김건모", False), ("만남2", "노사연", False), ("만남3", "노오연",  True), ("만남4", "노육연", True)]
    return render_template('index.html', title=tit, mu = h, lst=lst, lst2=lst2)

class Nav:
    def __init__(self, num, title, name, hide, children=[], url='#'):
        self.title = title
        self.url = url
        self.children = children

@app.route('/tmpl2')
def tmpl2():
    a = (1, "만남1", "김건모", False, [])
    b = (2, "만남2", "노사연", False, [a])
    c = (3, "만남3", "익명", False, [a, b])
    d = (4, "만남4", "익명", False, [a, b, c])

    nav_a = Nav(1, "만남1", "김건모", False, [])
    nav_b = Nav(2, "만남2", "노사연", False, [a])
    nav_c = Nav(3, "만남3", "익명", False, [a, b])
    nav_d = Nav(4, "만남4", "익명", False, [a, b, c])
    return render_template('index2.html', lst=[a,b,c,d], navs = [nav_a, nav_b, nav_c, nav_d])

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

@app.route('/hello_world')
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

@app.template_filter('ymd')
def datetime_ymd(dt, fmt='%m-%d'):
    if isinstance(dt, date):
        return "<strong>%s</strong>" % dt.strftime(fmt)
    else:
        return dt

@app.template_filter('simpledate')
def simpledate(dt):
    if not isinstance(dt, date):
        dt  = datetime.strptime(dt, '%Y-%m-%d %H:%M')
    
    if (datetime.now() - dt).days < 1:
        fmt = "%H:%M"
    else:
        fmt = "%m/%d"
    return "<strong>%s</strong>" % dt.strftime(fmt)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

import os
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint,
                                     filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
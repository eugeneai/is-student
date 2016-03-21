from bottle import *
import os, os.path

CURRD=os.getcwd()

@route("/")
@view("main.pt")
def index():
    return {"name":"Stranger", "phone":"+7 (914) 870 67-54"}

@route('/hello/<name>')
@view('main.pt')
def hello(name):
#    return "Hello,", name, "!" # +7 914 870 67 54
    return {"name":name, "phone":"+7 (914) 870 67-54"}

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename,
        root=os.path.join(CURRD,'static'))

@route('/img/<filename:path>')
def send_static(filename):
    return static_file(filename,
        root=os.path.join(CURRD,'static','img'))

@route('/font-awesome/<filename:path>')
def send_static(filename):
    return static_file(filename,
        root=os.path.join(CURRD,'static','font-awesome'))

# print(TEMPLATE_PATH)

run(host='0.0.0.0', port=8080, reloader=True)

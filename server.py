from bottle import *

@route('/hello/<name>')
def index(name):
#    return "Hello,", name, "!" # +7 914 870 67 54
    return template("main.pt", name=name, phone="+7 (914) 870 67-54")

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename,
        root='/home/stud/Example/2016-appl/is-student/static')

print(TEMPLATE_PATH)

run(host='0.0.0.0', port=8080)

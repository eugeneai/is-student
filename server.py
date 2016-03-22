from bottle import *
import os, os.path
from components import Student
from interfaces import IStorage, IMongoDBStorage, IID, ILoadEvent, IStoreEvent

from zope.interface import directlyProvides, implementer


from zope.component import getUtility, subscribers
from zope.configuration.xmlconfig import xmlconfig
xmlconfig(open("configure.zcml"))

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

@implementer(IID)
class id_holder(object):
    def __init__(self, id):
        self.id=id

def load_object(id):
    oid=id_holder(id)
    obj=subscribers([oid], ILoadEvent)[0].load()
    return obj

@route('/edit/<student_id>')
@view('student.pt')
def edit_get(student_id):
    #storage=getUtility(IStorage, name="database")
    #student=storage.get(student_id, Student)
    student=load_object(student_id)
    message=request.query.get("message",None)
    return {"id":student_id,
            "name":student.name,
            "grades":student.grades,
            "request":request,
            "message":message}

@route('/edit/<student_id>', method="POST")
def edit_post(student_id):
    student=load_object(student_id)

    forms=request.forms
    sid=forms.get("id")
    name=forms.get("name")

    student.name=name
    keys=forms.keys()
    response.status = 303
    for k in keys:
        if k.startswith("grades_"):
            v=forms.get(k)
            vl=v.strip().split(',')
            try:
                vl=[int(g) for g in vl]
            except ValueError:
                response.set_header('Location', '/edit/'+student_id+"?message=Error+in+a+grade+list.")
                return {}
            grade_name=k.replace("grades_","")
            student.replace_grades(grade_name, vl)
    new_id=subscribers([student],IStoreEvent)[0].store()
    response.set_header('Location', '/edit/'+new_id+"?message=Student+updated.")
    return {}  # Enter the body here

# ----------- STATIC ROUTES ---------------------- FIXME Better shortening them to one ---

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

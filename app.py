from bottle import get,post,route,run,template,TEMPLATE_PATH,static_file,request,redirect,Bottle
import os
import pymongo
myclient = pymongo.MongoClient("mongodb://deepz08:deepz08@cluster0-x9rfs.mongodb.net/test?retryWrites=true")

mydb = myclient["demo"]

mycol = mydb["users"]

root=os.getcwd()
TEMPLATE_PATH.insert(0,"./views")

@route('/static/<filepath:path>')
def serve_static(filepath):
    myroot=os.path.join(root,"static")
    return static_file(filepath,root=myroot)

@get('/')
def index():
    return template('login')

@get('/login')
def index():
    return template('login')

@get('/signup')
def index():
    return template('signup')

@post('/login')
def login():
    username=request.forms.get('username');
    password=request.forms.get('password');
    print(username)
    print(password)
    x=mycol.find({"username":username,"password":password})
    print(x)
    result=[]
    for i in x:
        result.append(i)
    
    if(len(result)!=0):
        return "login successful!!"
    else:
        print("login failed!!")
        return template('login')
    

@post('/signup')
def signup():
    username=request.forms.get('username');
    password=request.forms.get('password');
    mycol.insert({"username":username,"password":password})
    print("user added!!")
    return template('login')


@post('/upload')
def upload():
    file=request.files.get('upfile')
    filename,type=os.path.splitext(file.filename)
    print(file)
    file.save(filename+type)
    return "success!!!!!"

@get('/home')
def home():
    redirect('/')


run(host="0.0.0.0",port=int(os.environ.get('PORT',5000)))

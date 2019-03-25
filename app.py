import os
from bottle import get,post,route,run,template,TEMPLATE_PATH,static_file,request,redirect,Bottle

@get('/')
def index():
    return "deployed on Heroku!"

run(host="0.0.0.0",port=int(os.environ.get('PORT',5000)))

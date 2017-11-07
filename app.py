import os
from bottle import *

@route('/')
def index():
  return "Halló heimur"
  
run(host='0.0.0.0',port=os.environ.get('PORT'))

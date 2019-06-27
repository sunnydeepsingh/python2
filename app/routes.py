from app import app
@app.route('/index')
@app.route('/index2')
def index():
    a=8
    b=9
    c=str(index2())
    return str(a+b)+c
def index2():
    return('hello')
    

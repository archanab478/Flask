from flask import Flask,redirect,url_for


app = Flask(__name__)

@app.route('/')

def welcome():
    return"welcome"

@app.route('/success/<int:score>') #score it will be string

def success(score):
    return "welcome success" + str(score)

@app.route('/fail/<int:score>') 

def fail(score):
    return"welcome fail" + str(score)

@app.route('/results/<int:marks>') 
def results(marks): # result checker
    result =""
    if marks < 50:
        result = 'fail'
    else:
        result= 'success'
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run()
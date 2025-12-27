from flask import Flask

## WSGI -web sever gateway interface
app=Flask(__name__)

## decorator
'''This is a decorator that maps a URL to a function.

'/' represents the home page (root URL).

When a user opens http://localhost:5000/, Flask calls the function written just below this decorator.

📌 Interview phrasing:

“This decorator defines the URL endpoint and links it to a Python function.”'''
@app.route('/') #now it is root 
def welcome():  # binding function must be different
    return "welcome to my FLask channel"

@app.route('/members') #now it is root 
def members():
    return "welcome Archana"

if __name__ == '__main__':
    app.run()

# msg = " Welcome to my channel"
# print(msg)
# print("subscribe")
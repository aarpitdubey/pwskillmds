from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello Arpit!</h1>'
# http://127.0.0.1:5000/

@app.route('/about')
def about():
    return '<h1>This Arpit About section</h1>'
# http://127.0.0.1:5000/about

@app.route('/blog')
def blog():
    return '<h1>This is Arpit Blog section</h1>'
# http://127.0.0.1:5000/blog

@app.route('/add')
def add():
    num1 = 5
    num2 = 6
    sum = num1 + num2
    return f"Addition of {num1} and {num2} is : {sum}"
# http://127.0.0.1:5000/add

@app.route('/req/url')
def req():
    data = request.args.get('x')
    return f"This is the data input from my url: {data}"
# http://127.0.0.1:5000/req/url - this work properly but in place of value of x you will get "None".
# http://127.0.0.1:5000/req/url?x=Arpit%20Dubey - To get value of x in place of "None".
        
if __name__ == '__main__':
    app.run(host='0.0.0.0')
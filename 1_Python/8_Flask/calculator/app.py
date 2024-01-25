from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_operation():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        
        if(ops == 'add'):
            r = num1 + num2
            result = f"The sum of {num1} and {num2} is {r}" 
        elif ops == 'substract':
            r = num1 - num2
            result = f"Substraction of {num2} from {num1} is {r}" 
        elif ops == 'multiply':
            r = num1 * num2
            result = f"Multiplication of {num1} and {num2} is {r}" 
        else:
            r = num1 // num2
            result = f"Division of  {num1} and {num2} is {r}" 
        
        return render_template("results.html", result = result)
    
@app.route('/postman_api', methods=['POST'])
def postman_calculation():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        
        if(ops == 'add'):
            r = num1 + num2
            result = f"The sum of {num1} and {num2} is {r}" 
        elif ops == 'substract':
            r = num1 - num2
            result = f"Substraction of {num2} from {num1} is {r}" 
        elif ops == 'multiply':
            r = num1 * num2
            result = f"Multiplication of {num1} and {num2} is {r}" 
        else:
            r = num1 // num2
            result = f"Division of  {num1} and {num2} is {r}" 
        
        return jsonify(result)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0')
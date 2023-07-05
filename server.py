from flask import Flask  

app = Flask(__name__)  

@app.route('/')          
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')
def success():
    return "Dojo" 

@app.route('/say/flask')
def hello():
    return "Hi Flask"

@app.route('/say/michael')
def based():
    return "Hi michael"

@app.route('/repeat/<string:name>/<int:num>')
def repeat(name,num):
    return f"Hi, {name * num} "

if __name__=="__main__":    
    app.run(debug=True)     


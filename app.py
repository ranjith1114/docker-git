from flask import Flask 
app = Flask(__name__) 
  
@app.route('/') 
def hello(): 
    return "welcome to the flask tutorials"

@app.route('/hi') 
def helloo(): 
    return "welcome!!"
  
@app.route('/bye') 
def bye(): 
    return "bye..!!"
  
  
if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)  

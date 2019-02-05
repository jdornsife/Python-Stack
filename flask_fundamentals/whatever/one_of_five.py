from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route('/')

def hello_world():
    return 'Hello World'
if __name__=="__main__":
    
    app.run(debug=True)

@app.route('/Dojo')
def Dojo():
    return 'Dojo'

@app.route('/Hi_Flask')
def Hi_Flask():
    return 'Hi_Flask'

@app.route('/Hi_Michael')
def Hi_Michael():
    return 'Hi_Michael'

@app.route('/Hi_John')
def Hi_John():
    return 'Hi_John'

@app.route('/hello/<name>')
def hello(name):
    int(35)
    print(name)
    return "hello"+'name'

def show_user_profile(username,id):
    print(username)
    print(id)
    return "username:"+ username +",id"+id

@app.route('dogs/<name>')
def dog(name):
    int(99)
    print(name)
    return 'dogs'+'name'





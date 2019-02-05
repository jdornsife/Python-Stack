from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Welcome(self,header):
    self.header = Welcome
    return "render_template("index.html")

@app.route('/play,number,color')
def play(number,color):
    return render_template("playground.html",num=int(number),change=color)


@app.route("/repeat/<number>/<name>")
def repeater(name,number):
    str = "name"
    num = int(number)
    for i in range(num):
        return str

if __name__=="__main__":
    app.run(debug=True)
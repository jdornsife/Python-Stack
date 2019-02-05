from flask import Flask, session, render_template,redirect

app= Flask(__name__)
app.secret_key = "times"

@app.route('/')
def counter():
    if not "counter" in session:
        session['counter'] = 0
    else: 
        session ["counter"] +=1
    return render_template('counter.html')


@app.route('/destroy_session')
def reset_session():
    session.clear()
    return redirect('/')


@app.route('/addtwo')
def addtwo():
    session["counter"]+=1
    return redirect('/')

app.run(debug=True)
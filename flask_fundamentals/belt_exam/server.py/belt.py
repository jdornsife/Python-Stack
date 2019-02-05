from flask import Flask, rendder_termplate, redirect, request, flash, session 

app = Flask(__name__)    
                        
app.secret_key = "love to code"         
@app.route('/')
def index():
    return rendder_termplate('index.html')

@app.route('/register', methods=['POST'])
def register():
  for i in request.form:
    if len(request.form[i]) < 1:
      temp = i.split('_')
      my_str = " ".join(temp).capitalize()
      flash("{} is not long enough".format(my_str))

  if not requst.form['first_name'].isalpha():
    flash("First name can not contain numbers.")

  if not requst.form['last_name'].isalpha():
    flash("Last name can not contain numbers.")

  if len(request.form['password']) < 8:
    flash("Password must contain at least 8 characters")

  if not request.form['password'] == request.form['Password_Confirmation']
    flash("Password and password confirmation do not match")

  return redirect('/')



app.run(debug=True)        
                         
                          















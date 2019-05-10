from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)
app.config ['DEBUG']=True


@app.route("/", methods = ['GET', 'POST'])
def index():
    username = request.args.get('username', '')
    error = request.args.get('error')
    pwerror = request.args.get('pwerror')
    email = request.args.get('email', '')
    badusername = request.args.get ('badusername')


    return render_template("index.html", username=username, error=error, pwerror=pwerror,email=email, badusername=badusername)



@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify-password']
        username = request.form['username']
        short = len(password)

        if not is_username(username):
            usernameerror = 'Please choose a username between 3-20 characters. Exclude spaces.'
            return redirect('/?badusername=' + usernameerror)
        
        if not is_email(email):
            notemail = 'Please enter a valid email'
            return redirect('/?username='+ username + '&error=' + notemail)
        
        if password != verify:
            badpw = 'Please enter matching passwords'
            return redirect ('/?username=' + username + '&email=' + email + '&pwerror=' + badpw )         
        if short is 0:
            badpw = 'Please enter matching passwords'
            return redirect ('/?username=' + username + '&email=' + email + '&pwerror=' + badpw )  
        if " " in password:
            badpw = 'Please enter matching passwords'
            return redirect ('/?username=' + username + '&email=' + email + '&pwerror=' + badpw ) 
        else:
            return "<h1>" + "Welcome " + username + "</h1>"

        

def is_email(string):
    string = request.form["email"]
    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    length =len(string) 
    
    if not atsign_present:
        return False
    if length < 3 or length > 20 :
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present

def is_username(string):
    string = request.form['username']
    length =len(string) 
    

    if length < 3 or length > 20:
        return False
    
    else:
        return True


app.run()

    

    
    

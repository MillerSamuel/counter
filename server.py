from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if "count" in session:
        session["count"]+=1
    else:
        session["count"]=0
    
    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect ("/")

@app.route("/add")
def add2():
    session['count']+=1
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
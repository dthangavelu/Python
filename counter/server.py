
from flask import Flask, render_template, redirect, request, url_for, session

logging = True

app = Flask(__name__)
app.secret_key = "secretKey"

@app.route("/")
def index():	
	if 'count' not in session:
		session['count'] = 1
	else:
		session['count'] += 1
		
	return render_template("index.html", counter_val=session['count'])

@app.route("/reset")
def reset():
	session['count'] = 0
	return redirect("/")

@app.route("/add2_to_counter")
def add2_to_counter():
	session['count'] += 1
	return redirect("/")
	
app.run(debug=logging)
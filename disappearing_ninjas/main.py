
from flask import Flask, render_template, redirect, request, url_for

logging = True

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/ninja")
def ninja():				
	return redirect(url_for('specificNinja', color="default"))

@app.route("/ninja/<color>")
def specificNinja(color):	
	print "color************", color
	color = color.lower();	
	if color == "default":
		img_to_render = url_for('static', filename='images/tmnt.png')
	elif color == "blue":		
		img_to_render = url_for('static', filename='images/leonardo.jpg')
	elif color == "orange":		
		img_to_render = url_for('static', filename='images/michelangelo.jpg')
	elif color == "red":		
		img_to_render = url_for('static', filename='images/raphael.jpg')
	elif color == "purple":		
		img_to_render = url_for('static', filename='images/donatello.jpg')
	else:
		img_to_render = url_for('static', filename='images/notapril.jpg')			
	return render_template("ninja.html", render_img=img_to_render)
app.run(debug=logging)
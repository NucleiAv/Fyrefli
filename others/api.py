from flask import Flask, jsonify, redirect, url_for, render_template, request, Response
app = Flask(__name__)
import os

def root_dir():
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):
    try:
        src=os.path.join(root_dir(),filename)
        return open(src)
    except IOerror as exc:
        return str(exc)


@app.route('/')
def welcome():
    return 'Welcome to FyreFli'

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
	    user = request.form["nm"]
	    return redirect(url_for("user", usr=user))
    else:
	    # return render_template(get_file("login.html"))
        content = get_file("login.html")
        return Response(content, mimetype="text/html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
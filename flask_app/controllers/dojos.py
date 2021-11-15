from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template ("index.html", dojos=dojos)

@app.route('/createdojo', methods= ["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save_dojo(data)
    return redirect("/")


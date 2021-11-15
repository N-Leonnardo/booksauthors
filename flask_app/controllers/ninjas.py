from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/go_to_add_ninja')
def go_to_add_ninja():
    return redirect("/add_ninja")

@app.route('/go_to_home')
def go_to_home():
    return redirect("/")

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template("create_ninja.html", dojos=dojos)

@app.route('/create_ninja', methods= ["POST"])
def create_ninja():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect("/")

@app.route('/overview/<int:dojo_id>')
def overview_dojo(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    ninjas = Ninja.get_from_dojo(data)
    return render_template("overview.html", ninjas = ninjas)
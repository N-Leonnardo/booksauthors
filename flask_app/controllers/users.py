
from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route("/edit/<int:id>")
def showtouser(id):
    data = {
        "id": id
    }
    one_user = User.get_byid(data)
    return render_template("edit.html", one_user=one_user)


def edit(id):
    data = {
        "id": id
    }
    User.update(data)
    return redirect("/users")
            

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    User.delete_byid(data)
    return redirect("/users")
            

@app.route('/showuser/<int:id>')
def showuser(id):
    data = {
        "id": id
    }
    one_user = User.get_byid(data)
    return render_template("showuser.html", one_user=one_user)


@app.route("/users")
def showusers():
    users = User.get_all()
    print(users)
    return render_template("newuser.html", users=users)


@app.route("/newuser")
def index():
    return render_template("index.html")
            

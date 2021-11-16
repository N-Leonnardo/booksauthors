from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.author import Author

@app.route('/')
def index():
    authors = Author.get_all()
    return render_template ("index.html", authors=authors)

@app.route('/create_author', methods= ["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Author.save_author(data)
    return redirect("/")


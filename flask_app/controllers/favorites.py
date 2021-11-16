from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite

@app.route('/overview_authors/<int:author_id>')
def overview_dojo(author_id):
    data = {
        "author_id": author_id
    }
    books = Book.get_all()
    authors = Author.get_byid(data)
    favorites = Favorite.get_from_author(data)
    print (favorites)
    return render_template("overview_authors.html", favorites = favorites, authors = authors, books=books)


@app.route('/addtofavorites', methods= ["POST"])
def add_book_to_author():
    data = {
        "author_id": request.form["author_id"],
        "book_id": request.form["book_id"]
    }
    Favorite.save_favorite(data)
    return redirect("/")
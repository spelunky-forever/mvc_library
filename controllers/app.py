from flask import Flask, redirect, render_template, request, url_for
from pathlib import Path
import sys
# Ensure the mvc package directory is on sys.path so imports work when running this file directly
sys.path.append(str(Path(__file__).resolve().parents[1]))
from models.library import LibraryModel

app = Flask(__name__, template_folder="../views")
library = LibraryModel()
# Initialized library
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")
library.add_book("Python Programming", "John Zelle")
library.add_book("Fluent Python", "Luciano Ramalho")

@app.route("/")
def home():
    # Show the search page
    return render_template("search.html")

@app.route("/search")
def search():
    # Get search keyword from user
    keyword = request.args.get("keyword", "")
    search_type = request.args.get("type", "bid")
    if search_type == "author":
        results = library.search_by_author(keyword)
    elif search_type == "title":
        results = library.search_by_title(keyword)
    else:
        results = library.search_by_bid(keyword)
    return render_template("results.html", keyword=keyword, books=results)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        library.add_book(title, author)
        return redirect(url_for("home"))
    return render_template("add_book.html")

@app.route("/delete_book", methods=["GET", "POST"])
def delete_book():
    if request.method == "POST":
        bid = request.form.get("id")
        deleted_book = library.delete_book(bid)
        return render_template("delete_result.html",deleted_book=deleted_book ,id=bid)
    return render_template("delete_book.html")
    

if __name__ == "__main__":
    app.run(debug=True)

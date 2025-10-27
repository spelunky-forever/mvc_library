from flask import Flask, redirect, render_template, request, url_for
from pathlib import Path
import sys
# Ensure the mvc package directory is on sys.path so imports work when running this file directly
sys.path.append(str(Path(__file__).resolve().parents[1]))
from models.library import LibraryModel

app = Flask(__name__, template_folder="../views")
library = LibraryModel()

@app.route("/")
def home():
    # Show the search page
    return render_template("search.html")

@app.route("/search")
def search():
    # Get search keyword from user
    keyword = request.args.get("keyword", "")
    search_type = request.args.get("type", "title")
    if search_type == "author":
        results = library.search_by_author(keyword)
    else:
        results = library.search_by_title(keyword)
    return render_template("results.html", keyword=keyword, books=results)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        library.add_book(title, author)
        return redirect(url_for("home"))
    return render_template("add_book.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, render_template, request, redirect, url_for
from datetime import date

app = Flask(__name__)

# Sample Data with Dates
books = [
    {
        "id": 1, 
        "title": "The DevOps Handbook", 
        "author": "Gene Kim", 
        "issued": "2026-01-10", 
        "return_by": "2026-01-25"
    },
    {
        "id": 2, 
        "title": "Docker Deep Dive", 
        "author": "Nigel Poulton", 
        "issued": "2026-01-15", 
        "return_by": "2026-02-01"
    }
]

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    # Get data from the form
    title = request.form.get('title')
    author = request.form.get('author')
    issued = request.form.get('issued')
    return_by = request.form.get('return_by')

    # Create new book object
    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "issued": issued,
        "return_by": return_by
    }
    
    # Add to list
    books.append(new_book)
    
    # Refresh the page
    return redirect(url_for('home'))

@app.route('/api/books', methods=['GET'])
def get_books_api():
    return jsonify(books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
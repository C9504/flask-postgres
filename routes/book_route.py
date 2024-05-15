from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
import uuid
import datetime
from models import db
from models import Book, Author

book_routes = Blueprint('book_routes', __name__)

def generate_uuid():
    return str(uuid.uuid4())

@book_routes.route('/books', methods=['GET'])
def get_all():
    books = Book.query.all()
    return render_template('books/index.html', books=books)

@book_routes.route('/books/create', methods=['GET'])
def create():
    authors = Author.query.all()
    return render_template('books/create.html', book=None, authors=authors)

@book_routes.route('/books', methods=['POST'])
def store():
    if request.method == 'POST':
        try:
            book = Book(
                id=generate_uuid(),
                isbn=request.form['isbn'],
                name=request.form['name'],
                author_id=request.form['author_id'],
                quantity_pages=int(request.form['quantity_pages']),
                created_at=datetime.datetime.now()
            )
            db.session.add(book)
            db.session.commit()
            flash('Book saved successfully', 'success')
            return redirect(url_for('book_routes.create', book=None))
        except Exception as e:
            return jsonify({'message': str(e)}), 500
    
    render_template('books/create.html', book=None)

@book_routes.route('/books/<author_id>', methods=['GET'])
def show(author_id):
    author = Book.query.get(author_id)
    return render_template('books/edit.html', author=author)
    # return jsonify(author.to_dict())

@book_routes.route('/books/<book_id>/edit', methods=['GET'])
def edit(book_id):
    authors = Author.query.all()
    book = Book.query.get(book_id)
    return render_template('books/edit.html', book=book, authors=authors)

@book_routes.route('/books/<book_id>', methods=['POST'])
def update(book_id):
    if request.method == 'POST':
        try:
            book = Book.query.get(book_id)
            book.isbn=request.form['isbn']
            book.name=request.form['name']
            book.author_id=request.form['author_id']
            book.quantity_pages=int(request.form['quantity_pages'])
            db.session.commit()
            flash('Book updated successfully', 'success')
            return redirect(url_for('book_routes.edit', book_id=book_id))
        except Exception as e:
            return jsonify({'message': str(e)}), 500
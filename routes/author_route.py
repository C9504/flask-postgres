from flask import Blueprint, jsonify, url_for, redirect, request, render_template, flash
import uuid, datetime
from models import Author
from models import db
author_routes = Blueprint('author_routes', __name__)

def generate_uuid():
    return str(uuid.uuid4())

@author_routes.route('/authors/greeting', methods=['GET'])
def greeting():
    return jsonify({'message': 'Hello World!'}), 200

@author_routes.route('/authors', methods=['GET'])
def get_all():
    authors = Author.query.all()
    return render_template('authors/index.html', authors=authors)
    # try:
    #     authors = Author.query.all()
    #     authors_dict = [author.to_dict() for author in authors]
    #     return jsonify(authors_dict), 200
    # except Exception as e:
    #     return jsonify({'message': str(e)}), 500

@author_routes.route('/authors/create', methods=['GET'])
def create():
    return render_template('authors/create.html', author=None)

@author_routes.route('/authors', methods=['POST'])
def store():
    if request.method == 'POST':
        try:
            author = Author(
                id=generate_uuid(),
                name=request.form['name'],
                age=request.form['age'],
                created_at=datetime.datetime.now()
            )
            db.session.add(author)
            db.session.commit()
            flash('Author updated successfully', 'success')
            return redirect(url_for('author_routes.create', author=None))
        except Exception as e:
            return jsonify({'message': str(e)}), 500

@author_routes.route('/authors/<author_id>', methods=['GET'])
def show(author_id):
    author = Author.query.get(author_id)
    return render_template('authors/edit.html', author=author)
    # return jsonify(author.to_dict())

@author_routes.route('/authors/<author_id>/edit', methods=['GET'])
def edit(author_id):
    author = Author.query.get(author_id)
    return render_template('authors/edit.html', author=author)
    # return jsonify(author.to_dict())

@author_routes.route('/authors/<author_id>', methods=['POST'])
def update(author_id):
    if request.method == 'POST':
        try:
            author = Author.query.get(author_id)
            author.name = request.form['name']
            author.age = request.form['age']
            db.session.commit()
            flash('Author updated successfully', 'success')
            return redirect(url_for('author_routes.edit', author_id=author_id))
        except Exception as e:
            return jsonify({'message': str(e)}), 500
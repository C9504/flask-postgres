from utils.db import db
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    books = db.relationship("Book", backref="author")

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "age": self.age,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "books": [book.to_dict() for book in self.books]
        }
    # def __repr__(self):
    #     return f"Author(id={str(self.id)!r}, name={self.name!r}, age={self.age!r}, created_at={self.created_at!r})"
    
class Book (db.Model):
    __tablename__ = 'books'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    isbn = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity_pages = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    author_id = db.Column(UUID(as_uuid=True), db.ForeignKey('authors.id'))
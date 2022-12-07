from app import db


# many to many relationships
book_author = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'))
)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    release_date = db.Column(db.Integer, index=True)
    following = db.relationship('Author', secondary=book_author, backref='book')
    borrow = db.relationship('Borrow', backref='book', lazy='dynamic')

    def __str__(self):
        return f"<Book: {self.title}>"


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, index=True)
    last_name = db.Column(db.String, index=True)

    def __str__(self):
        return f"<{self.first_name} {self.last_name}>"

    
class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    borrowed= db.Column(db.String)
    
    def __str__(self):
        return f"<{self.id}: {self.borrowed}>"
    


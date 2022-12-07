from app import app, db
from app.models import Book, Author, Borrow, book_author

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": Book,
       "Author": Author,
       "Borrow": Borrow,
       "book_author": book_author
   }
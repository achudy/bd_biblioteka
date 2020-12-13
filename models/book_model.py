from components.db import db


class BookModel(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    fk_branch_id = db.Column(db.Integer, nullable=False)
    fk_category_id = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    for_adults = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)

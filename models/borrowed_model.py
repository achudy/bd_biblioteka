from components.db import db


class BorrowedModel(db.Model):
    __tablename__ = 'borrowed'
    id = db.Column(db.Integer, primary_key=True)
    fk_book_id = db.Column(db.Integer, nullable=False)
    fk_user_id = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.Date, nullable=False)
    end_time = db.Column(db.Date, nullable=False)

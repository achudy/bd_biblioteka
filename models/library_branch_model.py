from components.db import db


class LibraryBranchModel(db.Model):
    __tablename__ = 'library_branches'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

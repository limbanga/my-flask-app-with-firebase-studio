from app import db
from datetime import datetime

class Seat(db.Model):
    __tablename__ = 'seat'

    id = db.Column(db.Integer, primary_key=True)

    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'), nullable=False)
    # Ghế thuộc về rạp nào

    row = db.Column(db.String(5), nullable=False)
    column = db.Column(db.Integer, nullable=False)
    seat_type = db.Column(db.String(20), nullable=False, default='Standard')

    cinema = db.relationship('Cinema', back_populates='seats')

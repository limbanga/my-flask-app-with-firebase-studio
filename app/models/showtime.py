from app import db
from datetime import datetime

class Showtime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    available_seats = db.Column(db.Integer, nullable=False)

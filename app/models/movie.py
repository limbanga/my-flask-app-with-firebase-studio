from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.Integer)  # phút
    poster_url = db.Column(db.String(255), nullable=True)
    showtimes = db.relationship('Showtime', backref='movie', lazy=True)

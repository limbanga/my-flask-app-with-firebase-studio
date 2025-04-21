from app import db

class Ticket(db.Model):
    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True)

    showtime_id = db.Column(db.Integer, db.ForeignKey('showtime.id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)

    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='booked')  # hoặc 'reserved', 'paid', 'cancelled'

    showtime = db.relationship('Showtime', back_populates='tickets')
    seat = db.relationship('Seat')

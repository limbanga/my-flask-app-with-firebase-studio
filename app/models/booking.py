from app import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'booking'  # Đặt tên bảng rõ ràng (không bắt buộc nhưng tốt)

    id = db.Column(db.Integer, primary_key=True)
    
    # Liên kết với người dùng
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Liên kết với suất chiếu
    showtime_id = db.Column(db.Integer, db.ForeignKey('showtime.id'), nullable=False)
    
    # Số ghế đã đặt, ví dụ: A1, B2, C5...
    seat_number = db.Column(db.String(10), nullable=False)
    
    # Thời điểm đặt vé
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Quan hệ ngược (nếu cần dùng relationship)
    user = db.relationship('User', backref=db.backref('bookings', lazy=True))
    showtime = db.relationship('Showtime', backref=db.backref('bookings', lazy=True))

    def __repr__(self):
        return f'<Booking user={self.user_id}, showtime={self.showtime_id}, seat={self.seat_number}>'

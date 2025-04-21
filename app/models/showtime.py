from app import db
from datetime import datetime
from sqlalchemy.orm import validates
from . import cinema

class Showtime(db.Model):
    """
    Model Showtime đại diện cho một suất chiếu phim cụ thể.
    Mỗi suất chiếu liên kết với một bộ phim và một rạp chiếu,
    có thời gian chiếu và số lượng ghế còn trống.
    """
    __tablename__ = 'showtime'  # Tên bảng rõ ràng

    id = db.Column(db.Integer, primary_key=True)
    # ID duy nhất cho mỗi suất chiếu (Primary Key)

    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    # Khóa ngoại liên kết tới bảng Movie

    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'), nullable=False)
    # Khóa ngoại liên kết tới bảng Cinema

    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Thời gian chiếu, mặc định là thời điểm hiện tại nếu không truyền vào

    available_seats = db.Column(db.Integer, nullable=False)
    # Số lượng ghế còn trống cho suất chiếu

    # Thiết lập quan hệ với Movie (quan hệ 1-n)
    movie = db.relationship('Movie', back_populates='showtimes')

    # Thiết lập quan hệ với Cinema (quan hệ 1-n)
    cinema = db.relationship('Cinema', back_populates='showtimes')

    tickets = db.relationship('Ticket', back_populates='showtime', cascade='all, delete-orphan')
    
    @validates('available_seats')
    def validate_seats(self, key, value):
        """
        Kiểm tra rằng số ghế trống không vượt quá sức chứa của rạp.
        """
        if self.cinema and value > self.cinema.capacity:
            raise ValueError("Số ghế còn trống không thể vượt quá sức chứa của rạp.")
        return value

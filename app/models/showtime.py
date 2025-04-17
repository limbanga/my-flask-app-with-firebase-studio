from app import db
from datetime import datetime

class Showtime(db.Model):
    """
    Model Showtime đại diện cho một suất chiếu phim cụ thể.
    Mỗi suất chiếu liên kết với một bộ phim, có thời gian chiếu và số lượng ghế trống.
    """
    __tablename__ = 'showtime'  # Tên bảng rõ ràng

    id = db.Column(db.Integer, primary_key=True)
    
    # Khóa ngoại liên kết tới bảng movie (bắt buộc phải có movie_id)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    
    # Thời gian chiếu, mặc định là thời điểm tạo nếu không truyền vào
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Số lượng ghế còn trống cho suất chiếu
    available_seats = db.Column(db.Integer, nullable=False)

    # Thiết lập quan hệ ngược về phía Movie (tên thuộc tính: showtimes)
    movie = db.relationship('Movie', back_populates='showtimes')

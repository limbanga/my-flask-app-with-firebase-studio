from datetime import date

from app import db


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    # Tên phim

    description = db.Column(db.Text, nullable=True)
    # Mô tả nội dung phim

    duration = db.Column(db.Integer, nullable=False)
    # Thời lượng phim tính bằng phút

    poster_url = db.Column(db.String(255), nullable=True)
    # Đường dẫn đến hình ảnh poster phim

    genre = db.Column(db.String(50), nullable=True)
    # Thể loại phim (ví dụ: Hành động, Hài, Kinh dị)

    release_date = db.Column(db.Date, nullable=True)
    # Ngày phát hành phim

    director = db.Column(db.String(100), nullable=True)
    # Đạo diễn phim

    actors = db.Column(db.Text, nullable=True)
    # Danh sách diễn viên chính (chuỗi, có thể cách nhau bằng dấu phẩy)

    language = db.Column(db.String(50), nullable=True)
    # Ngôn ngữ của phim (ví dụ: Tiếng Việt, English)

    rated = db.Column(db.String(10), nullable=True)
    # Giới hạn độ tuổi (ví dụ: P, C13, C16, C18)

    trailer_url = db.Column(db.String(255), nullable=True)
    # Đường dẫn video trailer của phim

    is_active = db.Column(db.Boolean, default=True)
    # Trạng thái hiển thị của phim (ẩn / hiện)

    showtimes = db.relationship('Showtime', backref='movie', lazy=True)
    # Danh sách các suất chiếu liên quan đến phim này

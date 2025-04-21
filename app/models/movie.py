from datetime import date
from app import db

class Movie(db.Model):
    """
    Model Movie đại diện cho một bộ phim trong hệ thống.
    Bao gồm các thông tin chi tiết như tiêu đề, mô tả, thời lượng, thể loại, đạo diễn, diễn viên, v.v.
    Mỗi bộ phim có thể có nhiều suất chiếu (Showtimes).
    """
    __tablename__ = 'movie'  # Tên bảng trong cơ sở dữ liệu

    id = db.Column(db.Integer, primary_key=True)
    # ID duy nhất cho mỗi bộ phim (Primary Key)

    title = db.Column(db.String(100), nullable=False)
    # Tên phim

    description = db.Column(db.Text, nullable=True)
    # Mô tả nội dung phim

    duration = db.Column(db.Integer, nullable=False)
    # Thời lượng phim (phút)

    poster_url = db.Column(db.String(255), nullable=True)
    # Đường dẫn đến hình ảnh poster của phim

    genre = db.Column(db.String(50), nullable=True)
    # Thể loại phim (ví dụ: Hành động, Hài, Kinh dị)

    release_date = db.Column(db.Date, nullable=True)
    # Ngày phát hành phim

    director = db.Column(db.String(100), nullable=True)
    # Đạo diễn của phim

    actors = db.Column(db.Text, nullable=True)
    # Danh sách diễn viên chính (cách nhau bằng dấu phẩy)

    language = db.Column(db.String(50), nullable=True)
    # Ngôn ngữ phim (ví dụ: Tiếng Việt, English)

    rated = db.Column(db.String(10), nullable=True)
    # Phân loại độ tuổi (ví dụ: P, C13, C16, C18)

    trailer_url = db.Column(db.String(255), nullable=True)
    # Đường dẫn đến video trailer của phim

    is_active = db.Column(db.Boolean, default=True)
    # Trạng thái phim (True: hiển thị, False: ẩn)

    showtimes = db.relationship('Showtime', back_populates='movie', cascade='all, delete-orphan')
    # Liên kết với các suất chiếu của phim này (quan hệ 1-n)

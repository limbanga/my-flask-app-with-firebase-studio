from datetime import datetime

from app import db
from . import seat, ticket


class Cinema(db.Model):
    """
    Model Cinema đại diện cho một rạp chiếu phim cụ thể.
    Mỗi rạp có tên, vị trí và sức chứa nhất định, và liên kết với nhiều suất chiếu.
    """
    __tablename__ = 'cinema'  # Tên bảng trong cơ sở dữ liệu

    id = db.Column(db.Integer, primary_key=True)
    # ID duy nhất đại diện cho mỗi rạp (Primary Key)

    name = db.Column(db.String(100), nullable=False)
    # Tên của rạp chiếu phim (ví dụ: Galaxy Nguyễn Du)

    location = db.Column(db.String(255), nullable=False)
    # Địa chỉ hoặc vị trí cụ thể của rạp (ví dụ: 116 Nguyễn Du, Quận 1)

    capacity = db.Column(db.Integer, nullable=False)
    # Sức chứa tối đa của rạp (tổng số ghế có thể phục vụ trong một suất chiếu)

    showtimes = db.relationship('Showtime', back_populates='cinema', cascade='all, delete')
    # Thiết lập mối quan hệ 1-n với bảng Showtime.
    # Một rạp có thể có nhiều suất chiếu. Nếu rạp bị xóa, các suất chiếu liên quan cũng bị xóa theo.
    seats = db.relationship('Seat', back_populates='cinema', cascade='all, delete')
from flask import Blueprint, render_template
from app.models.movie import Movie

import logging

logger = logging.getLogger('flask_app') 

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    Trang chủ của website chiếu phim.

    - Phương thức: GET
    - Mục đích: Hiển thị danh sách tất cả các bộ phim hiện có trong hệ thống.
    - Cơ chế:
        + Truy vấn tất cả các bộ phim từ cơ sở dữ liệu.
        + Truyền dữ liệu phim vào template 'main/index.html' để hiển thị.
    - Trả về: HTML hiển thị giao diện trang chủ với danh sách phim.
    """
    logger.info("User accessed profile page")
    movies = Movie.query.all()
    return render_template('main/index.html', movies=movies)

# routes/movie.py
from flask import Blueprint, render_template
from collections import defaultdict
from sqlalchemy.orm import joinedload

from app.models import Movie, Ticket

movie_bp = Blueprint('movie', __name__)

@movie_bp.route('/movies')
def index():
    movies = Movie.query.all()
    return render_template('movie/index.html', movies=movies)


@movie_bp.route('/movies/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    
    # Group showtimes by date and cinema
    grouped_showtimes = defaultdict(lambda: defaultdict(list))

    # Load các ticket liên kết với showtime
    for show in sorted(movie.showtimes, key=lambda s: s.date_time):
        show_date = show.date_time.strftime('%d/%m/%Y')
        cinema_name = show.cinema.name

        # Lấy các ticket cho showtime (cùng seat)
        tickets = Ticket.query.filter_by(showtime_id=show.id).options(joinedload(Ticket.seat)).all()
        show.tickets = tickets  # gán thuộc tính động để dùng trong template

        grouped_showtimes[show_date][cinema_name].append(show)

    return render_template("/main/detail.html", movie=movie, grouped_showtimes=grouped_showtimes)
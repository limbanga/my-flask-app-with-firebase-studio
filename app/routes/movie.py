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

    grouped_showtimes = defaultdict(lambda: defaultdict(list))

    for show in sorted(movie.showtimes, key=lambda s: s.date_time):
        show_date = show.date_time.strftime('%d/%m/%Y')
        cinema_name = show.cinema.name

        # Lấy ticket liên kết với showtime và seat
        tickets = Ticket.query.filter_by(showtime_id=show.id).options(joinedload(Ticket.seat)).all()

        # Biến đổi về dạng JSON-friendly
        serialized_tickets = [
            {
                "id": ticket.id,
                "seat": {
                    "row": ticket.seat.row,
                    "column": ticket.seat.column
                },
                "status": {
                    "value": ticket.status.value  # 'available', 'paid', v.v.
                }
            } for ticket in tickets
        ]

        # Tạo bản ghi showtime
        show_data = {
            "id": show.id,
            "date_time": show.date_time.isoformat(),  # để client chuyển về Date object
            "available_seats": sum(1 for t in tickets if t.status.value == 'available'),
            "tickets": serialized_tickets
        }

        grouped_showtimes[show_date][cinema_name].append(show_data)

    return render_template(
        "/movie/detail.html",
        movie=movie,
        grouped_showtimes=grouped_showtimes
    )
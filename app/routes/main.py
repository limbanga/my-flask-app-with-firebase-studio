from flask import Blueprint, render_template
from app.models.movie import Movie

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    movies = Movie.query.all()
    return render_template('main/index.html', movies=movies)

@main_bp.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('main/detail.html', movie=movie)

# routes/movie.py
from flask import Blueprint, render_template
from app.models.movie import Movie

movie_bp = Blueprint('movie', __name__)

@movie_bp.route('/movies')
def index():
    movies = Movie.query.all()
    return render_template('movie/index.html', movies=movies)

@movie_bp.route('/movies/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('main/detail.html', movie=movie)
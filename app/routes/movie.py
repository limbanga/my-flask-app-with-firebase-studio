# routes/movie.py
from flask import Blueprint, render_template
from app.models.movie import Movie

movie_bp = Blueprint('movie', __name__)

@movie_bp.route('/movies')
def index():
    movies = Movie.query.all()
    return render_template('movie/index.html', movies=movies)
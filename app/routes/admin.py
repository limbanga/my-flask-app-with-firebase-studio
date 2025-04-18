from flask import Blueprint, render_template
from flask_login import login_required
from app.models.movie import Movie

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/movies')
@login_required
def manage_movies():
    movies = Movie.query.all()
    return render_template('admin/movies.html', movies=movies)

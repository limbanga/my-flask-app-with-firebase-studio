from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.movie import Movie
from app.forms import MovieForm
from app import db

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

# Thêm phim
@admin_bp.route('/movies/create', methods=['GET', 'POST'])
@login_required
def create_movie():
    form = MovieForm()
    if form.validate_on_submit():
        movie = Movie(
            title=form.title.data,
            genre=form.genre.data,
            duration=form.duration.data,
            director=form.director.data,
            poster_url=form.poster_url.data,
            release_date=form.release_date.data,
            rated=form.rated.data
        )
        db.session.add(movie)
        db.session.commit()
        flash('🎉 Thêm phim thành công!')
        return redirect(url_for('admin.manage_movies'))
    else: 
        print(form.errors)
    return render_template('admin/create_movie.html', form=form)

# Chỉnh sửa phim
@admin_bp.route('/movies/<int:movie_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = MovieForm(obj=movie)
    if form.validate_on_submit():
        form.populate_obj(movie)
        db.session.commit()
        flash('✅ Cập nhật phim thành công!')
        return redirect(url_for('admin.manage_movies'))
    return render_template('admin/create_movie.html', form=form, movie=movie)
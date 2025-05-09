from flask import Blueprint, render_template
from app.models.movie import Movie
from app.models.cinema import Cinema

import logging

logger = logging.getLogger("flask_app")

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    logger.info("User accessed profile page")
    cinemas = Cinema.query.all()
    movies = Movie.query.all()
    return render_template("main/index.html", movies=movies, cinemas=cinemas)

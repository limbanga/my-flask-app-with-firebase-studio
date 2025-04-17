from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from datetime import datetime

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

login_manager.login_view = 'auth.login'  # Đặt trang đăng nhập nếu người dùng chưa đăng nhập

def create_app(config_class='config.DevConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['DEBUG'] = True
    
    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.booking import booking_bp
    from app.routes.movie import movie_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(movie_bp)
    
    @app.context_processor
    def inject_now():
        return {'current_year': datetime.now().year}

    with app.app_context():
        from app.models import user, movie, showtime, booking
        db.create_all()
         # User loader
        @login_manager.user_loader
        def load_user(user_id):
            return user.User.query.get(int(user_id))
    return app
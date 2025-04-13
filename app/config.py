class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///tickets.db"
    SECRET_KEY = "your-secret-key"
    STRIPE_API_KEY = "sk_test_..."
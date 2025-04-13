from app import create_app, db
from app.models.movie import Movie
from app.models.showtime import Showtime
from app.models.user import User
from datetime import datetime

app = create_app()

# Function to seed the data
def seed_data():
    # Create some movies
    movie1 = Movie(title='Avengers: Endgame', description='The final battle of the Avengers to save the universe.', duration=181, poster_url='https://example.com/avengers.jpg')
    movie2 = Movie(title='Inception', description='A mind-bending thriller about dreams and reality.', duration=148, poster_url='https://example.com/inception.jpg')
    
    # Add movies to session
    db.session.add(movie1)
    db.session.add(movie2)

    # Commit to save movies in the database
    db.session.commit()

    # Create some showtimes for the movies
    showtime1 = Showtime(movie_id=movie1.id, date_time=datetime(2025, 5, 10, 19, 30), available_seats=50)
    showtime2 = Showtime(movie_id=movie1.id, date_time=datetime(2025, 5, 11, 14, 0), available_seats=50)
    showtime3 = Showtime(movie_id=movie2.id, date_time=datetime(2025, 5, 12, 16, 0), available_seats=50)
    
    # Add showtimes to session
    db.session.add(showtime1)
    db.session.add(showtime2)
    db.session.add(showtime3)

    # Commit to save showtimes
    db.session.commit()

    # # Create sample users
    # user1 = User(username='john_doe', email='john@example.com', password='password')
    # user2 = User(username='jane_doe', email='jane@example.com', password='password')


    # # Add users to session
    # db.session.add(user1)
    # db.session.add(user2)

    # Commit to save users
    db.session.commit()

    print('Data seeded successfully!')

# Run the seed function
if __name__ == "__main__":
    with app.app_context():
        seed_data()

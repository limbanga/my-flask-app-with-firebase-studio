from app import create_app, db
from app.models.movie import Movie
from app.models.showtime import Showtime
from app.models.user import User
from datetime import datetime, date, timedelta
import random

app = create_app()

# Function to seed the data
def seed_data():
    
    # Delete old data
    Movie.query.delete()

    db.session.commit()  # Xác nhận xóa
    
    movies = [
        Movie(
            title='Avengers: Endgame',
            description='The final battle of the Avengers to save the universe.',
            duration=181,
            poster_url='https://upload.wikimedia.org/wikipedia/vi/2/2d/Avengers_Endgame_bia_teaser.jpg',
            genre='Action',
            release_date=date(2019, 4, 26),
            director='Anthony Russo, Joe Russo',
            actors='Robert Downey Jr., Chris Evans, Mark Ruffalo',
            language='English',
            rated='C13',
            trailer_url='https://example.com/trailer/avengers',
            is_active=True
        ),
        Movie(
            title='Inception',
            description='A mind-bending thriller about dreams and reality.',
            duration=148,
            poster_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8jIZ4ghU8MiF_BbvSUquG7zEDzlA_rXiqnA&s',
            genre='Sci-Fi',
            release_date=date(2010, 7, 16),
            director='Christopher Nolan',
            actors='Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page',
            language='English',
            rated='C16',
            trailer_url='https://example.com/trailer/inception',
            is_active=True
        ),
        Movie(
            title='Parasite',
            description='A dark comedy thriller about class conflict.',
            duration=132,
            poster_url='https://upload.wikimedia.org/wikipedia/vi/c/cc/Poster_phim_Parasite_2019.jpg',
            genre='Drama',
            release_date=date(2019, 5, 30),
            director='Bong Joon-ho',
            actors='Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong',
            language='Korean',
            rated='C18',
            trailer_url='https://example.com/trailer/parasite',
            is_active=True
        ),
        Movie(
            title='Your Name',
            description='A magical story of two teenagers linked by fate.',
            duration=112,
            poster_url='https://upload.wikimedia.org/wikipedia/vi/thumb/b/b3/Your_Name_novel.jpg/330px-Your_Name_novel.jpg',
            genre='Animation',
            release_date=date(2016, 8, 26),
            director='Makoto Shinkai',
            actors='Ryunosuke Kamiki, Mone Kamishiraishi',
            language='Japanese',
            rated='P',
            trailer_url='https://example.com/trailer/yourname',
            is_active=True
        ),
        Movie(
            title='Joker',
            description='A mentally troubled man becomes the infamous Joker.',
            duration=122,
            poster_url='https://upload.wikimedia.org/wikipedia/vi/9/90/Joker_%28phim_2019%29_poster.jpg',
            genre='Crime',
            release_date=date(2019, 10, 4),
            director='Todd Phillips',
            actors='Joaquin Phoenix, Robert De Niro, Zazie Beetz',
            language='English',
            rated='C18',
            trailer_url='https://example.com/trailer/joker',
            is_active=True
        ),
        Movie(
            title='Dune',
            description='A noble family becomes embroiled in a war for control over a desert planet.',
            duration=155,
            poster_url='https://upload.wikimedia.org/wikipedia/vi/e/e9/Dune_H%C3%A0nh_tinh_c%C3%A1t_poster.jpg',
            genre='Adventure',
            release_date=date(2021, 10, 22),
            director='Denis Villeneuve',
            actors='Timothée Chalamet, Rebecca Ferguson, Zendaya',
            language='English',
            rated='C13',
            trailer_url='https://example.com/trailer/dune',
            is_active=True
        ),
        Movie(
            title='Interstellar',
            description='A team travels through a wormhole in space in an attempt to ensure humanity\'s survival.',
            duration=169,
            poster_url='https://upload.wikimedia.org/wikipedia/vi/4/46/Interstellar_poster.jpg',
            genre='Sci-Fi',
            release_date=date(2014, 11, 7),
            director='Christopher Nolan',
            actors='Matthew McConaughey, Anne Hathaway, Jessica Chastain',
            language='English',
            rated='C13',
            trailer_url='https://example.com/trailer/interstellar',
            is_active=True
        ),
        Movie(
            title='The Lion King',
            description='A young lion prince flees his kingdom only to learn the true meaning of responsibility.',
            duration=88,
            poster_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDdZliCqYzFyAaO1UHNrO0-UT5wx67rCvkbQ&s',
            genre='Animation',
            release_date=date(1994, 6, 15),
            director='Roger Allers, Rob Minkoff',
            actors='Matthew Broderick, Jeremy Irons, James Earl Jones',
            language='English',
            rated='P',
            trailer_url='https://example.com/trailer/lionking',
            is_active=True
        ),
        Movie(
            title='The Dark Knight',
            description='Batman faces off against the Joker.',
            duration=152,
            poster_url='https://upload.wikimedia.org/wikipedia/vi/2/2d/Poster_phim_K%E1%BB%B5_s%C4%A9_b%C3%B3ng_%C4%91%C3%AAm_2008.jpg',
            genre='Action',
            release_date=date(2008, 7, 18),
            director='Christopher Nolan',
            actors='Christian Bale, Heath Ledger, Aaron Eckhart',
            language='English',
            rated='C16',
            trailer_url='https://example.com/trailer/darkknight',
            is_active=True
        ),
        Movie(
            title='Coco',
            description='A young boy discovers his family history in the Land of the Dead.',
            duration=105,
            poster_url='https://upload.wikimedia.org/wikipedia/vi/7/7b/Coco_%28phim_2017%29_poster.jpg',
            genre='Animation',
            release_date=date(2017, 11, 22),
            director='Lee Unkrich, Adrian Molina',
            actors='Anthony Gonzalez, Gael García Bernal, Benjamin Bratt',
            language='English',
            rated='P',
            trailer_url='https://example.com/trailer/coco',
            is_active=True
        ),
        Movie(
            title='Frozen',
            description='A princess sets out on a journey to find her sister.',
            duration=102,
            poster_url='https://m.media-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_FMjpg_UX1000_.jpg',
            genre='Animation',
            release_date=date(2013, 11, 27),
            director='Chris Buck, Jennifer Lee',
            actors='Kristen Bell, Idina Menzel, Josh Gad',
            language='English',
            rated='P',
            trailer_url='https://example.com/trailer/frozen',
            is_active=True
        ),
        Movie(
            title='Titanic',
            description='A love story unfolds on the ill-fated Titanic ship.',
            duration=195,
            poster_url='https://upload.wikimedia.org/wikipedia/vi/a/ab/Titanic_3D_poster_Vietnam.jpg',
            genre='Romance',
            release_date=date(1997, 12, 19),
            director='James Cameron',
            actors='Leonardo DiCaprio, Kate Winslet',
            language='English',
            rated='C13',
            trailer_url='https://example.com/trailer/titanic',
            is_active=True
        ),
        Movie(
            title='Spider-Man: No Way Home',
            description='Peter Parker seeks help from Doctor Strange to restore his secret.',
            duration=148,
            poster_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlWqwmRiDNDFYw-4l3qFdT8TgpjRSTSF5X8A&s',
            genre='Action',
            release_date=date(2021, 12, 17),
            director='Jon Watts',
            actors='Tom Holland, Zendaya, Benedict Cumberbatch',
            language='English',
            rated='C13',
            trailer_url='https://example.com/trailer/spiderman',
            is_active=True
        ),
        Movie(
            title='Minions: The Rise of Gru',
            description='A young Gru dreams of becoming a supervillain.',
            duration=87,
            poster_url='https://play-lh.googleusercontent.com/jcW6qz6j4QnYQbyPiNcP8GGL8TKG-o3YBwCfSsOfBrz5JFEkYEShG7cwWFsDFO0YTk-H8OLSHSjxOhZ0rSk',
            genre='Comedy',
            release_date=date(2022, 7, 1),
            director='Kyle Balda',
            actors='Steve Carell, Pierre Coffin, Taraji P. Henson',
            language='English',
            rated='P',
            trailer_url='https://example.com/trailer/minions',
            is_active=True
        ),
        Movie(
            title='Everything Everywhere All at Once',
            description='A woman is swept into a multiverse adventure.',
            duration=139,
            poster_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpokhJeOkhn_ntJwgmyah-QY-MTByHjcWaWQ&s',
            genre='Fantasy',
            release_date=date(2022, 3, 11),
            director='Daniel Kwan, Daniel Scheinert',
            actors='Michelle Yeoh, Stephanie Hsu, Ke Huy Quan',
            language='English',
            rated='C16',
            trailer_url='https://example.com/trailer/everything',
            is_active=True
        ),
    ]

    db.session.add_all(movies)
    db.session.commit()

    print("15 movies have been seeded successfully.")

    # Create some showtimes for the movies
    # Tạo showtimes cho mỗi movie với thời gian và ghế ngẫu nhiên
    for movie in movies:
        now = datetime.now()
        showtimes = []
        for i in range(3):  # tạo 3 suất chiếu cho mỗi phim
            days_offset = random.randint(1, 7)  # từ 1 đến 7 ngày tới
            hour = random.choice([9, 11, 13, 15, 17, 19, 21])  # giờ chiếu phổ biến
            minute = random.choice([0, 15, 30, 45])  # phút phổ biến
            date_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0) + timedelta(days=days_offset)
            available_seats = random.randint(30, 70)  # số ghế trống từ 30 đến 70

            showtimes.append(
                Showtime(
                    movie_id=movie.id,
                    date_time=date_time,
                    available_seats=available_seats
                )
            )
        
        db.session.add_all(showtimes)

    db.session.commit()
    print("Showtimes have been seeded successfully.")
        
    # # Add showtimes to session
    # db.session.add(showtime1)
    # db.session.add(showtime2)
    # db.session.add(showtime3)

    # # Commit to save showtimes
    # db.session.commit()

    # # # Create sample users
    # # user1 = User(username='john_doe', email='john@example.com', password='password')
    # # user2 = User(username='jane_doe', email='jane@example.com', password='password')


    # # # Add users to session
    # # db.session.add(user1)
    # # db.session.add(user2)

    # # Commit to save users
    # db.session.commit()

    # print('Data seeded successfully!')

# Run the seed function
if __name__ == "__main__":
    with app.app_context():
        seed_data()

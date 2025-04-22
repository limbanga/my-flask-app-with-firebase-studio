import math
import random
import string
from datetime import date, datetime, timedelta

from app import create_app, db
from app.models import *

app = create_app()

def random_rating() -> int:
    return random.randint(1, 10) / 2

def seed_movie():
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
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
            is_active=True,
            rating=round(random_rating(), 1),
            rating_count=random.randint(100, 50000)
        ) 
    ]

    db.session.add_all(movies)
    db.session.commit()

    print("15 movies have been seeded successfully.")

def seed_cinema():
    # Xoá dữ liệu cũ
    Cinema.query.delete()
    db.session.commit()

    cinema_data = [
        {
            "name": "Galaxy Nguyễn Du",
            "location": "116 Nguyễn Du, Quận 1, TP.HCM",
            "capacity": 100
        },
        {
            "name": "CGV Vincom Đồng Khởi",
            "location": "72 Lê Thánh Tôn, Quận 1, TP.HCM",
            "capacity": 120
        },
        {
            "name": "Lotte Cinema Gò Vấp",
            "location": "242 Nguyễn Văn Lượng, Gò Vấp, TP.HCM",
            "capacity": 90
        },
        {
            "name": "BHD Star Bitexco",
            "location": "2 Hải Triều, Quận 1, TP.HCM",
            "capacity": 110
        },
        {
            "name": "Cinestar Quốc Thanh",
            "location": "271 Nguyễn Trãi, Quận 1, TP.HCM",
            "capacity": 85
        },
    ]

    cinemas = []
    for data in cinema_data:
        cinema = Cinema(
            name=data["name"],
            location=data["location"],
            capacity=data["capacity"]
        )
        cinemas.append(cinema)

    db.session.add_all(cinemas)
    db.session.commit()
    print("Cinemas have been seeded successfully.")


def seed_showtime():
    # Xoá toàn bộ showtime cũ
    Showtime.query.delete()
    db.session.commit()

    movies = Movie.query.all()
    cinemas = Cinema.query.all()

    all_showtimes = []

    now = datetime.now()

    for movie in movies:
        for _ in range(random.randint(3, 7)):  # Tạo từ 3 đến 7 suất chiếu cho mỗi phim
            cinema = random.choice(cinemas)
            capacity = cinema.capacity

            days_offset = random.randint(1, 7)
            hour = random.choice([9, 11, 13, 15, 17, 19, 21])
            minute = random.choice([0, 15, 30, 45])
            date_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0) + timedelta(days=days_offset)

            available_seats = random.randint(30, min(70, capacity))

            showtime = Showtime(
                movie_id=movie.id,
                cinema_id=cinema.id,
                date_time=date_time,
                available_seats=available_seats
            )

            all_showtimes.append(showtime)

    db.session.add_all(all_showtimes)
    db.session.commit()

    print(f"Seeded {len(all_showtimes)} showtimes successfully.")


def seed_seat():

    # Xoá dữ liệu cũ
    Seat.query.delete()
    db.session.commit()

    cinemas = Cinema.query.all()
    all_seats = []

    for cinema in cinemas:
        capacity = cinema.capacity

        # Giả sử mỗi hàng có 10 ghế
        seats_per_row = 10
        num_rows = math.ceil(capacity / seats_per_row)

        row_labels = list(string.ascii_uppercase)[:num_rows]  # A, B, C, ...

        for i, row in enumerate(row_labels):
            for col in range(1, seats_per_row + 1):
                if i * seats_per_row + col > capacity:
                    break

                seat = Seat(
                    cinema_id=cinema.id,
                    row=row,
                    column=col,
                    seat_type='Standard'  # có thể random VIP sau
                )
                all_seats.append(seat)

    db.session.add_all(all_seats)
    db.session.commit()
    print("Seats have been seeded successfully.")

def seed_ticket():
    # Xóa dữ liệu cũ
    Ticket.query.delete()
    db.session.commit()

    all_tickets = []

    showtimes = Showtime.query.all()
    for show in showtimes:
        # Lấy ghế của rạp chiếu tương ứng với showtime
        seats = Seat.query.filter_by(cinema_id=show.cinema_id).all()

        # Chọn số ghế tương ứng với số lượng available_seats
        available_seats = show.available_seats
        chosen_seats = random.sample(seats, min(available_seats, len(seats)))

        for seat in chosen_seats:
            ticket = Ticket(
                showtime_id=show.id,
                seat_id=seat.id,
                price=random.choice([70_000, 80_000, 90_000, 100_000]),  # Giá vé ngẫu nhiên
                status=random.choice(list(TicketStatus))
            )
            all_tickets.append(ticket)

    db.session.add_all(all_tickets)
    db.session.commit()
    print("Tickets have been seeded successfully.")

# Run the seed function
if __name__ == "__main__":
    with app.app_context():
        seed_movie()
        seed_cinema()
        seed_showtime()
        seed_seat()
        seed_ticket()
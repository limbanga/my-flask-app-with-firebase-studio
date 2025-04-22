from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.showtime import Showtime
from app.models.ticket import Ticket
from app.models.seat import Seat


# from app.models.booking import Booking

booking_bp = Blueprint('booking', __name__)

# @booking_bp.route('/book/<int:showtime_id>', methods=['GET', 'POST'])
# @login_required
# def book_ticket(showtime_id):
#     showtime = Showtime.query.get_or_404(showtime_id)
#     if request.method == 'POST':
#         seat = request.form.get('seat')
#         if not seat:
#             flash('Vui lòng chọn ghế.', 'warning')
#             return redirect(request.url)

#         booking = Booking(user_id=current_user.id, showtime_id=showtime_id, seat_number=seat)
#         db.session.add(booking)
#         showtime.available_seats -= 1
#         db.session.commit()
#         flash('Đặt vé thành công!', 'success')
#         return redirect(url_for('main.index'))

#     return render_template('booking/book.html', showtime=showtime)

# @booking_bp.route('/my-bookings')
# @login_required
# def my_bookings():
#     bookings = Booking.query.filter_by(user_id=current_user.id).join(Showtime).all()
#     return render_template('booking/my_bookings.html', bookings=bookings)

@booking_bp.route('/booking/<int:showtime_id>')
def book_ticket(showtime_id):
    showtime = Showtime.query.get_or_404(showtime_id)
    
    # Lấy danh sách các ticket của showtime, và thông tin ghế
    tickets = Ticket.query.filter_by(showtime_id=showtime_id).join(Seat).all()
    
    return render_template('booking/book.html', showtime=showtime, tickets=tickets)
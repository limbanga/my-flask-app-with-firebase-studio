from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.showtime import Showtime
from app.models.booking import Booking

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/book/<int:showtime_id>', methods=['GET', 'POST'])
@login_required
def book_ticket(showtime_id):
    showtime = Showtime.query.get_or_404(showtime_id)
    if request.method == 'POST':
        seat = request.form.get('seat')
        if not seat:
            flash('Vui lòng chọn ghế.', 'warning')
            return redirect(request.url)

        booking = Booking(user_id=current_user.id, showtime_id=showtime_id, seat_number=seat)
        db.session.add(booking)
        showtime.available_seats -= 1
        db.session.commit()
        flash('Đặt vé thành công!', 'success')
        return redirect(url_for('main.index'))

    return render_template('booking/book.html', showtime=showtime)

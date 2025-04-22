from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum

from app import db

class TicketStatus(Enum):
    AVAILABLE = 'available'      # Ghế còn trống, chưa được đặt
    RESERVED = 'reserved'        # Ghế đang được giữ chỗ (chưa thanh toán)
    PAID = 'paid'               # Vé đã được thanh toán
    CANCELLED = 'cancelled'     # Vé bị hủy (hoàn tiền hoặc hết hạn)
    USED = 'used'               # Vé đã được sử dụng để vào rạp
    EXPIRED = 'expired'         # Vé hết hạn (quá thời gian giữ chỗ)
    
class Ticket(db.Model):
    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True)

    showtime_id = db.Column(db.Integer, db.ForeignKey('showtime.id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)

    price = db.Column(db.Float, nullable=False)
    status = db.Column(SQLAlchemyEnum(TicketStatus), default=TicketStatus.AVAILABLE, nullable=False)

    showtime = db.relationship('Showtime', back_populates='tickets')
    seat = db.relationship('Seat')

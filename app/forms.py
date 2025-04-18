from flask_wtf import FlaskForm
from wtforms import (DateField, IntegerField, PasswordField, StringField,
                     SubmitField)
from wtforms.validators import (URL, DataRequired, Email, EqualTo, Length,
                                Optional)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    submit = SubmitField('Đăng nhập')

class RegistrationForm(FlaskForm):
    username = StringField('Tên người dùng', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    confirm_password = PasswordField('Xác nhận mật khẩu', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Đăng ký')



class MovieForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[DataRequired()])
    genre = StringField('Thể loại', validators=[Optional()])
    duration = IntegerField('Thời lượng (phút)', validators=[Optional()])
    director = StringField('Đạo diễn', validators=[Optional()])
    poster_url = StringField('URL poster', validators=[Optional(), URL()])
    release_date = DateField('Ngày khởi chiếu', validators=[Optional()])
    rated = StringField('Độ tuổi', validators=[Optional()])
    submit = SubmitField('Lưu')
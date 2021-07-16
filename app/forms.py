from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields
# https://wtforms.readthedocs.io/en/2.3.x/validators/#built-in-validators


class UserLoginForm(FlaskForm):
    email = EmailField (
        '이메일',
        validators = [
            DataRequired('값이 비어있습니다.'),
            Email('올바른 이메일 주소가 아닙니다.')
            ]
        )
    password = PasswordField (
        '비밀번호',
        validators = [
            DataRequired('값이 비어있습니다.')
            ]
        )


class UserCreateForm(FlaskForm):
    username = StringField (
        '닉네임',
        validators = [
            DataRequired('값이 비어있습니다.'),
            Length(min=3, max=25)
            ]
        )
    email = EmailField (
        '이메일',
        validators = [
            DataRequired('값이 비어있습니다.'),
            Email('올바른 이메일 주소가 아닙니다.')
            ]
        )
    password1 = PasswordField (
        '비밀번호',
        validators = [
            DataRequired('값이 비어있습니다.'),
            EqualTo('password2', '비밀번호가 일치하지 않습니다.')
            ]
        )
    password2 = PasswordField (
        '비밀번호 확인',
        validators = [
            DataRequired('값이 비어있습니다.')
            ]
        )
    


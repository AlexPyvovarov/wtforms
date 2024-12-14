from wtforms.validators import DataRequired, Length
from wtforms.fields import SubmitField, RadioField, TextAreaField
from flask_wtf import FlaskForm


class ReviewForm(FlaskForm):
    rating = RadioField("Rate us", choices=[5, 4, 3, 2, 1], validators=[DataRequired()])
    text = TextAreaField("Review text", validators=[DataRequired(), Length(max=300)])
    submit = SubmitField("Send")
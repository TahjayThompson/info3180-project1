

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField,SelectField,TextAreaField
from wtforms.validators import DataRequired

class CreateForm(FlaskForm):
    photo = FileField('image', validators=[
    FileRequired(),
    FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    title = StringField(' Property Title',validators=[DataRequired()])
    bedrooms = StringField('No. Bedrooms',validators=[DataRequired()])
    bathrooms = StringField('No. Bathrooms',validators=[DataRequired()])
    location = StringField('Location',validators=[DataRequired()])
    price = StringField('Price',validators=[DataRequired()])
    pro_type = SelectField('Property Type', choices=[('House'), ('Apartment')])
    description = TextAreaField('Description')


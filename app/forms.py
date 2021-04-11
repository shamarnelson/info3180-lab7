from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField
from wtforms.validators import DataRequired

from wtforms import PasswordField
from wtforms.validators import InputRequired
class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[DataRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','Images Only'])])


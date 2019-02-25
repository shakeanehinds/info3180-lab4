from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    photo = FileField('Photo Uploader', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired, url

class ShortenUrlForm(Form):
    url = StringField('The URL to be shortened:', validators=[DataRequired(), url()])

    def validate(self):
        if not (self.url.data.startswith("http://") or self.url.data.startswith("https://")):
            self.url.data = "http://" + self.url.data

        if not Form.validate(self):
            return False

        return True

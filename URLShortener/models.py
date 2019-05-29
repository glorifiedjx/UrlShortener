from sqlalchemy import desc
from URLShortener import db


class WebUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortUrl = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<WebUrl '{}'>".format(self.shortUrl)

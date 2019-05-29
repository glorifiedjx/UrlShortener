from flask import render_template, flash, redirect, url_for, abort, request
from math import floor
import string

from URLShortener import app, db
from URLShortener.forms import ShortenUrlForm
from URLShortener.models import WebUrl

# try:
from urllib.parse import urlparse  # Python 3
str_encode = str.encode
try:
    from string import ascii_lowercase
    from string import ascii_uppercase
except ImportError:
    from string import lowercase as ascii_lowercase
    from string import uppercase as ascii_uppercase
import base64


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ShortenUrlForm()
    if form.validate_on_submit():
        original_url = form.url.data
        url = str_encode(original_url)
        # base64 encoded url
        base64_encoded = base64.urlsafe_b64encode(url)
        # check if the url already exists
        row = db.session.query(WebUrl).filter_by(shortUrl=base64_encoded).first()
        encoded_string = None
        if(row is None):
            dbShortenedUrl = WebUrl(shortUrl=base64_encoded)
            db.session.add(dbShortenedUrl)
            db.session.commit()
            encoded_string = toBase62(dbShortenedUrl.id)
        else:
            encoded_string = toBase62(row.id)
        # print("___encoded_string___", encoded_string)
        # flash("Stored byte url entered '{}'".format(url))
        # flash("Stored encoded '{}'".format(dbShortenedUrl.shortUrl))

        return render_template('index.html',  original_url=original_url, short_url=request.base_url + encoded_string)
    return render_template('index.html', form=form)

def toBase62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + ascii_lowercase + ascii_uppercase
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

def toBase10(num, b=62):
    base = string.digits + ascii_lowercase + ascii_uppercase
    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res


@app.route('/<short_url>')
def redirect_to_da_url(short_url):
    url = request.base_url
    if(short_url == 'favicon.ico'):
        return url
    highest_id = -1
    if (db.session.query(WebUrl.id).count() <= 0):
        return render_template('404.html'), 404

    highest_id = db.session.query(WebUrl).order_by('id').all()[-1].id
    decoded = toBase10(short_url)
    print("______highest_id______: ", highest_id)
    print("______decoded value______: ", decoded)

    if(highest_id < decoded):
        return render_template('404.html'), 404

    shortUrl = db.session.query(WebUrl).filter_by(id=decoded).first()
    print("___url to be decoded___:",shortUrl.shortUrl)
    try:
        if shortUrl is not None:
            url = base64.urlsafe_b64decode(shortUrl.shortUrl)
    except Exception as e:
        print(e)

    return redirect(url)




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

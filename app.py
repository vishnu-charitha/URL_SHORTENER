from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)


# Create random short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None

    if request.method == 'POST':
        original_url = request.form['url']

        short_code = generate_short_code()

        while URL.query.filter_by(short_code=short_code).first():
            short_code = generate_short_code()

        new_url = URL(
            original_url=original_url,
            short_code=short_code
        )

        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_code

    urls = URL.query.all()

    return render_template(
        'index.html',
        short_url=short_url,
        urls=urls
    )


@app.route('/<short_code>')
def redirect_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first()

    if url:
        url.clicks += 1
        db.session.commit()
        return redirect(url.original_url)

    return "URL not found!"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
# URL Shortener

A full-stack URL Shortener web application built using Python, Flask, SQLite, HTML, CSS, and Bootstrap. The application converts long URLs into short, shareable links and tracks link usage through click analytics.

##  Live Demo

Deployed on Render

##  Features

* Convert long URLs into short URLs
* Automatic redirection to original URLs
* Click tracking and analytics
* URL history management
* Responsive user interface
* Database integration using SQLite
* Cloud deployment using Render
* GitHub version control

##  Tech Stack

### Frontend

* HTML5
* CSS3
* Bootstrap

### Backend

* Python
* Flask
* Flask-SQLAlchemy

### Database

* SQLite

### Deployment

* Render
* Gunicorn

##  Project Structure

```text
URL_SHORTENER/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── urls.db
```

##  Installation

### Clone Repository

```bash
git clone https://github.com/vishnu-charitha/URL_SHORTENER.git
cd URL_SHORTENER
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

##  How It Works

1. User enters a long URL.
2. Application generates a unique short code.
3. URL mapping is stored in the SQLite database.
4. A short URL is generated and displayed.
5. When the short URL is visited, the application redirects users to the original URL.
6. Click counts are updated automatically.

##  Challenges Solved

* URL mapping and redirection logic
* Database integration using SQLAlchemy
* Click tracking implementation
* Cloud deployment using Render
* Production configuration using Gunicorn

##  Future Enhancements

* User authentication
* Custom short URLs
* QR code generation
* URL expiration dates
* Advanced analytics dashboard
* PostgreSQL integration
* REST API support

##  Author

Vishnu Charitha

GitHub: https://github.com/vishnu-charitha

```
```

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:test@localhost/Watchdog"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

class imdbInfo(db.Model):
    __tablename__ = "imdbInfo"

    TTid = db.Column(db.String(50),primary_key=True)
    Title = db.Column(db.String(100))
    PosterURL = db.Column(db.String(120))

    def __init__(self, TTid, Title, PosterURL):
        self.TTid = TTid
        self.Title = Title
        self.PosterURL = PosterURL
    def __repr__(self):
        return "<ID {}>".format(self.TTid)
    def __str__(self):
        return "{}, {}".format(self.TTid, self.Title)
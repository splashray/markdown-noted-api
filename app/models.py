from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password = db.Column(db.String(120), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    notes = db.relationship('Note', backref='user', lazy=True)
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(120), nullable=False)

    content = db.Column(db.Text, nullable=False)

    rendered_html = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "rendered_html": self.rendered_html,
            "user_id": self.user_id
        }



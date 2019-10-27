from app import db
from datetime import datetime

#DECLARING MODEL, MY ITEMS TABLE TO HOLD TO DO ITEMS
class Items(db.Model):
    #five columns including the primary key
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    complete = db.Column(db.Boolean, unique=False)

    def __init__(self,title,content,complete):
        self.title = title
        self.content = content
        self.complete = complete


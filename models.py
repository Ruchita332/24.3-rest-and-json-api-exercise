"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFALUT_IMAGE_URL = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """Cupcake model"""
    __tablename__ ="cupcakes"

    def __repr__(self):
        return f" < Cupcake {self.id} {self.flavor} {self.size} {self.rating}>"

    id = db.Column (db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column (db.Text, nullable = False)
    size = db.Column (db.Text, nullable = False)
    rating = db.Column (db.Float, nullable = False)
    image = db.Column (db.Text, default = DEFALUT_IMAGE_URL)

    def serialize (self):
        """Serialize cupcake to a dict of cupcake info"""
        return {
            "id" : self.id,
            "flavor" : self.flavor,
            "size" : self.size,
            "rating" : self.rating,
            "image" : self.image
        }




def connect_db(app):
    db.app = app
    db.init_app(app)

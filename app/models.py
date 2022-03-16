from . import db

class  Property(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    bedrooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    location = db.Column(db.String(255))
    price = db.Column(db.String(80))
    pro_type = db.Column(db.String(40))
    description = db.Column(db.String(255), )


    def __init__(self, photo,title,bedrooms,bathrooms,location,price,pro_type,description):
        self.title = title
        self.photo = photo
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.pro_type = pro_type
        self.description = description

    def __repr__(self):
        return '<Property %r>' % self.title
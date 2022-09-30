"""Flask app for Cupcakes"""
import json
from flask import Flask, jsonify, render_template, request, jsonify
from models import db, connect_db, Cupcake

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config ['SQLALCHEMY_TRACK_MODICICATIONS']=False

connect_db(app)

@app.route ("/")
def home():
    """Homepage"""
    return render_template ("index.html")

@app.route ("/api/cupcakes")
def list_cupcakes():
    """Return list of all cupcakes in the system"""
    list_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    # print (list_cupcakes)

    return jsonify (cupcakes = list_cupcakes)

@app.route ("/api/cupcakes/<int:cupcake_id>")
def display_cupcake (cupcake_id):
    """Return info of cupcake with cupcake_id"""

    cupcake = Cupcake.query.get_or_404(cupcake_id).serialize()
    print (cupcake)
    return jsonify (cupcake = cupcake)

@app.route ("/api/cupcakes", methods = ["POST"])
def create_new_cupcake():
    """Create a cupcake and return it's data"""
    data = request.json
    new_cupcake = Cupcake (
                        flavor = data ['flavor'],
                        size = data ['size'],
                        rating = data['rating'],
                        image = data.get ('image', None) #image = data['image] or None
    )

    db.session.add(new_cupcake)
    db.session.commit()

    response_json = jsonify (cupcake = new_cupcake.serialize())

    return (response_json, 201) #where 201 is a status code

@app.route ("/api/cupcakes/<int:cupcake_id>", methods = ["PATCH"])
def edit_cupcake(cupcake_id):
    """Upcate a cupcake witht eh id passed in the url and return it's data"""
    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data.get('flavor', cupcake.flavor)
    cupcake.size = data.get('size', cupcake.size)
    cupcake.rating = data.get('rating', cupcake.rating)
    cupcake.image = data.get('image', cupcake.image)

    db.session.add(cupcake)
    db.session.commit()

    return jsonify (cupcake = cupcake.serialize())

    
@app.route ("/api/cupcakes/<int:cupcake_id>", methods = ["DELETE"])
def delete_cupcake (cupcake_id):
    """Delete upcake with the id passed in the URL and respond with delete message"""   
    
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete (cupcake)
    db.session.commit()
    
    return jsonify (message = f"Deleted Cupcake flavoured {cupcake.flavor}")


####################################################################################
#Front end 



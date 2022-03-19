"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app
from flask import render_template, request, redirect, send_from_directory, url_for,flash
from app.forms import CreateForm
from .models import Property
from werkzeug.utils import secure_filename
from . import db



@app.route("/uploads/<filename>")
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


def getprop():
    prop=Property.query.all()
    results=[{
        "photo":p.photo,
        "title":p.title,
        "location":p.location,
        "price":p.price,
        "id":p.idv,
        "bedroom":p.bedrooms,
        "bathroom":p.bathrooms,
        "propertytype":p.pro_type,
        "desc":p.description
        
        
    } for p in prop]
    return results

@app.route('/properties/create/', methods=['POST', 'GET'])
def create():
    form = CreateForm()
    title = form.title.data
    bedrooms = form.bedrooms.data
    bathrooms = form.bathrooms.data
    location = form.location.data
    price = form.price.data
    pro_type = form.pro_type.data
    description = form.description.data
       
    if request.method == 'POST':
        file_obj = request.files['photo']
        path = os.path.join('./uploads',file_obj.filename)
        file_obj.save(path)
        new = Property(file_obj.filename,title,bedrooms,bathrooms,location,price,pro_type,description)
        db.session.add(new)
        db.session.commit()
        flash('Property was successfully added','success')
        flash_errors(form)
        return redirect(url_for('properties'))
    return render_template('create.html',form=form)



# @app.route('/properties')
# def properties():
#     properties = db.session.query(Property).all()   
#     return render_template('properties.html',properties=properties)


@app.route('/properties')
def properties():
    prop=getprop()    
    return render_template('properties.html',prop=prop )



# @app.route('/properties/<propertyid>')
# def property_id(propertyid):
#     property = Property.query.get(property_id) 
#     return render_template('property.html',property=property)
@app.route('/property/<propertyid>')
def viewproperty(propertyid):
    pr = Property.query.get(propertyid) 
    return render_template('property.html', pr=pr)




###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")

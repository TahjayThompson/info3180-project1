"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from curses import flash
import os
from app import app
from flask import render_template, request, redirect, url_for
from app.forms import CreateForm
from .models import Property
from werkzeug.utils import secure_filename
from . import db

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

@app.route('/properties')
def properties():
    # properties = Property.query.all()
    return render_template('properties.html',)




@app.route('/properties/create/', methods=['POST', 'GET'])
def create():
    form = CreateForm()
    if  request.method == 'POST':
        f = form.photo.data
        title = form.title.data
        price = form.price.data
        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        location = form.location.data
        pro_type = form.pro_type.data
        description = form.description.data

        property = CreateForm(f.filename,title,bedrooms,bathrooms,location,price,pro_type,description) 
        db.session.add(property) 
        db.session.commit()
        if f.filename == '':
            flash('No selected file')
        
        # Get file data and save to your uploads folder
        filename = f.filename
        print(filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        f.save(path)
                
        return redirect(url_for('home'))
    return render_template('create.html',form=form)



@app.route('/properties/<propertyid>')
def property_id():
    return render_template('property.html')



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

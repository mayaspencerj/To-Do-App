from app import app
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
from .forms import CreateForm
from .models import db, Items
import os.path


#ROUTE TO BIND FUNCTION TO URL
#FIRST ROUTE TO LOAD WHEN APPLICATION LOADED
@app.route("/")
@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateForm() #CREATE TO DO ITEMS FORM
    #IF SUBMITTED CORRECTLY THEN COMMIT RECORD TO TABLE
    #ERROR MESSAGE WILL TELL USER TO FILL BLANK TEXTBOXES/REDUCE LENGTH OF CONTENT OTHERWISE
    if form.validate_on_submit():
        time = datetime.datetime.now()
        post = Items(title=form.title.data, content=form.content.data, date_posted=time, complete=False, )
        db.session.add(post)
        db.session.commit()
        flash('Your post has now been created!', 'success')
        return redirect(url_for('view_all'))
    #THIS CALLS create.html TEMPLATE
    return render_template('create.html', title='New Post',
                           form=form, legend='New Post')


#ROUTE TO VIEW ALL THE RECORDS / TO DO ITEMS
@app.route("/view_all")
def view_all():
    posts = Items.query.order_by(Items.date_posted.desc()).all()
    return render_template('view_all.html', posts=posts)

#ROUTE TO VIEW ALL COMPLETED TASKS
@app.route("/view_completed/<id>")
def view_completed(id):
    #IF COMPLETE, ID WILL BE 1 (OTHERWISE SET TO 0)
    if int(id)>0:
        post = Items.query.filter_by(id=int(id)).first() #gets specific id of button that was pressed
        post.complete = True #marks it as complete
        db.session.commit()
    else:
        pass
    posts = Items.query.filter_by(complete=True)
    #update record to be complete = 1
    return render_template('view_completed.html', posts=posts)

#ROUTE TO VIEW ALL INCOMPLETE TASKS
@app.route("/view_incomplete")
def view_incomplete():
    posts = Items.query.filter_by(complete=0)
    #DISPLAY TO USER
    return render_template('view_all.html', posts=posts)

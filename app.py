#IMPORT THE REQUIRED FRAMEWORKS / LIBRARIES
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import CreateForm
import os.path

#FLASK CONSTRUCTOR
app = Flask(__name__)

#CHECK IF THE DATABASE HAS CREATED
app.config['SECRET_KEY'] = '234iujvec984c839mji'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
db.create_all()



#DECLARING A MODEL, MY ITEMS TABLE TO HOLD TO DO ITEMS
class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    complete = db.Column(db.Boolean, unique=False)

    def __init__(self,title,content,complete):
        self.title = title
        self.content = content
        self.complete = complete


#DECORATER TO BIND FUNCTION TO URL
@app.route("/")
@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateForm() #CREATE TO DO ITMES FORM
    #IF SUBMITTED CORRECTLY THEN COMMIT RECORD TO TABLE
    #ERROR MESSAGE WILL TELL USER TO FILL BLANK TEXTBOXES OTHERWISE
    if form.validate_on_submit():
        post = Items(title=form.title.data, content=form.content.data, complete=False)
        db.session.add(post)
        db.session.commit()
        flash('Your post has now been created!', 'success')
        return redirect(url_for('view_all'))
    #THIS CALLS create.html TEMPLATE
    return render_template('create.html', title='New Post',
                           form=form, legend='New Post')


#DECORATOR TO VIEW ALL THE RECORDS / TO DO ITEMS
@app.route("/view_all")
def view_all():
    posts = Items.query.order_by(Items.date_posted.desc()).all()
    return render_template('view_all.html', posts=posts)

#DECORATER TO VIEW ALL COMPLETED TASKS
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

#DECORATER TO VIEW ALL INCOMPLETE TASKS
@app.route("/view_incomplete")
def view_incomplete():
    posts = Items.query.filter_by(complete=0)
    #DISPLAY TO USER
    return render_template('view_all.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)

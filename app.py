from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import CreateForm




app = Flask(__name__)

app.config['SECRET_KEY'] = 'amayamaya'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    complete = db.Column(db.Boolean, unique=False)

    def __init__(self,title,content,complete):
        self.title = title
        self.content = content
        self.complete = complete

@app.route("/")
@app.route("/view_all")
def view_all():
    posts = Items.query.all()
    return render_template('view_all.html', posts=posts)

@app.route("/view_completed/<id>")
def view_completed(id):

    if int(id)>0:
        post = Items.query.filter_by(id=int(id)).first() #gets specific id of button that was pressed
        post.complete = True #marks it as complete
        db.session.commit()

    else:
        pass

    posts = Items.query.filter_by(complete=True)
    #update record to be complete =1
    return render_template('view_completed.html', posts=posts)

@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateForm()
    if form.validate_on_submit():
        post = Items(title=form.title.data, content=form.content.data, complete=False)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('view_all'))
    return render_template('create.html', title='New Post',
                           form=form, legend='New Post')

if __name__ == '__main__':
    app.run(debug=True)

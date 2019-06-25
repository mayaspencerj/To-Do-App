from flask import Flask, render_template, url_for, flash, redirect
from forms import CreateForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'amayamaya'

posts = [
    {
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',

    },
    {
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'

    }
]


@app.route("/")
@app.route("/view_all")
def view_all():
    return render_template('view_all.html', posts=posts)


@app.route("/view_completed")
def view_completed():
    return render_template('view_completed.html', title='About')



@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        flash('Post Unsuccessful. Please check minimum requirements', 'danger')
    return render_template('create.html', title='Create', form=form)





if __name__ == '__main__':
    app.run(debug=True)

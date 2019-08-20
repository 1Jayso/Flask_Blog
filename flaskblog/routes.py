
from flask import render_template, url_for, flash, redirect, request
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required




posts = [
    {
        'author': 'Joseph Sowah',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 19, 2019'
    
    }, 

    {

        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 20, 2019'
    
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm() 
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title= 'Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.email.data)


        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember.data)
            flash("Logged in successfylly as {}".format(user.username))
            return redirect(request.args.get("next") or url_for('home'))
        flash("Incorrect email or password")
    return render_template("login.html", title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")
















    
    # About 46% of contributors on tensorflow are based in africa
    # Google -  Research
    # How machine Learning can help break language barrier in Africa.. Africa is  about 2.4Billion
    # Census is really expensive some of the time the statics are outdated.
    # Analysis of satellite images
    # Ai enabled flood forcasting. The app sends a notification whenever there's a chance of flood occurrence


    # Daibetic retinopathy fastest growing cause of blindess in the continent
    # Regular screening is key to prevention about 45% suffer vision loss before diagnosis
    # Deep learning can help analysis images to help i dentify whether a person have diabetic retinopathy



# Statistica



# Web VR....is an open source web platform where you can expirement with VR. you can code webVR with 
# HTMl 
# Issues in VR Ecosystem
# Gatekeepers
# installs
# closed
#   wrting VR code is complex so mozilla introduced A-frame to help minimze the codes we need to write






  



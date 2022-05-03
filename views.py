import sqlite3
from app import app, db
from flask import render_template, request, redirect, session, url_for, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from form import UserForm, Logins, DictionaryWords
from models import Dictionary, User
from models import Role

# from UserLogins import UserLogin

client = MongoClient('mongodb://localhost')
db_m = client.test_database
titles = db_m.posts.find_one()

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', header=titles.get('header', ''), heading=titles.get('heading', ''),
                           content=titles.get('content', ''))


@app.route('/dictionary', methods=['POST', 'GET'])
@login_required
def dictionary():
    form = DictionaryWords()
    if request.method == 'POST':
        try:
            res = Dictionary(eng=request.form.get('eng'), rus=request.form.get('rus'), story=request.form.get('text'))
            db.session.add(res)
            db.session.commit()
            return redirect('/')
        except sqlite3.Error as e:
            db.session.rollback()
            print(f"Ошибка добавления в БД {e}")
    elif request.method == 'GET':
        return render_template('dictionary.html', title='Dictionary', header='Please, fill this dictionary', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        logins = request.form.get('login')
        password = request.form.get('password')
        if logins and password:
            user = User.query.filter_by(name=request.form['login']).first()
            if check_password_hash(user.password, password):
                login_user(user)
                print(request.args.get("next"))
                return redirect("/")
            else:
                flash('This password is wrong')
        else:
            flash('Please fill login or password')
    form = Logins()
    return render_template('login.html', header=titles.get('header', ''), heading=titles.get('heading', ''),
                           content=titles.get('content', ''), form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            hashing = generate_password_hash(request.form['password'])
            user = User(name=request.form['firstname'], email=request.form['email'], password=hashing)
            db.session.add(user)
            db.session.commit()
            return redirect('login')
        except sqlite3.Error as e:
            db.session.rollback()
            print(f"Ошибка добавления в БД {e}")
    form = UserForm()
    return render_template('register.html', header=titles.get('header', ''), heading=titles.get('heading', ''),
                           content=titles.get('content', ''), form=form)


@app.route('/output')
# @login_required
def output_words():
    words = Dictionary.query.all()
    return render_template('output_words.html', itle='Guess words!', header='Please, translate these words', words=words)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('/'))

from flask import Blueprint, render_template, request, redirect, url_for, session, flash, g, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from blueprints.forms import RegisterForm, LogingForm
from exts import db
from models import UserModel,RankingModel

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LogingForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = UserModel.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.uid
                return redirect("/")
            else:
                flash("Password doesn't match the username!")
                return redirect(url_for("user.login"))
        else:
            flash("Username or Password format error!")
            return redirect(url_for("user.login"))


@bp.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            password_hashed = generate_password_hash(password)
            user = UserModel(username=username, password=password_hashed)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            flash("Format error")
            return redirect(url_for("user.register"))


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("user.login"))


@bp.route("/ranking", methods=['POST', 'GET'])
def ranking():
    if request.method == "GET":
        return render_template("404.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            password_hashed = generate_password_hash(password)
            user = UserModel(username=username, password=password_hashed)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            flash("Format error")
            return redirect(url_for("user.register"))
    rank = RankingModel.query.all()
    print(rank)
    # context = {
    #     "rank_user":rank.rank_user,
    #     "rank_id":rank.rank_id,
    #     "wrong_moves":rank.wrong_moves,
    # }
    return redirect(url_for("user.show_ranking"))


@bp.route("/showranking")
def show_ranking():
    rv = RankingModel.query.filter_by(rank_user=g.user.username).order_by(RankingModel.wrong_moves).all()
    payload = []
    content = {}
    for result in rv:
        content = {'username': result.rank_user, 'wrong_moves':result.wrong_moves}
        payload.append(content)
        content = {}
    return render_template("ranking.html", context=payload)


@bp.route("/allranking")
def all_ranking():
    rv = RankingModel.query.order_by(RankingModel.wrong_moves).all()
    payload = []
    content = {}
    for result in rv:
        content = {'username': result.rank_user, 'wrong_moves': result.wrong_moves}
        payload.append(content)
        content = {}
    return render_template("ranking.html", context=payload)
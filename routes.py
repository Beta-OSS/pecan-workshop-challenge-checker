# routes.py
from flask import Blueprint, request, render_template
from flags import flags, check_flag

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/challenges")
def challenges():
    return render_template("challenge.html", challenges=flags)

@bp.route("/submit")
def submit_flag():
    challenge_id = request.args.get("challenge_id")
    flag = request.args.get("flag")

    if not challenge_id or not flag:
        return "Incorrect", 400

    if check_flag(challenge_id, flag):
        return "Correct"
    else:
        return "Incorrect"

@bp.route('/resources')
def resources():
    return render_template('resources.html')

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from leaderboard import Leaderboard
from models import Score


app = Flask(__name__)
Bootstrap(app)


leaderboard = Leaderboard()


@app.route("/")
def index():



    scores = leaderboard.get_scores()
    return render_template("index.html",
                            scores=scores)



@app.route("/player", methods=["GET", "POST"])
def player():
    avatars = leaderboard.get_avatar_dic()
    score = Score(0, 0, "", 0)


    return render_template("player.html", score = score, avatars = avatars)
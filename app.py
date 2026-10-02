import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/rps", methods=["GET", "POST"])
def rps():
    if request.method == "POST":
        player = request.form["choice"]
        computer = random.choice(["rock", "paper", "scissors"])

        if player == computer:
            result = "draw"
        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            result = "You win"
        else:
            result = "Computer  win"

        return render_template(
            "rps.html", player=player, computer=computer, result=result
        )

    return render_template("rps.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    
    question = "What is the capital of India?"
    options = ["Delhi", "Mumbai", "Kolkata", "Punjab"]
    correct_answer = "Delhi"

    if request.method == "POST":
        user_choice = request.form["choice"]

        if user_choice == correct_answer:
            result = "Correct! You win"
        else:
            result = "Wrong Answer! Try again"

        return render_template(
            "quiz.html",
            question=question,
            options=options,
            user_choice=user_choice,
            result=result,
        )

    return render_template("quiz.html", question=question, options=options)



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, flash, redirect, render_template, url_for
from sqlmodel import select
from forms import ReviewForm
from models import Config, Reviews
from config import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/write-review/")
def write_review():
    return render_template("write_review.html", form=ReviewForm())


@app.post("/write-review/")
def write_review_post():
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Reviews(rating=int(form.rating.data),
                            text=form.text.data)
        Config.SESSION.add(new_review)
        Config.SESSION.commit()
        flash('Your review has been sent!', 'success')
        return redirect(url_for("index"))
    return render_template("write_review.html", form=form)


@app.get("/reviews/")
def reviews():
    reviews = Config.SESSION.scalars(select(Reviews)).all()
    return render_template("reviews.html", reviews=reviews)



if __name__ == "__main__":
    app.run(debug=True)
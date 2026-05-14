import pickle
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── Load model artifacts ──────────────────────────────────────────────────────
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
similarity  = pickle.load(open("similarity.pkl",  "rb"))
movies      = pd.DataFrame(movies_dict)          # expects a 'title' column


# ── Core recommendation logic ─────────────────────────────────────────────────
def recommend(movie_title: str, n: int = 5) -> list[str]:
    """Return the top-n similar movie titles for *movie_title*."""
    try:
        idx = movies[movies["title"] == movie_title].index[0]
    except IndexError:
        return []

    distances = sorted(
        enumerate(similarity[idx]),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        movies.iloc[i[0]].title
        for i in distances[1 : n + 1]   # skip the movie itself
    ]


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    titles = sorted(movies["title"].tolist())
    return render_template("index.html", movies=titles)


@app.route("/recommend", methods=["POST"])
def get_recommendations():
    data  = request.get_json()
    title = data.get("title", "")
    recs  = recommend(title)
    return jsonify({"recommendations": recs})


if __name__ == "__main__":
    app.run(debug=True)
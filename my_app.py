import json
from flask import Flask, render_template, request
from decouple import config
from utils import get_corrections



app = Flask(__name__)
app.config["SECRET_KEY"] = config('SECRET_KEY')
app.config['JSON_SORT_KEYS'] = False


with open('probs.json', 'r') as prob_file:
    probs = json.load(prob_file)


with open('vocab.json', 'r') as vocab_file:
    vocab_dict = json.load(vocab_file)
    vocab_set = [i for i in vocab_dict.keys()]
    vocab = set(vocab_set)



@app.route("/", methods=["GET", "POST"])
def index():
    suggestion = {}
    verbose = False
    word = ''
    if request.method == "POST":
        word = request.form.get("word").strip().lower()
        verbose = False if request.form.get("verbose") == "No" else True
        number = int(request.form.get("number"))

        suggestion = get_corrections(word, probs, vocab, number)     

    return render_template("index.html", suggestion=suggestion, verbose=verbose, word=word)
from flask import Flask
from src.use_case import reverse_use_case

app = Flask(__name__)


@app.route("/<input_word>")
def reverse(input_word):
    return reverse_use_case(input_word)

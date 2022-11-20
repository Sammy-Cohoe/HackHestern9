from flask import Flask, render_template, request
from twitterScraper import tweets
from sentimentAnalysis import fiveMostPositive
from sentimentAnalysis import fiveMostNegative

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/')
def topThreePositive():
    return fiveMostPositive, render_template('index.html')

@app.route('/')
def topThreeNegative():
    return fiveMostNegative

if __name__ == '__main__':
    app.run()
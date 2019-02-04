from flask import render_template
from flask import request
from flaskexample import app
import pandas as pd
import pickle as pckl


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Tyler Blair - Insight Data Science',)


@app.route('/ARK')
def ARK():

    topics = pckl.load(open('flaskexample/static/data/ARK_dec8_5topics_trunc_0129.pckl', 'rb'))

    positive = topics['positive']
    recent = topics['recent']

    outputs = []

    for positive, recent in zip(positive, recent):
        outputs.append(dict(positive = positive, recent = recent))

    return render_template('topics_new.html',
    title = 'Insight on ARK Reviews',
    game = 'ARK',
    game_pic = '../static/images/ARK.jpeg',
    plot = '../static/plots/interactive_ARK5.json',
    address = 'address',
    change = 'drop',
    accuracy = '90.8',
    outputs = outputs)


@app.route('/ARK_plot')
def ARK_plot():

    return render_template('json_entry.html')

    #topics = pckl.load(open('flaskexample/static/data/ARK_dec8_topics.pckl', 'rb'))

    #outputs = dict('positive'= topics['positive_20'], 'negative'= topics['negative_20'], 'recent'= topics['recent_20'])

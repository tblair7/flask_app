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

    return render_template('topics.html',
                            game = 'ARK',
                            game_pic = '../static/images/ARK.jpeg',
                            plot = '../static/plots/interactive_ARK.json',
                            accuracy = '90.8')


@app.route('/MHW')
@app.route('/Monster_Hunter_World')
def MWH():

    return render_template('topics.html',
                            game = 'Monster Hunter World',
                            game_pic = '../static/images/MHW.jpeg',
                            plot = '../static/plots/interactive_MHW.json',
                            accuracy = '90.8')

@app.route('/NMS')
@app.route('/No_Mans_Sky')
def NMS():

    return render_template('topics.html',
                            game = 'No Man\'s Sky',
                            game_pic = '../static/images/NMS.jpeg',
                            plot = '../static/plots/interactive_NMS.json',
                            accuracy = '90.8')

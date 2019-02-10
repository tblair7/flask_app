from flask import render_template
from flask import request
from flaskexample import app
import pandas as pd
import pickle as pckl
import os

#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField

from flask import Flask, render_template, request
#app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Tyler Blair - Insight Data Science',)


@app.route('/suggested',methods=['POST', 'GET'])
def suggested():
    if request.method=='POST':
       suggestion=request.form['game']

       f = open("suggestions.txt","a")
       f.write(suggestion + "\n")
       f.close()

       return render_template('suggested.html',
                              suggestion = suggestion)

    else:
        return "error"


#@app.route('/', methods=['POST'])
#def my_form_post():
#    text = request.form['text']
#    processed_text = text.upper()
#    return processed_text


@app.route('/ARK')
def ARK():

    return render_template('topics.html',
                            game = 'ARK',
                            game_pic = '../static/images/ARK.jpeg',
                            plot = '../static/plots/interactive_ARK2.json',
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

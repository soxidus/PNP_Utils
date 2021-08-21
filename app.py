import os
import requests
from flask import Flask, render_template, request, redirect, url_for, abort
# from config import plays_URL

app = Flask(__name__)

# @app.errorhandler(413)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_npc')
def get_games():
    return render_template('generate_npc.html')


@app.route('/stat_list')
def get_games():
    return render_template('stat_list.html')

import os
import requests
from flask import Flask, render_template, request, redirect, url_for, abort
# from config import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_npc')
def generate_npc():
    return render_template('generate_npc.html')


@app.route('/stat_list')
def stat_list():
    return render_template('stat_list.html')

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

@app.route('/slider_appr')
def slider_appr():
    return render_template('slider_appr.html')

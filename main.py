from flask import Flask, render_template, request
import os

def index():
    return render_template("index.html")

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder) 
app.add_url_rule('/', 'index', index)

if __name__ == "__main__":
    app.run()
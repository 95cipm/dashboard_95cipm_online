
from flask import Flask, render_template, request, redirect, send_file
import pandas as pd
import os
from utils import gerar_dashboard

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".xlsx"):
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            gerar_dashboard(path)
            return redirect("/dashboard")
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)

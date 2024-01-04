from flask import Flask, render_template
import pandas as pd
from src.data_preprocessing import load_and_preprocess_data
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/base')
def base():
    return render_template("base.html")


@app.route('/dashboard')
def dashboard():
    data = pd.DataFrame(load_and_preprocess_data())

    # convert dataframe to HTML
    df_html = data.to_html(classes='table table-striped', index=False)

    return render_template("dashboard.html", table=df_html )


if __name__ == '__main__':
    app.run(debug=True)

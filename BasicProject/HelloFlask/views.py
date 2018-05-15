from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "index.html",
        title = "Hello Flask",
        message = "Hello, Flask!",
        content = " on " + formatted_now)

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')

@app.route('/about')
def about(request):
    return render_template(
        "about.html",
        {
            'title' : "About HelloFlask",
            'content' : "Example app page for Flask."
        }
    )
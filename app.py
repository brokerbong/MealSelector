from flask import Flask, render_template
from views import notice

app = Flask(__name__)

app.register_blueprint(notice.bp, url_prefix="/notice")

@app.route('/')
def home():
    #return "Hello, Flask on Heroku!"
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
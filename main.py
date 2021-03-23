from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
# JS
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    app.run()

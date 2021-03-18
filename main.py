from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# JS
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    app.run()

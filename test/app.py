from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/course")
def course():
    with app.open_resource('mock/index.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
    return render_template("course.html", info=info)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    if request.method == 'POST':
        displayinput = request.form['input']
    return render_template("welcome.html", displayinput)

if __name__ == '__main__':
    app.run("0.0.0.0", 3000, debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')  # your existing main page HTML file

if __name__ == "__main__":
    app.run(debug=True)
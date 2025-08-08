from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "SJCAKey"

users = {
    "student1": ["pass123", "student"],
    "teacher1": ["pass456", "teacher"],
    "headmaster": ["admin123", "head"]
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('main_page'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username][0] == password:
            session['username'] = username
            session['role'] = users[username][1]
            return redirect(url_for('main_page'))
        else:
            error = "Invalid username or password."
    return render_template('login.html', error=error)

@app.route('/main')
def main_page():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('main.html', username=session['username'], role=session['role'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)



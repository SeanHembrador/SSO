from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# In-memory user "database"
users = {
    'admin': generate_password_hash('admin123')
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and check_password_hash(users[username], password):
            session['user'] = username
            return f'Welcome, {username}!'
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/signup')
def signup():
    return '<h3>Signup Page Placeholder</h3>'

@app.route('/oauth2/authorization/google')
def google_login():
    return '<h3>Google OAuth login placeholder</h3>'

if __name__ == '__main__':
    app.run(debug=True)

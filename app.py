import os
import hashlib
import random
import string
import json
from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management
socketio = SocketIO(app)

# Ensure the users directory exists
if not os.path.exists('./users'):
    os.makedirs('./users')

# File path for user data
USER_DATA_FILE = './users/secret.key'

def load_users():
    """Load user data from the file."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # If the file is empty or contains invalid JSON, return an empty dictionary
                return {}
    return {}

def save_users(users):
    """Save user data to the file."""
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f)

def generate_token():
    """Generate a random SHA-256 token."""
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return hashlib.sha256(random_string.encode()).hexdigest()

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    users = load_users()  # Load users from file
    if request.method == 'POST':
        username = request.form['username']
        if username and username not in users:
            token = generate_token()
            users[username] = token
            save_users(users)  # Save updated users to file
            return render_template('token_display.html', username=username, token=token)
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    users = load_users()  # Load users from file
    if request.method == 'POST':
        username = request.form['username']
        token = request.form['token']
        if username in users and users[username] == token:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = "Invalid username or token. Please try again."
            return render_template('login.html', error=error)
    return render_template('login.html')

@socketio.on('message')
def handle_message(msg):
    print('Received message: ' + msg)
    socketio.send(msg)  # Broadcast the message to all clients

if __name__ == '__main__':
    socketio.run(app, debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = '001100'  # Needed for flash messages

# Initialize the database
def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                email TEXT,
                password TEXT,
                phone TEXT
            )
        ''')
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'signin' in request.form:
            username = request.form['username']
            password = request.form['password']
            with sqlite3.connect('users.db') as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
                user = cursor.fetchone()
                if user:
                    return redirect(url_for('home'))
                else:
                    flash('Invalid username or password', 'error')
        
        elif 'signup' in request.form:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            phone = request.form['phone']
            with sqlite3.connect('users.db') as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute('INSERT INTO users (username, email, password, phone) VALUES (?, ?, ?, ?)', 
                                (username, email, password, phone))
                    conn.commit()
                    flash('Sign up successful, please sign in.', 'success')
                except sqlite3.IntegrityError:
                    flash('Username already exists', 'error')
                    
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/Training Program')
def training_program():
    return render_template('Training Program.html')

@app.route('/Healthy_diet')
def healthy_diet():
    return render_template('Healthy_diet.html')

@app.route('/Progress')
def progress():
    return render_template('Progress.html')

@app.route('/Problems')
def problems():
    return render_template('Problems.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

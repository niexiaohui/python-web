from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def hello():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('hello'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/background')
def background():
    return send_from_directory('图片', '65830 “硬”核思维导图.png')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return 'Login page here!'

@app.route('/dashboard')
def dashboard():
    return 'Hello dashboard!'

if __name__ == '__main__':
    app.run()

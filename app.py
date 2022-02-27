from flask import Flask, render_template, request, abort

# https://www.codementor.io/@chirilovadrian360/jinja-templates-open-source-and-free-194mvcg66x

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()

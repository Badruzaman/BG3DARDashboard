from flask import Flask, render_template, request, abort

app = Flask(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()

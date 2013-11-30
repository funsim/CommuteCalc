from flask import Flask, url_for, redirect

app = Flask('commutecalc_frontend')

@app.route('/commutecalc/')
def home():
    return redirect(url_for('static', filename='index.html'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001)

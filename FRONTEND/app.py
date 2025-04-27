from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/cep')
def cep():
    return render_template('cep.html')

@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.html')

@app.route('/megasena')
def megasena():
    return render_template('megasena.html')

if __name__ == '__main__':
    app.run(debug=True)
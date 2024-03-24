from flask import Flask, render_template
import sqlite3
# import random

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/pizza/<int:id>')
def pizza(id):
    conn = sqlite3.connect('Pizza.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Pizza WHERE id = ?', (id,))
    pizza = cur.fetchone()
    return render_template('pizza.html', pizza=pizza)


if __name__ == "__main__":
    app.run(debug=True)
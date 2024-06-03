from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    
    conn = sqlite3.connect('ipo.db')
    c = conn.cursor()

   
    c.execute("SELECT * FROM ipo_data")

  
    rows = c.fetchall()

  
    conn.close()

   
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)

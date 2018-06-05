import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def get_index():
    return render_template('index.html')
    
@app.route("/results")
def get_results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)

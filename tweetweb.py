import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def get_index():
    return render_template('index.html')
    
@app.route("/results")
def get_results():
    results = [
        {'id': 1003934266038849536, 'text': 'Hello'},
        {'id': 1003995254486282240, 'text': 'This is another tweet'},
        ]
    return render_template('results.html', tweets=results)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)

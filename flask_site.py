from flask import Flask, render_template
import pickle
import random
quotes_dict = pickle.load(open('quotes_dict2.pkl', 'rb'))
app = Flask(__name__)

def random_quote():
    name, message = random.choice(list(quotes_dict.items()))
    return name, message

@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name="Mark"):
    return render_template('hello.html', name=name)

@app.route('/quote/')
@app.route('/quote/<name><message>')
def quote():
    name, message = random_quote()
    return render_template('quote_page.html', name=name, message=message)
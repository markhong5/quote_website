from flask import Flask, render_template, redirect, url_for, request
import pickle
import random
quotes_dict = pickle.load(open('quotes_dict2.pkl', 'rb'))
app = Flask(__name__)

def random_quote():
    name, message = random.choice(list(quotes_dict.items()))
    return name, message

def chosen_quote(name):
    if name in quotes_dict:
        quote = quotes_dict[name]
    else:
        quote = "Not a valid name"
    return name, quote

@app.route('/quote/')
@app.route('/quote/<name><message>')
def quote(author=None):
    if author == None:
        name, message = random_quote()
    else:
        name, message = chosen_quote(author)
    return render_template('quote_page.html', name=name, message=message)

@app.route('/listquotes/',methods = ['POST', 'GET'])
def list_quotes():
    if request.method == 'POST':
        auth = request.form['nm']
        return redirect(url_for('quote', type_of_quote_function=chosen_quote, author=auth))
    quote_names = sorted(quotes_dict.keys())
    split_names = [[],[],[],[],[]]
    for i, name in enumerate(quote_names):
        split_names[i % len(split_names)].append(name)
    return render_template('list_quotes.html', split_names=split_names)

@app.route('/quote/',methods = ['POST'])
def specific_quote():
    if request.method == 'POST':
        author = request.form['nm']
        return quote(author)

"""
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="Mark"):
    return render_template('hello.html', name=name)
    """


if __name__ == "__main__":
    list_quotes()
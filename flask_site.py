from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name="Mark"):
    return render_template('hello.html', name=name)

@app.route('/quote/')
@app.route('/quote/<name><message>')
def quote(name='Ashley', message='Hi there'):
    return render_template('quote_page.html', name=name, message=message)
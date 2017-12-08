import flask
app = flask.Flask(__name__)    

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='World'):
    return flask.render_template('hello_template.html', name=name, flavour='vanilla')

@app.route('/greetings')
def greetings():
    return "Nice greetings"

if __name__ == '__main__':
    app.run('localhost', 8080, True)  
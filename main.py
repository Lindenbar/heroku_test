from bottle import Bottle

app = Bottle()

app.route('/')


def test():
    return '<h1>HELLO</h1>'

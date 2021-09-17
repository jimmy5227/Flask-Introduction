# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operations = {'add': add, 'sub': sub, 'mult': mult, 'div': div}


@app.route('/math/<method>')
def math(method):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[method](a, b)

    return f'<h1>{method} a and b together: {result}</h1>'

# @app.route('/add')
# def page_add():
#     a = request.args.get('a')
#     b = request.args.get('b')

#     return f'<h1>Adding a and b together: {add(int(a),int(b))}</h1>'


# @app.route('/sub')
# def page_subtract():
#     a = request.args.get('a')
#     b = request.args.get('b')

#     return f'<h1>Subtracting a and b together: {sub(int(a),int(b))}</hh1>'


# @app.route('/mult')
# def page_multiply():
#     a = request.args.get('a')
#     b = request.args.get('b')

#     return f'<h1>Multiplying a and b together: {mult(int(a),int(b))}</h1>'


# @app.route('/div')
# def page_div():
#     a = request.args.get('a')
#     b = request.args.get('b')

#     return f'<h1>Dividing a and b together: {div(int(a),int(b))}</h1>'

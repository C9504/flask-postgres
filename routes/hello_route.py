from flask import Blueprint

hello_route = Blueprint('hello_route', __name__)

@hello_route.route('/', methods=['GET'])
def index():
    return 'Welcome to Flask Application!'
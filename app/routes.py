from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = []  # Placeholder 
    return "Nothing now"
    # return render_template('search.html', results=results, query=query)
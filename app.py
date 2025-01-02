from flask import Flask, request, jsonify
from faqs import find_best_match

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the FAQ Search API! Use the `/search` endpoint to find answers."

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Suppress favicon request errors

@app.route('/search', methods=['POST'])
def search_faq():
    query = request.json.get('query', '')
    if not query:
        return jsonify({"error": "Query cannot be empty"}), 400
    
    # Replace this with your FAISS search logic
    result = find_best_match(query)  # Assuming you implemented this function
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)






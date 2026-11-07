from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

data = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    return jsonify({"message": "Welcome to our Home Page!"}), 200

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [item for item in data if item["category"] == category]
        return jsonify(filtered), 200
    return jsonify(data), 200
  # TODO: Return all products or filter by ?category=

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    for p in data:
       if p["id"] == id:
          return jsonify(p), 200
    return jsonify({"message": "Product not found"}), 404  
# TODO: Return product by ID or 404

if __name__ == "__main__":
    app.run(debug=True)

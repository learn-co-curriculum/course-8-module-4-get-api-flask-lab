from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product API!"}), 200  # TODO: Return a welcome message

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")  # TODO: Return all products or filter by ?category=
    if not category:
        return jsonify(products), 200
    filtered = [
        p for p in products
        if p.get("category","").lower() == category.lower()
    ]
    return jsonify(filtered), 200
# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((p for p in products if p.get("id") == id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404  # TODO: Return product by ID or 404
    return jsonify(product), 200

if __name__ == "__main__":
    app.run(debug=True)

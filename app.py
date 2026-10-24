
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock product data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]


# Homepage
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product API"}), 200


# Get all products or filter by category
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        filtered_products = [
            product for product in products
            if product["category"].lower() == category.strip().lower()
        ]
        return jsonify(filtered_products), 200

    return jsonify(products), 200


# Get a single product by ID
@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Welcome to the home page")

@app.route("/products")
def get_products():
    category = request.args.get("category")
    if category is not None:
        category = category.lower()
        filtered_products = [
            product for product in products
            if product["category"].lower() == category
        ]
        return jsonify(filtered_products)
    return jsonify(products)

@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((product for product in products if product["id"] == id), None)
    if product is None:
        return jsonify(message="Product not found"), 404
    return jsonify(product)

if __name__ == "__main__":
    app.run(debug=True)

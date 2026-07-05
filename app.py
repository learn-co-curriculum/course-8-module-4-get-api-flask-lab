from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the product catalog API!"})


@app.route("/products")
def get_products():
    category = request.args.get("category")

    if category:
        category = category.lower()
        filtered_products = [
            product for product in products if product["category"].lower() == category
        ]
        return jsonify(filtered_products)

    return jsonify(products)


@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((item for item in products if item["id"] == id), None)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product)


if __name__ == "__main__":
    app.run(debug=True)
